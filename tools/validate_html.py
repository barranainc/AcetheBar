#!/usr/bin/env python3
"""
validate_html.py — AcetheBar index.html integrity checker
==========================================================
Validates that index.html is safe to ship:

  1. JavaScript syntax — extracts <script> block, checks with `node --check`
  2. _DATA payload lengths — all known exam keys match expected b64 lengths
  3. All exam keys in _DATA have a matching entry in EXAMS config
  4. All exam keys have a matching tab button and panel div in the HTML
  5. No unterminated string in _DATA (scans every b64 value for a closing quote)

Usage:
    python3 tools/validate_html.py [--html PATH]

Exit codes:
    0 — all checks passed
    1 — one or more checks failed

Run this before every commit that touches index.html.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DEFAULT_HTML = REPO_ROOT / "index.html"

# ── Known frozen payload lengths ──────────────────────────────────────────────
# Update this dict whenever a new generated exam is permanently baked in.
FROZEN_LENGTHS: dict[str, int] = {
    "bar":  191500,
    "sol":  242816,
    "mini": 171132,
    "abp":  189540,
    "bar2": 237360,
}

B64_CHARS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")

def get_b64_length(content: str, key_pos: int) -> tuple[int, bool]:
    """Return (length, closes_correctly) for a _DATA b64 value starting at key_pos."""
    quote_open = content.find('"', key_pos)
    if quote_open == -1:
        return 0, False
    i = quote_open + 1
    while i < len(content) and content[i] in B64_CHARS:
        i += 1
    length = i - quote_open - 1
    closes = content[i] == '"'
    return length, closes


def find_data_entries(content: str) -> dict[str, tuple[int, bool]]:
    """Return {key: (b64_length, closes_correctly)} for all entries in _DATA."""
    data_start = content.find("_DATA = {")
    if data_start == -1:
        return {}
    data_end = content.find("\n};", data_start)
    data_block = content[data_start:data_end + 3]

    results = {}
    pos = 0
    while True:
        m = re.search(r'[,{\s\n](\w+):\s*"', data_block[pos:])
        if not m:
            break
        key = m.group(1)
        abs_pos = data_start + pos + m.end()  # position just after opening quote
        length, closes = get_b64_length(content, abs_pos - 1)  # pass pos of "
        results[key] = (length, closes)
        pos += m.end()
    return results


def check_js_syntax(html_path: Path) -> list[str]:
    """Extract <script> block and validate with node --check."""
    errors = []
    content = html_path.read_text(encoding="utf-8")
    script_start = content.find("<script>")
    script_end = content.rfind("</script>")
    if script_start == -1 or script_end == -1:
        errors.append("Could not locate <script> block")
        return errors
    js_block = content[script_start + len("<script>"):script_end]
    with tempfile.NamedTemporaryFile(suffix=".js", mode="w", delete=False, encoding="utf-8") as tmp:
        tmp.write(js_block)
        tmp_path = tmp.name
    try:
        result = subprocess.run(
            ["node", "--check", tmp_path],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            # Clean up temp path from error message
            msg = result.stderr.replace(tmp_path, "index.html <script>")
            errors.append(f"JS syntax error:\n{msg.strip()}")
    finally:
        os.unlink(tmp_path)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--html", default=str(DEFAULT_HTML), help="Path to index.html")
    args = parser.parse_args()

    html_path = Path(args.html)
    if not html_path.exists():
        print(f"❌ File not found: {html_path}", file=sys.stderr)
        sys.exit(1)

    content = html_path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    print(f"Validating {html_path.name} …\n")

    # ── 1. JS syntax ──────────────────────────────────────────────────────────
    print("  [1] JavaScript syntax check …", end=" ", flush=True)
    js_errs = check_js_syntax(html_path)
    if js_errs:
        print("❌")
        errors.extend(js_errs)
    else:
        print("✅")

    # ── 2. _DATA entries ──────────────────────────────────────────────────────
    print("  [2] _DATA payload integrity …", end=" ", flush=True)
    data_entries = find_data_entries(content)
    payload_ok = True
    for key, expected_len in FROZEN_LENGTHS.items():
        if key not in data_entries:
            errors.append(f"_DATA key '{key}' missing")
            payload_ok = False
        else:
            length, closes = data_entries[key]
            if not closes:
                errors.append(f"_DATA['{key}']: missing closing quote (unterminated string)")
                payload_ok = False
            if length != expected_len:
                errors.append(f"_DATA['{key}']: length {length} ≠ expected {expected_len} (frozen payload modified)")
                payload_ok = False
    # Check all entries close correctly
    for key, (length, closes) in data_entries.items():
        if not closes and key not in FROZEN_LENGTHS:
            errors.append(f"_DATA['{key}']: missing closing quote (unterminated string)")
            payload_ok = False
    print("✅" if payload_ok else "❌")

    # ── 3. EXAMS config has entry for every _DATA key ─────────────────────────
    print("  [3] EXAMS config completeness …", end=" ", flush=True)
    exams_block_start = content.find("var EXAMS")
    exams_block_end = content.find("\n};", exams_block_start) + 3
    exams_block = content[exams_block_start:exams_block_end]
    exams_ok = True
    for key in data_entries:
        if f"{key}:" not in exams_block and f'"{key}"' not in exams_block:
            errors.append(f"EXAMS config missing entry for key '{key}'")
            exams_ok = False
    print("✅" if exams_ok else "❌")

    # ── 4. Tab button and panel for every _DATA key ───────────────────────────
    print("  [4] HTML tab buttons and panels …", end=" ", flush=True)
    html_ok = True
    for key in data_entries:
        if f'data-exam="{key}"' not in content:
            errors.append(f"Missing tab button for key '{key}'")
            html_ok = False
        if f'id="panel-{key}"' not in content:
            errors.append(f"Missing panel div for key '{key}'")
            html_ok = False
    print("✅" if html_ok else "❌")

    # ── Report ────────────────────────────────────────────────────────────────
    print(f"\n  Exam keys in _DATA: {sorted(data_entries.keys())}")
    print(f"  Payload lengths:    {', '.join(f'{k}={v[0]}' for k,v in sorted(data_entries.items()))}")

    if errors:
        print(f"\n{'='*60}")
        print(f"❌ VALIDATION FAILED — {len(errors)} error(s):\n")
        for e in errors:
            print(f"  • {e}")
        print(f"{'='*60}")
        sys.exit(1)
    else:
        print(f"\n✅ index.html passes all checks.")
        sys.exit(0)


if __name__ == "__main__":
    main()
