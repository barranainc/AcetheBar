#!/usr/bin/env python3
"""
patch_3c_study_reports.py — Phase 3C: Smart Study Reports, Weak-Area Action Plan,
Exportable Progress Reports. Run from repo root:  python3 tools/patch_3c_study_reports.py
"""
import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT  = os.path.dirname(SCRIPT_DIR)
INDEX_PATH = os.path.join(REPO_ROOT, 'index.html')


def patch(content, old, new, label):
    if old not in content:
        print(f'  [WARN] anchor not found: {label}')
        return content
    result = content.replace(old, new, 1)
    print(f'  [OK]   patched: {label}')
    return result


# ══════════════════════════════════════════════════════════════
# CSS
# ══════════════════════════════════════════════════════════════
STUDY_CSS = """\
/* ── Phase 3C Study Plan ── */
.spl-milestones{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:4px}
.spl-milestone{display:flex;align-items:center;gap:6px;background:var(--bg2,#1a1d2e);border:1px solid var(--border1,#2a2d3e);border-radius:8px;padding:6px 10px;font-size:12px;color:var(--text2,#9ca3af)}
.spl-milestone.done{border-color:#22c55e;background:rgba(34,197,94,.1);color:#22c55e}
.spl-ms-icon{flex-shrink:0}
.spl-ms-lbl{line-height:1.3}
.spl-sub-table{display:flex;flex-direction:column;gap:5px}
.spl-sub-row{display:flex;align-items:center;gap:10px;padding:8px 12px;background:var(--bg2,#1a1d2e);border-radius:8px;border:1px solid var(--border1,#2a2d3e)}
.spl-sub-name{flex:1;font-size:13px;color:var(--text1,#e8eaf0);font-weight:600}
.spl-sub-stats{display:flex;gap:10px;font-size:12px;color:var(--text3,#6b7280)}
.spl-diag-badge{font-size:10px;font-weight:700;padding:3px 8px;border-radius:12px;white-space:nowrap;flex-shrink:0}
.spl-weak-item{background:var(--bg2,#1a1d2e);border:1px solid var(--border1,#2a2d3e);border-radius:8px;padding:12px 14px;margin-bottom:8px}
.spl-weak-hdr{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:5px;flex-wrap:wrap}
.spl-weak-title{font-size:13px;font-weight:700;color:var(--text1,#e8eaf0)}
.spl-weak-meta{font-size:11px;color:var(--text3,#6b7280);margin-bottom:5px}
.spl-weak-action{font-size:12px;color:var(--text2,#9ca3af);margin-bottom:8px;font-style:italic}
.spl-action-btns{display:flex;flex-wrap:wrap;gap:6px}
.spl-prescription{background:rgba(99,102,241,.08);border-left:3px solid var(--accent,#6366f1);border-radius:0 8px 8px 0;padding:12px 16px;font-size:13px;color:var(--text2,#9ca3af)}
.spl-steps{margin:0;padding-left:20px;line-height:2.2}
.spl-steps li{margin-bottom:2px}
.spl-notice{background:rgba(99,102,241,.06);border-left:3px solid var(--border1,#2a2d3e);border-radius:0 8px 8px 0;padding:10px 14px;font-size:12px;color:var(--text3,#6b7280)}
"""

# ══════════════════════════════════════════════════════════════
# HTML
# ══════════════════════════════════════════════════════════════
STUDY_HTML = """\
<!-- Phase 3C: Study Plan -->
<div id="study-plan" class="anl-overlay" style="display:none" onclick="if(event.target===this)splShow(false)">
  <div class="anl-panel">
    <div class="anl-hdr"><h2>🧭 Smart Study Plan</h2><button class="anl-close" onclick="splShow(false)">✕</button></div>
    <div class="anl-body" id="spl-body"><div class="anl-empty">Building report…</div></div>
    <div class="anl-footer">
      <button class="nbtn" onclick="splPrint()">🖨 Print</button>
      <button class="nbtn" onclick="splExportJSON()">⬇ JSON</button>
      <button class="nbtn" onclick="splExportCSV()">⬇ CSV</button>
    </div>
  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════
# JS MODULE
# ══════════════════════════════════════════════════════════════
STUDY_JS = """\
// ============================================================
// PHASE 3C — SMART STUDY REPORTS
// ============================================================
var splActionQueue = [];

// ── Data Aggregation ─────────────────────────────────────────
function splAggregateData() {
  var d = anlLoad();
  var flagged = d.flaggedQuestions || {};
  var subMap = {}, chMap = {};
  var totalUniqueQ = 0, totalAttempts = 0, totalCorrectQ = 0;
  var totalTimeSum = 0, totalTimeCnt = 0, totalRepeatWrong = 0;
  var noChMetaSubjects = {};

  function accum(map, key, sub, ch, hasChMeta,
                 qAttempts, qCorrect, qWrong, qFastWrong, qSlowCorrect,
                 qRepeatWrong, qTimeSum, qTimeCnt, isFlagged) {
    if (!map[key]) {
      map[key] = { sub:sub, ch:ch, hasChMeta:hasChMeta,
        uniqueQ:0, attempts:0, correct:0, wrong:0,
        fastWrong:0, slowCorrect:0, repeatWrong:0,
        timeSum:0, timeCnt:0, flagged:0 };
    }
    var m = map[key];
    m.uniqueQ++;
    m.attempts    += qAttempts;
    m.correct     += qCorrect;
    m.wrong       += qWrong;
    m.fastWrong   += qFastWrong;
    m.slowCorrect += qSlowCorrect;
    m.repeatWrong += qRepeatWrong;
    m.timeSum     += qTimeSum;
    m.timeCnt     += qTimeCnt;
    if (isFlagged) m.flagged++;
  }

  Object.keys(d.attempts).forEach(function(key) {
    var atts = d.attempts[key];
    if (!atts || !atts.length) return;
    var last = atts[atts.length - 1];
    var sub  = last.subject || '(Unknown)';
    var ch   = last.chapterTitle || '';
    var hasChMeta = !!ch;

    var qCorrect = 0, qWrong = 0, qFastWrong = 0, qSlowCorrect = 0;
    var qTimeSum = 0, qTimeCnt = 0;
    atts.forEach(function(a) {
      if (a.isCorrect) {
        qCorrect++;
        if (a.timeSeconds > 120) qSlowCorrect++;
      } else {
        qWrong++;
        if (a.timeSeconds > 0 && a.timeSeconds < 45) qFastWrong++;
      }
      if (a.timeSeconds > 0) { qTimeSum += a.timeSeconds; qTimeCnt++; }
    });
    var qRepeatWrong = (qWrong >= 2 && qCorrect === 0) ? 1 : 0;
    var isFlagged    = !!flagged[key];

    totalUniqueQ++;
    totalAttempts += atts.length;
    if (qCorrect > 0) totalCorrectQ++;
    if (qTimeCnt) { totalTimeSum += qTimeSum; totalTimeCnt += qTimeCnt; }
    if (qRepeatWrong) totalRepeatWrong++;
    if (!hasChMeta) noChMetaSubjects[sub] = true;

    accum(subMap, sub, sub, '', false,
          atts.length, qCorrect, qWrong, qFastWrong, qSlowCorrect,
          qRepeatWrong, qTimeSum, qTimeCnt, isFlagged);
    if (hasChMeta) {
      accum(chMap, sub + '||' + ch, sub, ch, true,
            atts.length, qCorrect, qWrong, qFastWrong, qSlowCorrect,
            qRepeatWrong, qTimeSum, qTimeCnt, isFlagged);
    }
  });

  return {
    subMap: subMap, chMap: chMap,
    totalUniqueQ: totalUniqueQ, totalAttempts: totalAttempts,
    totalCorrectQ: totalCorrectQ,
    totalFlagged: Object.keys(flagged).length,
    totalRepeatWrong: totalRepeatWrong,
    totalAvgTime: totalTimeCnt ? Math.round(totalTimeSum / totalTimeCnt) : 0,
    noChMetaSubjects: noChMetaSubjects
  };
}

// ── Scoring helpers ───────────────────────────────────────────
function splAccPct(m) {
  var total = m.correct + m.wrong;
  return total ? Math.round((m.correct / total) * 100) : null;
}
function splAvgT(m) {
  return m.timeCnt ? Math.round(m.timeSum / m.timeCnt) : 0;
}
function splDiagLabel(acc, avgTime, repeatWrong, fastWrong, wrong) {
  if (acc === null) return 'No Data';
  if (acc >= 80 && avgTime > 0 && avgTime <= 120) return 'Strong';
  if (acc >= 70 && avgTime > 120) return 'Speed Issue';
  if (wrong > 0 && fastWrong > 0 && fastWrong >= Math.ceil(wrong / 2)) return 'Guessing Risk';
  if (acc < 60 && repeatWrong > 0) return 'Knowledge Gap';
  if (acc < 70 && avgTime > 120) return 'Mixed Weakness';
  if (acc < 70) return 'Concept Gap';
  if (acc < 80) return 'Needs Review';
  return 'Strong';
}
function splDiagCol(label) {
  if (label === 'Strong')        return '#22c55e';
  if (label === 'Speed Issue')   return '#f59e0b';
  if (label === 'Needs Review')  return '#f59e0b';
  if (label === 'Guessing Risk') return '#f97316';
  return '#ef4444';  // Knowledge Gap, Concept Gap, Mixed Weakness, No Data
}
function splPriority(m) {
  var acc = splAccPct(m);
  if (acc === null) return 0;
  var s = (1 - acc / 100) * 40;
  s += m.repeatWrong * 10;
  s += m.fastWrong * 8;
  s += (splAvgT(m) > 120 ? 5 : 0);
  s += (m.flagged > 0 ? 3 : 0);
  return Math.round(s);
}
function splChToNum(sub, cht) {
  if (!drillCatalog) return 0;
  for (var i = 0; i < drillCatalog.length; i++) {
    var it = drillCatalog[i];
    if (it.sub === sub && it.cht === cht && it.ch) return it.ch;
  }
  return 0;
}

// ── HTML helpers ─────────────────────────────────────────────
function splEsc(s) {
  if (!s) return '';
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function splStatCard(label, val, color) {
  return '<div class="anl-stat-card">' +
    '<div class="anl-stat-val"' + (color ? ' style="color:' + color + '"' : '') + '>' + val + '</div>' +
    '<div class="anl-stat-lbl">' + label + '</div></div>';
}
function splBadge(label) {
  var col = splDiagCol(label);
  return '<div class="spl-diag-badge" style="background:' + col + '22;color:' + col + ';border:1px solid ' + col + '44">' + label + '</div>';
}
function splMakeBtn(label, opts) {
  var idx = splActionQueue.length;
  splActionQueue.push(opts);
  return '<button class="drl-preset-btn" onclick="splShowFalse();splDrillQueued(' + idx + ')">' + label + '</button>';
}

// ── Report builder ────────────────────────────────────────────
function splBuildReport() {
  splActionQueue = [];
  var data = splAggregateData();
  var TOTAL_Q = 963;
  var pctAtt  = Math.round((data.totalUniqueQ / TOTAL_Q) * 100);
  var totalAcc = data.totalUniqueQ > 0
    ? Math.round((data.totalCorrectQ / data.totalUniqueQ) * 100) : 0;
  var accCol = totalAcc >= 80 ? '#22c55e' : totalAcc >= 70 ? '#f59e0b' : '#ef4444';

  // 1. Overall
  var html = '<div class="anl-sec-hdr">Overall Progress</div>';
  html += '<div class="anl-stats-grid">';
  html += splStatCard('Attempted', data.totalUniqueQ + ' / ' + TOTAL_Q, '');
  html += splStatCard('Coverage',  pctAtt + '%', pctAtt >= 50 ? '#22c55e' : '#f59e0b');
  html += splStatCard('Accuracy',  totalAcc + '%', accCol);
  html += splStatCard('Avg Time',  data.totalAvgTime + 's', '');
  html += splStatCard('Flagged',   data.totalFlagged, data.totalFlagged > 0 ? '#f59e0b' : '');
  html += splStatCard('Repeat Wrong', data.totalRepeatWrong,
    data.totalRepeatWrong > 0 ? '#ef4444' : (data.totalUniqueQ > 0 ? '#22c55e' : ''));
  html += '</div>';

  // 2. Milestones
  var ms = [
    ['25% of questions attempted',  pctAtt >= 25],
    ['50% of questions attempted',  pctAtt >= 50],
    ['75% of questions attempted',  pctAtt >= 75],
    ['100% of questions attempted', pctAtt >= 100],
    ['70%+ overall accuracy',       totalAcc >= 70],
    ['80%+ overall accuracy',       totalAcc >= 80],
    ['Average time under 90s',      data.totalAvgTime > 0 && data.totalAvgTime < 90],
    ['No repeated wrong questions', data.totalRepeatWrong === 0 && data.totalUniqueQ > 0]
  ];
  html += '<div class="anl-sec-hdr">Milestones</div><div class="spl-milestones">';
  for (var mi = 0; mi < ms.length; mi++) {
    html += '<div class="spl-milestone' + (ms[mi][1] ? ' done' : '') + '">' +
      '<span class="spl-ms-icon">' + (ms[mi][1] ? '✅' : '⬜') + '</span>' +
      '<span class="spl-ms-lbl">' + ms[mi][0] + '</span></div>';
  }
  html += '</div>';

  // 3. Subject breakdown
  var subs = Object.keys(data.subMap).sort();
  if (subs.length) {
    html += '<div class="anl-sec-hdr">Subject Breakdown</div><div class="spl-sub-table">';
    for (var si = 0; si < subs.length; si++) {
      var sm = data.subMap[subs[si]];
      var sacc = splAccPct(sm), savg = splAvgT(sm);
      var slbl = splDiagLabel(sacc, savg, sm.repeatWrong, sm.fastWrong, sm.wrong);
      html += '<div class="spl-sub-row">' +
        '<div class="spl-sub-name">' + splEsc(subs[si]) + '</div>' +
        '<div class="spl-sub-stats">' +
          '<span>' + sm.uniqueQ + ' q</span>' +
          '<span>' + (sacc !== null ? sacc + '%' : '—') + '</span>' +
          '<span>' + (savg > 0 ? savg + 's' : '—') + '</span>' +
        '</div>' +
        splBadge(slbl) + '</div>';
    }
    html += '</div>';
  }

  // 4. Weak-area ranking
  var chKeys = Object.keys(data.chMap);
  var ranked = [];
  for (var ci = 0; ci < chKeys.length; ci++) {
    var cm = data.chMap[chKeys[ci]];
    var cp = splPriority(cm);
    if (cp > 5) ranked.push({ m: cm, p: cp });
  }
  ranked.sort(function(a, b) { return b.p - a.p; });

  if (ranked.length) {
    html += '<div class="anl-sec-hdr">Weak-Area Ranking</div>';
    var limit = ranked.length < 10 ? ranked.length : 10;
    for (var ri = 0; ri < limit; ri++) {
      var wm = ranked[ri].m;
      var wacc = splAccPct(wm), wavg = splAvgT(wm);
      var wlbl = splDiagLabel(wacc, wavg, wm.repeatWrong, wm.fastWrong, wm.wrong);
      var chNum = splChToNum(wm.sub, wm.ch);

      var action = '';
      if (wlbl === 'Knowledge Gap' || wlbl === 'Concept Gap') {
        action = 'Review concept material and reattempt wrong answers.';
      } else if (wlbl === 'Guessing Risk') {
        action = 'Slow down — read each question carefully before answering.';
      } else if (wlbl === 'Speed Issue') {
        action = 'Practice for speed — knowledge is solid but pace needs work.';
      } else if (wlbl === 'Mixed Weakness') {
        action = 'Both knowledge and speed need work — start with concept review.';
      } else if (wlbl === 'Needs Review') {
        action = 'Close to passing threshold — a focused drill will consolidate this area.';
      } else {
        action = 'Keep practising to maintain strength.';
      }

      var base = { sub: wm.sub, ch: chNum, top: '', dif: 'all', count: 20, order: 'random' };
      var drillBtn = splMakeBtn('🎯 Drill this area', { sub:wm.sub, ch:chNum, top:'', dif:'all', status:'all', count:20, order:'random' });
      var wrongBtn = splMakeBtn('✗ Wrong answers', { sub:wm.sub, ch:chNum, top:'', dif:'all', status:'wrong', count:40, order:'weakest' });
      var unattBtn = splMakeBtn('○ Unattempted', { sub:wm.sub, ch:chNum, top:'', dif:'all', status:'unattempted', count:20, order:'random' });
      var flagBtn  = wm.flagged > 0 ? splMakeBtn('⚑ Flagged', { sub:wm.sub, ch:chNum, top:'', dif:'all', status:'flagged', count:40, order:'random' }) : '';

      html += '<div class="spl-weak-item">' +
        '<div class="spl-weak-hdr">' +
          '<div class="spl-weak-title">' + splEsc(wm.sub) + (wm.ch ? ' — ' + splEsc(wm.ch) : '') + '</div>' +
          splBadge(wlbl) +
        '</div>' +
        '<div class="spl-weak-meta">' +
          (wacc !== null ? wacc + '% accuracy' : '') +
          (wavg > 0 ? ' · ' + wavg + 's avg' : '') +
          (wm.wrong > 0 ? ' · ' + wm.wrong + ' wrong' : '') +
          (wm.repeatWrong > 0 ? ' · ' + wm.repeatWrong + ' repeat wrong' : '') +
          (wm.fastWrong > 0 ? ' · ' + wm.fastWrong + ' fast wrong' : '') +
        '</div>' +
        '<div class="spl-weak-action">' + splEsc(action) + '</div>' +
        '<div class="spl-action-btns">' + drillBtn + wrongBtn + flagBtn + unattBtn + '</div>' +
        '</div>';
    }
  }

  // 5. Daily prescription
  html += splPrescription(ranked, data);

  // 6. Imported exam notice
  if (Object.keys(data.noChMetaSubjects).length > 0) {
    html += '<div class="anl-sec-hdr">Note</div>' +
      '<div class="spl-notice">Detailed chapter/topic recommendations are available for generated exams and PR drills only. ' +
      'Imported exams (LSO Barrister A/B, LSO Solicitor A, ABP) appear in subject-level stats only.</div>';
  }

  return html;
}

function splPrescription(ranked, data) {
  var steps = [], idx = 1;
  var topN = ranked.length < 3 ? ranked.length : 3;
  for (var i = 0; i < topN; i++) {
    var wm = ranked[i].m;
    var wacc = splAccPct(wm), wavg = splAvgT(wm);
    var wlbl = splDiagLabel(wacc, wavg, wm.repeatWrong, wm.fastWrong, wm.wrong);
    var area = splEsc(wm.sub) + (wm.ch ? ' — ' + splEsc(wm.ch) : '');
    if (wlbl === 'Knowledge Gap' || wlbl === 'Concept Gap' || wlbl === 'Mixed Weakness') {
      steps.push(idx + '. Review <strong>' + area + '</strong> — accuracy is ' + wacc + '%. Focus on understanding the rule, not just the answer.');
      idx++;
      if (wm.wrong > 0) {
        steps.push(idx + '. Run a wrong-answer drill on <strong>' + splEsc(wm.sub) + '</strong> (up to 40 questions, weakest first).');
        idx++;
      }
    } else if (wlbl === 'Guessing Risk') {
      steps.push(idx + '. Slow down on <strong>' + area + '</strong> — ' + wm.fastWrong +
        ' fast wrong answer' + (wm.fastWrong !== 1 ? 's' : '') + ' detected. Spend at least 60 seconds per question.');
      idx++;
    } else if (wlbl === 'Speed Issue') {
      steps.push(idx + '. Practice <strong>' + area + '</strong> for speed — accuracy is ' +
        wacc + '% but averaging ' + wavg + 's per question.');
      idx++;
    } else if (wlbl === 'Needs Review') {
      steps.push(idx + '. Run a 20-question drill on <strong>' + area + '</strong> to push accuracy above 80%.');
      idx++;
    }
  }
  if (data.totalFlagged > 0) {
    steps.push(idx + '. Revisit your <strong>' + data.totalFlagged + ' flagged question' +
      (data.totalFlagged !== 1 ? 's' : '') + '</strong> — use the Flagged preset in Drill Builder.');
    idx++;
  }
  if (data.totalRepeatWrong > 0) {
    steps.push(idx + '. Focus on <strong>' + data.totalRepeatWrong + ' repeatedly wrong question' +
      (data.totalRepeatWrong !== 1 ? 's' : '') + '</strong> — use the Weak Areas preset.');
    idx++;
  }
  var pctAtt = Math.round((data.totalUniqueQ / 963) * 100);
  if (pctAtt < 50) {
    steps.push(idx + '. Expand coverage — only <strong>' + pctAtt + '%</strong> of the question bank attempted. Run Unattempted drills.');
    idx++;
  }

  if (!steps.length) {
    return '<div class="anl-sec-hdr">Today\\'s Study Plan</div>' +
      '<div class="spl-notice">Not enough data yet — answer at least 10 questions to generate a personalised plan.</div>';
  }
  return '<div class="anl-sec-hdr">Today\\'s Study Plan</div>' +
    '<div class="spl-prescription"><ol class="spl-steps">' +
    steps.map(function(s) { return '<li>' + s + '</li>'; }).join('') +
    '</ol></div>';
}

// ── Public API ────────────────────────────────────────────────
function splShow(show) {
  var el = document.getElementById('study-plan');
  if (!el) return;
  if (show) {
    el.style.display = 'flex';
    buildDrillCatalog(function() {
      document.getElementById('spl-body').innerHTML = splBuildReport();
    });
  } else {
    el.style.display = 'none';
  }
}
function splShowFalse() { splShow(false); }

function splDrillQueued(idx) {
  var opts = splActionQueue[idx];
  if (!opts) return;
  drillOpts = opts;
  buildDrillCatalog(function() { drillStart(); });
}

function splPrint() {
  var body = document.getElementById('spl-body');
  if (!body) return;
  var w = window.open('', '_blank', 'width=900,height=700');
  if (!w) { alert('Please allow pop-ups to print the Study Plan.'); return; }
  var printCSS =
    'body{font-family:system-ui,-apple-system,sans-serif;max-width:860px;margin:0 auto;padding:24px;color:#1a1a2e;font-size:14px}' +
    '.anl-sec-hdr{font-size:11px;text-transform:uppercase;letter-spacing:.6px;color:#6b7280;margin:18px 0 8px;font-weight:700;border-bottom:1px solid #e5e7eb;padding-bottom:4px}' +
    '.anl-stats-grid{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:12px}' +
    '.anl-stat-card{background:#f9fafb;border:1px solid #e5e7eb;border-radius:8px;padding:10px 14px;min-width:90px;text-align:center}' +
    '.anl-stat-val{font-size:20px;font-weight:800;margin-bottom:3px}' +
    '.anl-stat-lbl{font-size:10px;color:#6b7280;text-transform:uppercase}' +
    '.spl-milestones{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px}' +
    '.spl-milestone{display:flex;align-items:center;gap:6px;border:1px solid #e5e7eb;border-radius:8px;padding:5px 10px;font-size:12px;color:#6b7280}' +
    '.spl-milestone.done{border-color:#22c55e;background:#f0fdf4;color:#16a34a}' +
    '.spl-sub-table{display:flex;flex-direction:column;gap:5px;margin-bottom:12px}' +
    '.spl-sub-row{display:flex;align-items:center;gap:10px;padding:7px 10px;background:#f9fafb;border:1px solid #e5e7eb;border-radius:6px}' +
    '.spl-sub-name{flex:1;font-weight:600;font-size:13px}' +
    '.spl-sub-stats{display:flex;gap:10px;font-size:12px;color:#6b7280}' +
    '.spl-diag-badge{font-size:10px;font-weight:700;padding:3px 8px;border-radius:12px;border:1px solid #d1d5db;color:#374151}' +
    '.spl-weak-item{border:1px solid #e5e7eb;border-radius:8px;padding:10px 12px;margin-bottom:8px}' +
    '.spl-weak-hdr{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;margin-bottom:5px}' +
    '.spl-weak-title{font-weight:700;font-size:13px}' +
    '.spl-weak-meta{font-size:11px;color:#6b7280;margin-bottom:4px}' +
    '.spl-weak-action{font-size:12px;color:#374151;font-style:italic}' +
    '.spl-action-btns{display:none}' +
    '.spl-prescription{background:#f5f3ff;border-left:3px solid #6366f1;padding:10px 14px;font-size:13px;border-radius:0 6px 6px 0;margin-top:4px}' +
    '.spl-steps{margin:0;padding-left:20px;line-height:2.2}' +
    '.spl-notice{background:#f5f3ff;border-left:3px solid #6366f1;padding:8px 12px;font-size:12px;color:#4b5563;border-radius:0 6px 6px 0}';
  w.document.write('<!DOCTYPE html><html><head><title>Smart Study Plan</title><style>' + printCSS + '</style></head><body>' +
    '<h2 style="margin:0 0 4px">🧭 Smart Study Plan</h2>' +
    '<p style="color:#6b7280;font-size:12px;margin:0 0 16px">Generated ' + new Date().toLocaleDateString() + '</p>' +
    body.innerHTML + '</body></html>');
  w.document.close();
  w.focus();
  w.print();
}

function splExportJSON() {
  var data = splAggregateData();
  var rows = [];
  var chKeys = Object.keys(data.chMap).sort();
  for (var i = 0; i < chKeys.length; i++) {
    var cm = data.chMap[chKeys[i]];
    var acc = splAccPct(cm), avg = splAvgT(cm);
    rows.push({ subject:cm.sub, chapter:cm.ch, attempts:cm.attempts,
      correct:cm.correct, wrong:cm.wrong, accuracy_pct:acc, avg_time_s:avg,
      repeat_wrong:cm.repeatWrong, fast_wrong:cm.fastWrong, slow_correct:cm.slowCorrect,
      flagged:cm.flagged, diagnostic:splDiagLabel(acc,avg,cm.repeatWrong,cm.fastWrong,cm.wrong),
      priority_score:splPriority(cm) });
  }
  var subKeys = Object.keys(data.subMap).sort();
  for (var j = 0; j < subKeys.length; j++) {
    var sm = data.subMap[subKeys[j]];
    if (data.noChMetaSubjects[subKeys[j]]) {
      var sacc = splAccPct(sm), savg = splAvgT(sm);
      rows.push({ subject:sm.sub, chapter:'(imported — no chapter metadata)', attempts:sm.attempts,
        correct:sm.correct, wrong:sm.wrong, accuracy_pct:sacc, avg_time_s:savg,
        repeat_wrong:sm.repeatWrong, fast_wrong:sm.fastWrong, slow_correct:sm.slowCorrect,
        flagged:sm.flagged, diagnostic:splDiagLabel(sacc,savg,sm.repeatWrong,sm.fastWrong,sm.wrong),
        priority_score:splPriority(sm) });
    }
  }
  var content = JSON.stringify({ generated:new Date().toISOString(), total_questions:963, rows:rows }, null, 2);
  splDownload('study_report_' + new Date().toISOString().slice(0,10) + '.json', 'application/json', content);
}

function splExportCSV() {
  var data = splAggregateData();
  var cols = ['subject','chapter','attempts','correct','wrong','accuracy_pct','avg_time_s',
    'repeat_wrong','fast_wrong','slow_correct','flagged','diagnostic','priority_score','recommended_action'];
  var lines = [cols.join(',')];

  function rowFor(m, ch) {
    var acc = splAccPct(m), avg = splAvgT(m);
    var lbl = splDiagLabel(acc, avg, m.repeatWrong, m.fastWrong, m.wrong);
    var act = 'Maintain and monitor';
    if (lbl==='Knowledge Gap'||lbl==='Concept Gap') act='Review concept material and reattempt wrong answers';
    else if (lbl==='Guessing Risk') act='Slow down and read each question carefully';
    else if (lbl==='Speed Issue')   act='Practice for speed — knowledge is solid';
    else if (lbl==='Mixed Weakness') act='Review concepts then run timed drills';
    else if (lbl==='Needs Review')  act='Run a focused review drill';
    return [
      '"' + (m.sub||'').replace(/"/g,'""') + '"',
      '"' + (ch||'').replace(/"/g,'""') + '"',
      m.attempts, m.correct, m.wrong,
      acc !== null ? acc : '',
      avg > 0 ? avg : '',
      m.repeatWrong, m.fastWrong, m.slowCorrect, m.flagged,
      '"' + lbl + '"',
      splPriority(m),
      '"' + act + '"'
    ].join(',');
  }

  var chKeys = Object.keys(data.chMap).sort();
  for (var i = 0; i < chKeys.length; i++) {
    var cm = data.chMap[chKeys[i]];
    lines.push(rowFor(cm, cm.ch));
  }
  var subKeys = Object.keys(data.subMap).sort();
  for (var j = 0; j < subKeys.length; j++) {
    if (data.noChMetaSubjects[subKeys[j]]) {
      lines.push(rowFor(data.subMap[subKeys[j]], '(imported)'));
    }
  }
  splDownload('study_report_' + new Date().toISOString().slice(0,10) + '.csv',
    'text/csv', lines.join('\\r\\n'));
}

function splDownload(filename, mime, content) {
  var a = document.createElement('a');
  a.href = 'data:' + mime + ';charset=utf-8,' + encodeURIComponent(content);
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}

// ── Nav button ────────────────────────────────────────────────
(function() {
  var nav = document.querySelector('.anl-nav-btns') || document.querySelector('.topnav');
  if (!nav) return;
  var btn = document.createElement('button');
  btn.className = 'anl-dash-btn';
  btn.textContent = '🧭 Study Plan';
  btn.onclick = function() { splShow(true); };
  var drillBtn = nav.querySelector('[onclick*="drillBuilderShow"]');
  if (drillBtn) nav.insertBefore(btn, drillBtn);
  else nav.appendChild(btn);
})();

"""

# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════
def main():
    print('=== Phase 3C Study Reports Patch ===')

    if not os.path.exists(INDEX_PATH):
        print(f'ERROR: {INDEX_PATH} not found')
        sys.exit(1)

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f'Read index.html ({len(content):,} bytes)')

    # 1. CSS before </style>
    content = patch(content, '</style>', STUDY_CSS + '</style>', 'study plan CSS')

    # 2. Modal HTML before </body>
    content = patch(content, '</body>', STUDY_HTML + '</body>', 'study plan modal HTML')

    # 3. JS module before buildPanel('bar');
    content = patch(content, "buildPanel('bar');", STUDY_JS + "buildPanel('bar');", 'study plan JS module')

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'\nWrote index.html ({len(content):,} bytes)')
    print('=== Done — Phase 3C study reports injected ===')


if __name__ == '__main__':
    main()
