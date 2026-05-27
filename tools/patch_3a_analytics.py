#!/usr/bin/env python3
"""
patch_3a_analytics.py — Phase 3A: Inject complete analytics system into index.html
Run from repo root or tools/ directory:  python3 tools/patch_3a_analytics.py
"""

import os
import sys
import base64
import json

# ── paths ──────────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT   = os.path.dirname(SCRIPT_DIR)
INDEX_PATH  = os.path.join(REPO_ROOT, 'index.html')
META_PATH   = os.path.join(REPO_ROOT, 'data', 'analytics', 'question_metadata.json')

# ── helpers ────────────────────────────────────────────────────────────────────
def patch(content, old, new, label):
    if old not in content:
        print(f'  [WARN] anchor not found for: {label}')
        return content
    result = content.replace(old, new, 1)
    print(f'  [OK]   patched: {label}')
    return result

# ══════════════════════════════════════════════════════════════════════════════
# CSS
# ══════════════════════════════════════════════════════════════════════════════
ANALYTICS_CSS = """\
/* ── Phase 3A Analytics ── */
.anl-overlay{position:fixed;inset:0;background:rgba(0,0,0,.8);z-index:2000;display:flex;align-items:center;justify-content:center;padding:16px}
.anl-panel{background:var(--bg1,#131520);border:1px solid var(--border1,#2a2d3e);border-radius:12px;width:min(680px,96vw);max-height:88vh;display:flex;flex-direction:column;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.5)}
.anl-hdr{display:flex;align-items:center;justify-content:space-between;padding:14px 20px;border-bottom:1px solid var(--border1,#2a2d3e);flex-shrink:0}
.anl-hdr h2{margin:0;font-size:16px;font-weight:700;color:var(--text1,#e8eaf0)}
.anl-close{background:none;border:none;color:var(--text3,#6b7280);font-size:22px;cursor:pointer;padding:2px 8px;line-height:1;border-radius:4px}
.anl-close:hover{color:var(--text1,#e8eaf0)}
.anl-body{flex:1;overflow-y:auto;padding:18px 20px}
.anl-footer{padding:12px 20px;border-top:1px solid var(--border1,#2a2d3e);display:flex;gap:8px;flex-wrap:wrap;flex-shrink:0}
.anl-stats-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(95px,1fr));gap:8px;margin-bottom:16px}
.anl-stat-card{background:var(--bg2,#1a1d2e);border-radius:8px;padding:12px 8px;text-align:center}
.anl-stat-val{font-size:20px;font-weight:700;color:var(--text1,#e8eaf0)}
.anl-stat-lbl{font-size:10px;color:var(--text3,#6b7280);margin-top:3px;text-transform:uppercase;letter-spacing:.4px}
.anl-sec-hdr{font-size:11px;font-weight:600;color:var(--text3,#6b7280);text-transform:uppercase;letter-spacing:.5px;margin:16px 0 8px}
.anl-bars{display:flex;flex-direction:column;gap:5px}
.anl-bar-row{display:flex;align-items:center;gap:8px}
.anl-bar-lbl{width:90px;font-size:11px;color:var(--text2,#9ca3af);text-align:right;flex-shrink:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.anl-bar-bg{flex:1;background:var(--bg2,#1a1d2e);border-radius:3px;height:10px;overflow:hidden}
.anl-bar-fill{height:100%;border-radius:3px;transition:width .3s}
.anl-bar-pct{font-size:11px;color:var(--text3,#6b7280);width:44px;flex-shrink:0}
.anl-list{display:flex;flex-direction:column;gap:3px}
.anl-list-item{display:flex;justify-content:space-between;align-items:center;padding:6px 10px;background:var(--bg2,#1a1d2e);border-radius:6px;gap:8px}
.anl-list-name{font-size:12px;color:var(--text2,#9ca3af);flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.anl-list-val{font-size:12px;font-weight:600;flex-shrink:0}
.anl-ok{color:#22c55e}
.anl-bad{color:#ef4444}
.anl-empty{color:var(--text3,#6b7280);text-align:center;padding:40px 20px;font-size:14px}
.anl-recs{display:flex;flex-direction:column;gap:5px}
.anl-rec-item{padding:8px 12px;background:rgba(59,130,246,.1);border-left:3px solid #3b82f6;border-radius:0 6px 6px 0;font-size:12px;color:var(--text2,#9ca3af)}
.flag-btn{background:transparent!important;border:1px solid var(--border1,#2a2d3e)!important}
.flag-btn.flagged{background:rgba(245,158,11,.15)!important;border-color:#f59e0b!important;color:#f59e0b!important}
.jb.flagged{outline:2px solid #f59e0b}
.anl-dash-btn{background:var(--bg2,#1a1d2e);border:1px solid var(--border1,#2a2d3e);color:var(--text2,#9ca3af);padding:5px 12px;border-radius:6px;cursor:pointer;font-size:12px;white-space:nowrap;transition:border-color .15s}
.anl-dash-btn:hover{border-color:var(--text2,#9ca3af);color:var(--text1,#e8eaf0)}
.anl-nav-btns{display:flex;align-items:center;gap:8px;padding:0 8px;flex-shrink:0}
.anl-finish-btns{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0}
.anl-status-dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:5px}
"""

# ══════════════════════════════════════════════════════════════════════════════
# MODAL HTML
# ══════════════════════════════════════════════════════════════════════════════
MODAL_HTML = """\
<!-- Analytics Dashboard -->
<div id="anl-dash" class="anl-overlay" style="display:none" onclick="if(event.target===this)anlDashboard(false)">
  <div class="anl-panel">
    <div class="anl-hdr"><h2>📊 Progress Dashboard</h2><button class="anl-close" onclick="anlDashboard(false)">✕</button></div>
    <div class="anl-body" id="anl-dash-body"></div>
    <div class="anl-footer">
      <button class="nbtn" onclick="anlExport()">⬇ Export Progress</button>
      <button class="nbtn" onclick="anlImport()">⬆ Import Progress</button>
      <button class="nbtn danger" onclick="anlReset()">✕ Reset All</button>
    </div>
  </div>
</div>
<!-- Session Report -->
<div id="anl-report" class="anl-overlay" style="display:none" onclick="if(event.target===this)anlReport(null)">
  <div class="anl-panel">
    <div class="anl-hdr"><h2>📋 Session Report</h2><button class="anl-close" onclick="anlReport(null)">✕</button></div>
    <div class="anl-body" id="anl-report-body"></div>
  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════════
# ANALYTICS JS MODULE
# ══════════════════════════════════════════════════════════════════════════════
ANALYTICS_JS = """\
// ============================================================
// PHASE 3A — ANALYTICS MODULE
// ============================================================
var ANALY_KEY = 'acethebar.analytics.v1';
var anlMeta = null;
var anlSess = null;

function anlDefault() {
  return { attempts: {}, sessions: [], flaggedQuestions: {} };
}

function anlLoad() {
  try {
    var raw = localStorage.getItem(ANALY_KEY);
    if (raw) {
      var d = JSON.parse(raw);
      if (!d.attempts) d.attempts = {};
      if (!d.sessions) d.sessions = [];
      if (!d.flaggedQuestions) d.flaggedQuestions = {};
      return d;
    }
  } catch(e) {}
  return anlDefault();
}

function anlSave(d) {
  try { localStorage.setItem(ANALY_KEY, JSON.stringify(d)); } catch(e) {}
}

function anlGetMeta() {
  if (anlMeta) return anlMeta;
  try { anlMeta = JSON.parse(atob(_META)); } catch(e) { anlMeta = {}; }
  return anlMeta;
}

function anlQMeta(examId, seqId) {
  var meta = anlGetMeta();
  if (!meta.examPositions || !meta.questions) return null;
  var pos = meta.examPositions[examId];
  if (!pos) return null;
  var actualId = pos[String(seqId)];
  if (!actualId) return null;
  return meta.questions[actualId] || null;
}

function anlStartSession(examId) {
  anlSess = { id: 'sess_' + Date.now(), examKey: examId, startedAt: new Date().toISOString(), keys: [] };
}

function anlEndSession() {
  if (!anlSess) return;
  var d = anlLoad();
  d.sessions.push({
    id: anlSess.id,
    examKey: anlSess.examKey,
    startedAt: anlSess.startedAt,
    endedAt: new Date().toISOString(),
    keys: anlSess.keys.slice()
  });
  anlSave(d);
}

function anlRecord(examId, q, selectedIdx, timeSec) {
  var d = anlLoad();
  var meta = anlQMeta(examId, q.id);
  var posMap = (anlGetMeta().examPositions || {})[examId] || null;
  var actualId = posMap ? (posMap[String(q.id)] || (examId + ':' + q.id)) : (examId + ':' + q.id);
  var key = examId + ':' + q.id;
  if (!d.attempts[key]) d.attempts[key] = [];
  var attemptNum = d.attempts[key].length;
  var attempt = {
    questionId: actualId,
    examKey: examId,
    examLabel: (EXAMS[examId] && EXAMS[examId].name) ? EXAMS[examId].name : examId,
    subject: q.sec || '',
    chapterNumber: meta ? (meta.ch || '') : '',
    chapterTitle: meta ? (meta.cht || '') : '',
    topicHeading: meta ? (meta.top || '') : '',
    startedAt: new Date(Date.now() - timeSec * 1000).toISOString(),
    answeredAt: new Date().toISOString(),
    timeSeconds: timeSec,
    selectedAnswer: 'ABCD'[selectedIdx] || '',
    correctAnswer: 'ABCD'[q.ans] || '',
    isCorrect: selectedIdx === q.ans,
    difficulty: meta ? (meta.dif || '') : '',
    attemptNumber: attemptNum,
    sessionId: anlSess ? anlSess.id : ''
  };
  d.attempts[key].push(attempt);
  if (anlSess) anlSess.keys.push(key);
  anlSave(d);
}

function anlIsFlagged(examId, seqId) {
  var d = anlLoad();
  return !!d.flaggedQuestions[examId + ':' + seqId];
}

function anlToggleFlag(examId) {
  var s = state[examId];
  if (!s || s.finished) return;
  var seqId = s.qs[s.cur].id;
  var fkey = examId + ':' + seqId;
  var d = anlLoad();
  if (d.flaggedQuestions[fkey]) {
    delete d.flaggedQuestions[fkey];
  } else {
    d.flaggedQuestions[fkey] = true;
  }
  anlSave(d);
  renderQ(examId);
  buildJump(examId);
}

function anlLastStatus(examId, seqId) {
  var d = anlLoad();
  var key = examId + ':' + seqId;
  var arr = d.attempts[key];
  if (!arr || !arr.length) return 'none';
  return arr[arr.length - 1].isCorrect ? 'correct' : 'wrong';
}

// ── Dashboard ────────────────────────────────────────────────
function anlDashboard(show) {
  var el = document.getElementById('anl-dash');
  if (!el) return;
  if (show) {
    el.style.display = 'flex';
    document.getElementById('anl-dash-body').innerHTML = anlBuildDash();
  } else {
    el.style.display = 'none';
  }
}

function anlStat(label, value, color) {
  var col = color ? ' style="color:' + color + '"' : '';
  return '<div class="anl-stat-card"><div class="anl-stat-val"' + col + '>' + value + '</div><div class="anl-stat-lbl">' + label + '</div></div>';
}

function anlBuildDash() {
  var d = anlLoad();
  var allAttempts = [];
  var keys = Object.keys(d.attempts);
  keys.forEach(function(k) { allAttempts = allAttempts.concat(d.attempts[k]); });

  if (!allAttempts.length) {
    return '<div class="anl-empty">No attempts yet. Complete some questions to see your progress.</div>';
  }

  var total = allAttempts.length;
  var correct = allAttempts.filter(function(a) { return a.isCorrect; }).length;
  var wrong = total - correct;
  var acc = total ? Math.round((correct / total) * 100) : 0;
  var avgTime = total ? Math.round(allAttempts.reduce(function(s, a) { return s + (a.timeSeconds || 0); }, 0) / total) : 0;
  var flagCount = Object.keys(d.flaggedQuestions).length;

  var html = '<div class="anl-stats-grid">';
  html += anlStat('Total', total, '');
  html += anlStat('Correct', correct, '#22c55e');
  html += anlStat('Wrong', wrong, '#ef4444');
  html += anlStat('Accuracy', acc + '%', acc >= 70 ? '#22c55e' : acc >= 50 ? '#f59e0b' : '#ef4444');
  html += anlStat('Avg Time', avgTime + 's', '');
  html += anlStat('Flagged', flagCount, '#f59e0b');
  html += '</div>';

  // Subject accuracy bars
  var subMap = {};
  allAttempts.forEach(function(a) {
    var sub = (a.subject || 'Unknown').split(' ')[0];
    if (!subMap[sub]) subMap[sub] = { ok: 0, total: 0 };
    subMap[sub].total++;
    if (a.isCorrect) subMap[sub].ok++;
  });
  var subs = Object.keys(subMap);
  if (subs.length) {
    html += '<div class="anl-sec-hdr">Subject Accuracy</div><div class="anl-bars">';
    subs.sort().forEach(function(sub) {
      var m = subMap[sub];
      var pct = Math.round((m.ok / m.total) * 100);
      var col = pct >= 70 ? '#22c55e' : pct >= 50 ? '#f59e0b' : '#ef4444';
      html += '<div class="anl-bar-row">' +
        '<div class="anl-bar-lbl">' + sub + '</div>' +
        '<div class="anl-bar-bg"><div class="anl-bar-fill" style="width:' + pct + '%;background:' + col + '"></div></div>' +
        '<div class="anl-bar-pct">' + pct + '% (' + m.total + ')</div>' +
        '</div>';
    });
    html += '</div>';
  }

  // Chapter accuracy (lowest %, >= 2 attempts, < 70%)
  var chMap = {};
  allAttempts.forEach(function(a) {
    var ch = a.chapterTitle || a.chapterNumber || '';
    if (!ch) return;
    if (!chMap[ch]) chMap[ch] = { ok: 0, total: 0 };
    chMap[ch].total++;
    if (a.isCorrect) chMap[ch].ok++;
  });
  var weakChs = Object.keys(chMap).filter(function(ch) {
    var m = chMap[ch];
    return m.total >= 2 && Math.round((m.ok / m.total) * 100) < 70;
  });
  weakChs.sort(function(a, b) {
    return (chMap[a].ok / chMap[a].total) - (chMap[b].ok / chMap[b].total);
  });
  if (weakChs.length) {
    html += '<div class="anl-sec-hdr">Weak Chapters (below 70%)</div><div class="anl-list">';
    weakChs.slice(0, 8).forEach(function(ch) {
      var m = chMap[ch];
      var pct = Math.round((m.ok / m.total) * 100);
      html += '<div class="anl-list-item">' +
        '<div class="anl-list-name">' + ch + '</div>' +
        '<div class="anl-list-val anl-bad">' + pct + '%</div>' +
        '</div>';
    });
    html += '</div>';
  }

  // Slow areas (avg > 110s, >= 2 attempts)
  var slowSubs = Object.keys(subMap).filter(function(sub) {
    var arr = allAttempts.filter(function(a) { return (a.subject || '').split(' ')[0] === sub; });
    var avg = arr.reduce(function(s, a) { return s + (a.timeSeconds || 0); }, 0) / arr.length;
    return arr.length >= 2 && avg > 110;
  });
  if (slowSubs.length) {
    html += '<div class="anl-sec-hdr">Slow Areas (avg &gt; 110s)</div><div class="anl-list">';
    slowSubs.forEach(function(sub) {
      var arr = allAttempts.filter(function(a) { return (a.subject || '').split(' ')[0] === sub; });
      var avg = Math.round(arr.reduce(function(s, a) { return s + (a.timeSeconds || 0); }, 0) / arr.length);
      html += '<div class="anl-list-item">' +
        '<div class="anl-list-name">' + sub + '</div>' +
        '<div class="anl-list-val" style="color:#f59e0b">' + avg + 's avg</div>' +
        '</div>';
    });
    html += '</div>';
  }

  // Repeatedly wrong (all attempts wrong, >= 2)
  var repeatWrong = keys.filter(function(k) {
    var arr = d.attempts[k];
    return arr.length >= 2 && arr.every(function(a) { return !a.isCorrect; });
  });
  if (repeatWrong.length) {
    html += '<div class="anl-sec-hdr">Repeatedly Wrong (' + repeatWrong.length + ' questions)</div><div class="anl-list">';
    repeatWrong.slice(0, 10).forEach(function(k) {
      var arr = d.attempts[k];
      var last = arr[arr.length - 1];
      html += '<div class="anl-list-item">' +
        '<div class="anl-list-name">' + (last.examKey || '') + ' Q' + k.split(':')[1] + ' — ' + (last.subject || '') + '</div>' +
        '<div class="anl-list-val anl-bad">' + arr.length + '× wrong</div>' +
        '</div>';
    });
    html += '</div>';
  }

  return html;
}

// ── Session Report ───────────────────────────────────────────
function anlReport(examId) {
  var el = document.getElementById('anl-report');
  if (!el) return;
  if (!examId) {
    el.style.display = 'none';
    return;
  }
  el.style.display = 'flex';
  document.getElementById('anl-report-body').innerHTML = anlBuildReport(examId);
}

function anlBuildReport(examId) {
  var d = anlLoad();
  var attempts = [];

  if (anlSess && anlSess.examKey === examId && anlSess.keys.length) {
    // Use session keys
    var seen = {};
    anlSess.keys.forEach(function(k) {
      if (seen[k]) return;
      seen[k] = true;
      var arr = d.attempts[k];
      if (arr && arr.length) attempts.push(arr[arr.length - 1]);
    });
  } else {
    // All attempts for this exam
    Object.keys(d.attempts).forEach(function(k) {
      if (k.indexOf(examId + ':') === 0) {
        var arr = d.attempts[k];
        if (arr && arr.length) attempts = attempts.concat(arr);
      }
    });
  }

  if (!attempts.length) {
    return '<div class="anl-empty">No attempts recorded for this exam yet.</div>';
  }

  var total = attempts.length;
  var correct = attempts.filter(function(a) { return a.isCorrect; }).length;
  var wrong = total - correct;
  var acc = total ? Math.round((correct / total) * 100) : 0;
  var avgTime = total ? Math.round(attempts.reduce(function(s, a) { return s + (a.timeSeconds || 0); }, 0) / total) : 0;

  var html = '<div class="anl-stats-grid">';
  html += anlStat('Attempted', total, '');
  html += anlStat('Correct', correct, '#22c55e');
  html += anlStat('Wrong', wrong, '#ef4444');
  html += anlStat('Accuracy', acc + '%', acc >= 70 ? '#22c55e' : acc >= 50 ? '#f59e0b' : '#ef4444');
  html += anlStat('Avg Time', avgTime + 's', '');
  html += '</div>';

  // Subject accuracy bars
  var subMap = {};
  attempts.forEach(function(a) {
    var sub = (a.subject || 'Unknown').split(' ')[0];
    if (!subMap[sub]) subMap[sub] = { ok: 0, total: 0 };
    subMap[sub].total++;
    if (a.isCorrect) subMap[sub].ok++;
  });
  var subs = Object.keys(subMap);
  if (subs.length) {
    html += '<div class="anl-sec-hdr">Subject Accuracy</div><div class="anl-bars">';
    subs.sort().forEach(function(sub) {
      var m = subMap[sub];
      var pct = Math.round((m.ok / m.total) * 100);
      var col = pct >= 70 ? '#22c55e' : pct >= 50 ? '#f59e0b' : '#ef4444';
      html += '<div class="anl-bar-row">' +
        '<div class="anl-bar-lbl">' + sub + '</div>' +
        '<div class="anl-bar-bg"><div class="anl-bar-fill" style="width:' + pct + '%;background:' + col + '"></div></div>' +
        '<div class="anl-bar-pct">' + pct + '% (' + m.total + ')</div>' +
        '</div>';
    });
    html += '</div>';
  }

  // Slowest 5
  var sorted = attempts.slice().sort(function(a, b) { return (b.timeSeconds || 0) - (a.timeSeconds || 0); });
  html += '<div class="anl-sec-hdr">Slowest Questions</div><div class="anl-list">';
  sorted.slice(0, 5).forEach(function(a) {
    html += '<div class="anl-list-item">' +
      '<div class="anl-list-name">' + (a.subject || '') + ' — ' + (a.answeredAt ? a.answeredAt.substring(0, 10) : '') + '</div>' +
      '<div class="anl-list-val" style="color:#f59e0b">' + (a.timeSeconds || 0) + 's</div>' +
      '</div>';
  });
  html += '</div>';

  // Fast wrong (< 45s and wrong)
  var fastWrong = attempts.filter(function(a) { return !a.isCorrect && (a.timeSeconds || 0) < 45; });
  if (fastWrong.length) {
    html += '<div class="anl-sec-hdr">Likely Guessing (wrong in &lt;45s) — ' + fastWrong.length + ' questions</div>';
    html += '<div class="anl-list">';
    fastWrong.slice(0, 5).forEach(function(a) {
      html += '<div class="anl-list-item">' +
        '<div class="anl-list-name">' + (a.subject || '') + '</div>' +
        '<div class="anl-list-val anl-bad">' + (a.timeSeconds || 0) + 's</div>' +
        '</div>';
    });
    html += '</div>';
  }

  // Recommendations
  var recs = [];
  subs.forEach(function(sub) {
    var m = subMap[sub];
    var pct = Math.round((m.ok / m.total) * 100);
    if (pct < 70) recs.push('Review ' + sub + ' material (' + pct + '% accuracy)');
  });
  if (avgTime > 110) recs.push('Practice navigation speed — average answer time is ' + avgTime + 's');
  if (fastWrong.length >= 3) recs.push('Avoid guessing — ' + fastWrong.length + ' quick wrong answers detected');
  // Topic recs
  var topMap = {};
  attempts.forEach(function(a) {
    var top = a.topicHeading || '';
    if (!top) return;
    if (!topMap[top]) topMap[top] = { ok: 0, total: 0 };
    topMap[top].total++;
    if (a.isCorrect) topMap[top].ok++;
  });
  Object.keys(topMap).forEach(function(top) {
    var m = topMap[top];
    if (m.total >= 2 && Math.round((m.ok / m.total) * 100) < 70) {
      recs.push('Focus on topic: ' + top + ' (' + Math.round((m.ok / m.total) * 100) + '%)');
    }
  });

  if (recs.length) {
    html += '<div class="anl-sec-hdr">Recommendations</div><div class="anl-recs">';
    recs.forEach(function(r) { html += '<div class="anl-rec-item">' + r + '</div>'; });
    html += '</div>';
  }

  return html;
}

// ── Review Modes ─────────────────────────────────────────────
function anlReviewWrong(examId) {
  var d = anlLoad();
  var s = state[examId];
  if (!s) return;
  var wrongIdxs = [];
  s.qs.forEach(function(q, i) {
    var key = examId + ':' + q.id;
    var arr = d.attempts[key];
    if (arr && arr.length && !arr[arr.length - 1].isCorrect) wrongIdxs.push(i);
  });
  if (!wrongIdxs.length) { alert('No wrong answers to review!'); return; }
  restartExam(examId);
  // After restart, filter to wrong questions
  setTimeout(function() {
    var s2 = state[examId];
    if (!s2) return;
    s2.filteredIdx = wrongIdxs;
    s2.cur = wrongIdxs[0];
    renderQ(examId);
    buildJump(examId);
  }, 100);
}

function anlReviewFlagged(examId) {
  var d = anlLoad();
  var s = state[examId];
  if (!s) return;
  var flaggedIdxs = [];
  s.qs.forEach(function(q, i) {
    if (d.flaggedQuestions[examId + ':' + q.id]) flaggedIdxs.push(i);
  });
  if (!flaggedIdxs.length) { alert('No flagged questions to review!'); return; }
  restartExam(examId);
  setTimeout(function() {
    var s2 = state[examId];
    if (!s2) return;
    s2.filteredIdx = flaggedIdxs;
    s2.cur = flaggedIdxs[0];
    renderQ(examId);
    buildJump(examId);
  }, 100);
}

// ── Import / Export / Reset ──────────────────────────────────
function anlExport() {
  var d = anlLoad();
  var json = JSON.stringify(d, null, 2);
  var blob = new Blob([json], { type: 'application/json' });
  var url = URL.createObjectURL(blob);
  var a = document.createElement('a');
  a.href = url;
  a.download = 'acethebar-progress-' + new Date().toISOString().substring(0, 10) + '.json';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function anlImport() {
  var inp = document.createElement('input');
  inp.type = 'file';
  inp.accept = '.json,application/json';
  inp.onchange = function() {
    var file = inp.files[0];
    if (!file) return;
    var reader = new FileReader();
    reader.onload = function(e) {
      try {
        var data = JSON.parse(e.target.result);
        if (!data.attempts) throw new Error('Invalid format');
        anlSave(data);
        anlDashboard(true);
      } catch(err) {
        alert('Import failed: invalid file format.');
      }
    };
    reader.readAsText(file);
  };
  document.body.appendChild(inp);
  inp.click();
  document.body.removeChild(inp);
}

function anlReset() {
  if (!confirm('Reset ALL progress data? This cannot be undone.')) return;
  localStorage.removeItem(ANALY_KEY);
  anlDashboard(true);
}

// ── Visibility change — accumulate time when tab hidden ──────
document.addEventListener('visibilitychange', function() {
  if (!activeExam) return;
  var s = state[activeExam];
  if (!s || !s.started || s.paused || s.finished) return;
  if (document.hidden) {
    if (s.qStarts[s.cur]) {
      s.qTimes[s.cur] += Math.round((Date.now() - s.qStarts[s.cur]) / 1000);
      s.qStarts[s.cur] = 0;
    }
  } else {
    s.qStarts[s.cur] = Date.now();
  }
});

"""

# ══════════════════════════════════════════════════════════════════════════════
# INIT SNIPPET (appended after buildPanel('bar');)
# ══════════════════════════════════════════════════════════════════════════════
INIT_JS = """\
// Add analytics nav button
(function(){
  var nav = document.querySelector('.topnav');
  if (nav) {
    var btn = document.createElement('div');
    btn.className = 'anl-nav-btns';
    btn.innerHTML = '<button class="anl-dash-btn" onclick="anlDashboard(true)">📊 Progress</button>';
    nav.appendChild(btn);
  }
})();
"""

# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════
def main():
    print('=== Phase 3A Analytics Patch ===')

    # ── read files ────────────────────────────────────────────────────────────
    if not os.path.exists(INDEX_PATH):
        print(f'ERROR: {INDEX_PATH} not found')
        sys.exit(1)
    if not os.path.exists(META_PATH):
        print(f'ERROR: {META_PATH} not found')
        sys.exit(1)

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f'Read index.html ({len(content):,} bytes)')

    with open(META_PATH, 'rb') as f:
        meta_b64 = base64.b64encode(f.read()).decode('ascii')
    print(f'Read question_metadata.json → {len(meta_b64):,} chars base64')

    # ── 1. CSS ────────────────────────────────────────────────────────────────
    content = patch(
        content,
        '</style>',
        ANALYTICS_CSS + '</style>',
        'analytics CSS before </style>'
    )

    # ── 2. _META variable after _DATA closing }; ──────────────────────────────
    meta_js = 'var _META = "' + meta_b64 + '";\n'
    content = patch(
        content,
        '};\n\nvar EXAMS',
        '};\n\n' + meta_js + '\nvar EXAMS',
        '_META variable after _DATA'
    )

    # ── 3. patch pick() — record attempt after answer ─────────────────────────
    content = patch(
        content,
        's.answers[s.cur] = idx;\n  renderQ(examId);\n}',
        's.answers[s.cur] = idx;\n  anlRecord(examId, s.qs[s.cur], idx, s.qTimes[s.cur]);\n  renderQ(examId);\n}',
        'pick(): record attempt'
    )

    # ── 4. patch buildJump() — flag indicator on jump buttons ─────────────────
    content = patch(
        content,
        'b.className=cls2; b.textContent=s.qs[i].id;',
        'if (anlIsFlagged(examId, s.qs[i].id)) cls2+=\' flagged\';\n    b.className=cls2; b.textContent=s.qs[i].id;',
        'buildJump(): flagged class'
    )

    # ── 5. patch startExam() — start session ──────────────────────────────────
    content = patch(
        content,
        's.started = true;\n  s.paused = false;',
        's.started = true;\n  s.paused = false;\n  anlStartSession(examId);',
        'startExam(): start session'
    )

    # ── 6. patch finishExam() — end session ───────────────────────────────────
    content = patch(
        content,
        '  s.finished=true;\n  if(s.timerID) clearInterval(s.timerID);',
        '  anlEndSession();\n  s.finished=true;\n  if(s.timerID) clearInterval(s.timerID);',
        'finishExam(): end session'
    )

    # ── 7. patch finishExam() forEach — insert finish buttons after ───────────
    finish_btns = (
        "  var anlFinishBtns = '<div class=\"anl-finish-btns\">" +
        "<button class=\"nbtn\" onclick=\"anlReport(\\'" + "'+examId+'\\')\">" +
        "📋 Session Report</button>" +
        "<button class=\"nbtn\" onclick=\"anlReviewWrong(\\'" + "'+examId+'\\')\">" +
        "🔁 Review Wrong</button>" +
        "<button class=\"nbtn\" onclick=\"anlReviewFlagged(\\'" + "'+examId+'\\')\">" +
        "⚑ Review Flagged</button>" +
        "</div>';\n" +
        "  rg.insertAdjacentHTML('afterend', anlFinishBtns);\n"
    )
    content = patch(
        content,
        'rl.appendChild(div);\n  });\n}',
        'rl.appendChild(div);\n  });\n' + finish_btns + '}',
        'finishExam(): finish buttons after forEach'
    )

    # ── 8. patch renderQ() — update flag button state ─────────────────────────
    content = patch(
        content,
        'updStats(examId);\n  buildJump(examId);',
        'updStats(examId);\n  buildJump(examId);\n'
        '  var fb = document.getElementById(\'flagbtn-\'+examId);\n'
        '  if(fb){ if(anlIsFlagged(examId, q.id)){fb.textContent=\'⚑ Flagged\';fb.classList.add(\'flagged\');}else{fb.textContent=\'⚑ Flag\';fb.classList.remove(\'flagged\');} }',
        'renderQ(): update flag button state'
    )

    # ── 9. patch buildPanel() — add Flag button before Finish button ──────────
    content = patch(
        content,
        '\'<button class="nbtn danger" onclick="finishExam(\\\'\'+examId+\'\\\')">Finish & Review</button>\'',
        '\'<button class="nbtn flag-btn" id="flagbtn-\'+examId+\'" onclick="anlToggleFlag(\\\'\'+examId+\'\\\')">⚑ Flag</button>\' +\n            \'<button class="nbtn danger" onclick="finishExam(\\\'\'+examId+\'\\\')">Finish & Review</button>\'',
        'buildPanel(): Flag button before Finish'
    )

    # ── 10. Modal HTML before </body> ─────────────────────────────────────────
    content = patch(
        content,
        '</body>',
        MODAL_HTML + '</body>',
        'modal HTML before </body>'
    )

    # ── 11. Analytics JS + Init before </script> (before buildPanel('bar');) ──
    content = patch(
        content,
        "buildPanel('bar');",
        ANALYTICS_JS + "buildPanel('bar');\n" + INIT_JS,
        'analytics JS module + init snippet'
    )

    # ── write out ─────────────────────────────────────────────────────────────
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'\nWrote index.html ({len(content):,} bytes)')
    print('=== Done — Phase 3A analytics injected ===')


if __name__ == '__main__':
    main()
