#!/usr/bin/env python3
"""
patch_3b_drill.py — Phase 3B: Inject Drill Builder system into index.html
Run from repo root or tools/ directory:  python3 tools/patch_3b_drill.py

Injects:
  1. Drill CSS
  2. anlRecord improvements (canonId, drill metadata fallbacks)
  3. Drill modal HTML (builder, session, report)
  4. Drill JS module
  5. Nav button IIFE
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
DRILL_CSS = """\
/* ── Phase 3B Drill ── */
.drl-overlay{position:fixed;inset:0;background:rgba(0,0,0,.88);z-index:3000;display:flex;align-items:center;justify-content:center;padding:12px;overflow-y:auto}
.drl-panel{background:var(--bg1,#131520);border:1px solid var(--border1,#2a2d3e);border-radius:12px;width:min(740px,96vw);max-height:90vh;display:flex;flex-direction:column;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.6)}
.drl-presets{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:4px}
.drl-preset-btn{background:var(--bg2,#1a1d2e);border:1px solid var(--border1,#2a2d3e);color:var(--text2,#9ca3af);padding:6px 12px;border-radius:8px;cursor:pointer;font-size:12px;transition:border-color .15s,color .15s}
.drl-preset-btn:hover{border-color:var(--accent,#6366f1);color:var(--text1,#e8eaf0)}
.drl-filters{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:12px 0 8px}
.drl-filter-row{display:flex;flex-direction:column;gap:3px}
.drl-filter-row label{font-size:10px;color:var(--text3,#6b7280);text-transform:uppercase;letter-spacing:.4px}
.drl-filter-row select{background:var(--bg2,#1a1d2e);border:1px solid var(--border1,#2a2d3e);color:var(--text1,#e8eaf0);padding:6px 8px;border-radius:6px;font-size:12px;cursor:pointer}
.drl-filter-row select:focus{outline:none;border-color:var(--accent,#6366f1)}
.drl-preview{background:var(--bg2,#1a1d2e);border-radius:8px;padding:9px 12px;font-size:12px;color:var(--text2,#9ca3af);margin-top:4px}
.drl-preview strong{color:var(--text1,#e8eaf0)}
/* Drill session full-screen */
.drl-session{position:fixed;inset:0;background:var(--bg0,#0d0f1a);z-index:3500;display:flex;flex-direction:column;overflow:hidden}
.drl-s-hdr{display:flex;align-items:center;justify-content:space-between;padding:10px 14px;border-bottom:1px solid var(--border1,#2a2d3e);flex-shrink:0;gap:8px;flex-wrap:wrap}
.drl-s-name{font-size:13px;font-weight:600;color:var(--text2,#9ca3af);flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.drl-s-stats{display:flex;align-items:center;gap:8px;flex-shrink:0;font-size:12px;flex-wrap:wrap}
.drl-s-timer{font-size:13px;font-weight:700;color:var(--text1,#e8eaf0);min-width:44px}
.drl-s-body{flex:1;overflow-y:auto;padding:18px 22px;display:flex;flex-direction:column;gap:14px}
.drl-q-text{font-size:15px;line-height:1.7;color:var(--text1,#e8eaf0);white-space:pre-wrap}
.drl-opts{display:flex;flex-direction:column;gap:8px}
.drl-opt{display:flex;align-items:flex-start;gap:10px;padding:10px 14px;background:var(--bg2,#1a1d2e);border:1px solid var(--border1,#2a2d3e);border-radius:8px;cursor:pointer;text-align:left;font-size:14px;color:var(--text1,#e8eaf0);transition:border-color .12s;width:100%}
.drl-opt:hover:not(:disabled){border-color:var(--accent,#6366f1)}
.drl-opt.correct{border-color:#22c55e!important;background:rgba(34,197,94,.1)}
.drl-opt.wrong{border-color:#ef4444!important;background:rgba(239,68,68,.1)}
.drl-opt-lbl{font-weight:700;flex-shrink:0;width:18px;color:var(--text3,#6b7280)}
.drl-expl{background:rgba(99,102,241,.08);border-left:3px solid var(--accent,#6366f1);border-radius:0 8px 8px 0;padding:12px 16px;font-size:13px;color:var(--text2,#9ca3af);line-height:1.6;white-space:pre-wrap}
.drl-ref{font-size:11px;color:var(--text3,#6b7280);margin-top:6px}
.drl-s-foot{padding:10px 14px;border-top:1px solid var(--border1,#2a2d3e);display:flex;align-items:center;gap:8px;flex-shrink:0;flex-wrap:wrap}
.drl-jump-wrap{padding:6px 14px 8px;border-top:1px solid var(--border1,#2a2d3e);overflow-x:auto;flex-shrink:0;display:flex;flex-wrap:wrap;gap:4px;max-height:90px;overflow-y:auto}
.drl-jb{width:30px;height:30px;border-radius:4px;border:1px solid var(--border1,#2a2d3e);background:var(--bg2,#1a1d2e);color:var(--text3,#6b7280);font-size:10px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.drl-jb.cur{border-color:var(--accent,#6366f1);color:var(--accent,#6366f1)}
.drl-jb.good{background:rgba(34,197,94,.15);border-color:#22c55e;color:#22c55e}
.drl-jb.bad{background:rgba(239,68,68,.15);border-color:#ef4444;color:#ef4444}
.drl-jb.flagged{outline:2px solid #f59e0b;outline-offset:1px}
"""

# ══════════════════════════════════════════════════════════════
# HTML
# ══════════════════════════════════════════════════════════════
DRILL_HTML = """\
<!-- Phase 3B: Drill Builder -->
<div id="drill-builder" class="drl-overlay" style="display:none" onclick="if(event.target===this)drillBuilderShow(false)">
  <div class="drl-panel">
    <div class="anl-hdr"><h2>🎯 Drill Builder</h2><button class="anl-close" onclick="drillBuilderShow(false)">✕</button></div>
    <div class="anl-body" id="drl-builder-body"><div class="anl-empty">Loading questions…</div></div>
    <div class="anl-footer"><button class="nbtn" style="flex:1" onclick="drillStart()">▶ Start Drill</button></div>
  </div>
</div>
<!-- Phase 3B: Drill Session -->
<div id="drill-session" class="drl-session" style="display:none">
  <div class="drl-s-hdr">
    <span class="drl-s-name" id="drl-s-name">Drill</span>
    <div class="drl-s-stats">
      <span id="drl-sc" style="color:var(--text3,#6b7280)"></span>
      <span class="drl-s-timer" id="drl-timer">0:00</span>
      <button class="anl-dash-btn" onclick="drillBuilderShow(true)">🎯 Builder</button>
      <button class="nbtn flag-btn" id="drl-flag-btn" onclick="drillToggleFlag()">⚑ Flag</button>
      <button class="nbtn danger" onclick="drillFinish()">Finish Drill</button>
    </div>
  </div>
  <div class="drl-s-body" id="drl-s-body"></div>
  <div class="drl-s-foot">
    <button class="nbtn" onclick="drillNav(-1)">◀ Prev</button>
    <button class="nbtn" onclick="drillNav(1)">Next ▶</button>
  </div>
  <div class="drl-jump-wrap" id="drl-jump"></div>
</div>
<!-- Phase 3B: Drill Report -->
<div id="drill-report" class="anl-overlay" style="display:none" onclick="if(event.target===this)drillReportShow(false)">
  <div class="anl-panel">
    <div class="anl-hdr"><h2>🎯 Drill Report</h2><button class="anl-close" onclick="drillReportShow(false)">✕</button></div>
    <div class="anl-body" id="drl-report-body"></div>
    <div class="anl-footer">
      <button class="nbtn" onclick="drillBuilderShow(true);drillReportShow(false)">🎯 New Drill</button>
      <button class="nbtn" onclick="anlDashboard(true);drillReportShow(false)">📊 Dashboard</button>
    </div>
  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════
# JS MODULE
# ══════════════════════════════════════════════════════════════
DRILL_JS = """\
// ============================================================
// PHASE 3B — DRILL BUILDER MODULE
// ============================================================
var drillCatalog = null;  // built lazily
var drillSess    = null;  // active drill session state
var drillOpts    = { sub:'', ch:0, top:'', dif:'all', status:'all', count:20, order:'random' };

// ── Catalog ─────────────────────────────────────────────────
function buildDrillCatalog(cb) {
  if (drillCatalog) { if (cb) cb(); return; }
  var body = document.getElementById('drl-builder-body');
  if (body) body.innerHTML = '<div class="anl-empty">Building question catalog…</div>';
  setTimeout(function() {
    drillCatalog = [];
    var meta = anlGetMeta();
    var seen = {};
    var KEYS = ['barc','bard','bare','barf','prb200','prdra','prdrb'];
    KEYS.forEach(function(examKey) {
      var raw = _DATA[examKey];
      if (!raw) return;
      var qs;
      try { qs = JSON.parse(atob(raw)); } catch(e) { return; }
      var posMap = (meta.examPositions || {})[examKey] || null;
      qs.forEach(function(q) {
        var canonId = posMap ? (posMap[String(q.id)] || null) : null;
        if (!canonId || seen[canonId]) return;
        seen[canonId] = true;
        var qm = (meta.questions && meta.questions[canonId]) || {};
        drillCatalog.push({
          canonId: canonId,
          sourceExamKey: examKey,
          sourceSeqId: q.id,
          q: q,
          sub: q.sec || qm.sub || '',
          ch: qm.ch || 0,
          cht: qm.cht || '',
          top: qm.top || '',
          dif: qm.dif || '',
          ref: qm.ref || ''
        });
      });
    });
    if (cb) cb();
  }, 10);
}

function drillCatUniq(field, pred) {
  var cat = drillCatalog || [];
  var seen = {}, vals = [];
  for (var i = 0; i < cat.length; i++) {
    var item = cat[i];
    if (pred && !pred(item)) continue;
    var v = item[field];
    if (v !== undefined && v !== '' && v !== 0 && !seen[String(v)]) {
      seen[String(v)] = true;
      vals.push(v);
    }
  }
  if (field === 'ch') vals.sort(function(a,b){return a-b;});
  else vals.sort();
  return vals;
}

function drillCatFindCht(chNum) {
  var cat = drillCatalog || [];
  for (var i = 0; i < cat.length; i++) {
    if (cat[i].ch === chNum) return cat[i].cht;
  }
  return 'Chapter ' + chNum;
}

// ── Filter + Sort ────────────────────────────────────────────
function drillFilterItems(opts) {
  var cat = drillCatalog || [];
  var d = anlLoad();
  var out = [];
  for (var i = 0; i < cat.length; i++) {
    var item = cat[i];
    if (opts.sub && item.sub !== opts.sub) continue;
    if (opts.ch  && item.ch  !== opts.ch)  continue;
    if (opts.top && item.top !== opts.top) continue;
    if (opts.dif && opts.dif !== 'all' && item.dif !== opts.dif) continue;
    var key = item.sourceExamKey + ':' + item.sourceSeqId;
    var atts = d.attempts[key] || [];
    var last = atts.length ? atts[atts.length - 1] : null;
    var status = opts.status;
    if (status === 'unattempted'  && atts.length > 0) continue;
    if (status === 'attempted'    && atts.length === 0) continue;
    if (status === 'wrong'        && (!last || last.isCorrect)) continue;
    if (status === 'correct'      && (!last || !last.isCorrect)) continue;
    if (status === 'repeat_wrong') {
      var allWrong = atts.length >= 2;
      if (allWrong) { for (var j=0;j<atts.length;j++){if(atts[j].isCorrect){allWrong=false;break;}} }
      if (!allWrong) continue;
    }
    if (status === 'flagged'   && !d.flaggedQuestions[key]) continue;
    if (status === 'slow'      && (!last || !last.isCorrect || last.timeSeconds <= 120)) continue;
    if (status === 'fast_wrong'&& (!last || last.isCorrect || last.timeSeconds >= 45)) continue;
    out.push(item);
  }
  return out;
}

function drillSortItems(items, order) {
  var d = anlLoad();
  if (order === 'random') {
    for (var i = items.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = items[i]; items[i] = items[j]; items[j] = tmp;
    }
  } else if (order === 'weakest') {
    items.sort(function(a, b) {
      function acc(it) {
        var arr = d.attempts[it.sourceExamKey+':'+it.sourceSeqId]||[];
        if(!arr.length) return 0.5;
        var ok=0; for(var k=0;k<arr.length;k++){if(arr[k].isCorrect)ok++;}
        return ok/arr.length;
      }
      return acc(a) - acc(b);
    });
  } else if (order === 'slowest') {
    items.sort(function(a, b) {
      function lt(it) {
        var arr=d.attempts[it.sourceExamKey+':'+it.sourceSeqId]||[];
        return arr.length ? arr[arr.length-1].timeSeconds : 0;
      }
      return lt(b) - lt(a);
    });
  }
  // 'original' — no sort
  return items;
}

// ── Builder UI ───────────────────────────────────────────────
function drillBuilderShow(show) {
  var el = document.getElementById('drill-builder');
  if (!el) return;
  if (show) {
    el.style.display = 'flex';
    buildDrillCatalog(drillBuilderRender);
  } else {
    el.style.display = 'none';
  }
}

function drillBuilderRender() {
  var body = document.getElementById('drl-builder-body');
  if (!body) return;

  var subjects = drillCatUniq('sub');
  var chapters = drillCatUniq('ch', drillOpts.sub ? function(i){return i.sub===drillOpts.sub;} : null);
  var topics   = drillCatUniq('top', function(i){
    if (drillOpts.sub && i.sub !== drillOpts.sub) return false;
    if (drillOpts.ch  && i.ch  !== drillOpts.ch)  return false;
    return true;
  });

  var mk = function(v,t,s){return '<option value="'+v+'"'+(s===(typeof v==='number'?v:v)?' selected':'')+'>'+t+'</option>';};

  var subOpts = '<option value="">All Subjects</option>' +
    subjects.map(function(s){return mk(s,s,drillOpts.sub);}).join('');
  var chOpts  = '<option value="0">All Chapters</option>' +
    chapters.map(function(c){return mk(c,'Ch.'+c+' — '+drillCatFindCht(c), drillOpts.ch);}).join('');
  var topOpts = '<option value="">All Topics</option>' +
    topics.map(function(t){
      var enc=encodeURIComponent(t),disp=t.length>52?t.substring(0,50)+'…':t;
      return '<option value="'+enc+'"'+(drillOpts.top===t?' selected':'')+'>'+disp+'</option>';
    }).join('');

  var difPairs  = [['all','All Difficulties'],['easy','Easy'],['medium','Medium'],['hard','Hard'],['exam_trap','Exam Trap']];
  var statPairs = [['all','All'],['unattempted','Unattempted'],['attempted','Attempted'],
    ['wrong','Previously Wrong'],['correct','Previously Correct'],['repeat_wrong','Repeatedly Wrong'],
    ['flagged','Flagged'],['slow','Slow Correct (>120s)'],['fast_wrong','Fast Wrong (<45s)']];
  var ordPairs  = [['random','Random'],['weakest','Weakest First'],['slowest','Slowest First'],['original','Original Order']];
  var cntPairs  = [10,20,40,80,200];

  var mkSel = function(id, pairs, cur, onch) {
    var opts;
    if (Array.isArray(pairs[0])) {
      opts = pairs.map(function(p){return '<option value="'+p[0]+'"'+(cur===p[0]?' selected':'')+'>'+p[1]+'</option>';}).join('');
    } else {
      opts = pairs.map(function(v){return '<option value="'+v+'"'+(cur===v?' selected':'')+'>'+v+'</option>';}).join('');
    }
    return '<select id="'+id+'" onchange="'+onch+'">'+opts+'</select>';
  };

  var presetDefs = [
    ['weak','📉 Weak Areas'],['wrong','✗ Wrong Answers'],['flagged','⚑ Flagged'],
    ['slow','🐢 Slow Correct'],['fast_wrong','⚡ Fast Wrong'],
    ['unattempted','○ Unattempted'],['public_law','⚖ Public Law'],['pr','📋 PR Ethics']
  ];

  var html = '<div class="anl-sec-hdr">Preset Drills</div>' +
    '<div class="drl-presets">' +
    presetDefs.map(function(p){
      return '<button class="drl-preset-btn" onclick="drillStartPreset(\\''+p[0]+'\\')">'+ p[1]+'</button>';
    }).join('') + '</div>';

  html += '<div class="anl-sec-hdr">Custom Drill</div>';
  html += '<div class="drl-filters">' +
    '<div class="drl-filter-row"><label>Subject</label><select id="df-sub" onchange="drillOptChange(\'sub\',this.value)">'+subOpts+'</select></div>' +
    '<div class="drl-filter-row"><label>Chapter</label><select id="df-ch" onchange="drillOptChange(\'ch\',parseInt(this.value)||0)">'+chOpts+'</select></div>' +
    '<div class="drl-filter-row"><label>Topic</label><select id="df-top" onchange="drillOptChange(\'top\',this.value?decodeURIComponent(this.value):\'\')">'+topOpts+'</select></div>' +
    '<div class="drl-filter-row"><label>Difficulty</label>'+mkSel('df-dif',difPairs,drillOpts.dif,"drillOptChange('dif',this.value)")+'</div>' +
    '<div class="drl-filter-row"><label>Attempt Status</label>'+mkSel('df-stat',statPairs,drillOpts.status,"drillOptChange('status',this.value)")+'</div>' +
    '<div class="drl-filter-row"><label>Questions</label>'+mkSel('df-cnt',cntPairs,drillOpts.count,"drillOptChange('count',parseInt(this.value))")+'</div>' +
    '<div class="drl-filter-row"><label>Order</label>'+mkSel('df-ord',ordPairs,drillOpts.order,"drillOptChange('order',this.value)")+'</div>' +
    '</div>';

  var matched = drillFilterItems(drillOpts).length;
  var capped  = Math.min(matched, drillOpts.count);
  html += '<div class="drl-preview"><strong>'+matched+'</strong> questions match — drill will use <strong>'+capped+'</strong></div>';

  body.innerHTML = html;
}

function drillOptChange(key, val) {
  drillOpts[key] = val;
  if (key === 'sub') { drillOpts.ch = 0; drillOpts.top = ''; }
  if (key === 'ch')  { drillOpts.top = ''; }
  drillBuilderRender();
}

// ── Preset Drills ────────────────────────────────────────────
function drillStartPreset(name) {
  drillOpts = { sub:'', ch:0, top:'', dif:'all', status:'all', count:40, order:'random' };
  var label = '';
  switch (name) {
    case 'weak':
      drillOpts.status='wrong'; drillOpts.order='weakest'; drillOpts.count=40;
      label = 'Weak Areas'; break;
    case 'wrong':
      drillOpts.status='wrong'; drillOpts.order='weakest'; drillOpts.count=80;
      label = 'Wrong Answers'; break;
    case 'flagged':
      drillOpts.status='flagged'; drillOpts.count=200;
      label = 'Flagged Questions'; break;
    case 'slow':
      drillOpts.status='slow'; drillOpts.order='slowest'; drillOpts.count=40;
      label = 'Slow Questions'; break;
    case 'fast_wrong':
      drillOpts.status='fast_wrong'; drillOpts.count=40;
      label = 'Fast Wrong'; break;
    case 'unattempted':
      drillOpts.status='unattempted'; drillOpts.count=40;
      label = 'Unattempted'; break;
    case 'public_law':
      drillOpts.sub='Public Law'; drillOpts.count=40;
      label = 'Public Law'; break;
    case 'pr':
      drillOpts.sub='Professional Responsibility'; drillOpts.count=40;
      label = 'PR Ethics'; break;
  }
  drillOpts._label = label;
  drillBuilderShow(false);
  buildDrillCatalog(function() { drillStart(); });
}

// ── Start Session ────────────────────────────────────────────
function drillStart() {
  var items  = drillFilterItems(drillOpts);
  var sorted = drillSortItems(items.slice(), drillOpts.order);
  var capped = sorted.slice(0, drillOpts.count);
  if (!capped.length) {
    alert('No questions match the selected filters.\\nTry adjusting your criteria.');
    drillBuilderShow(true);
    return;
  }

  var labelParts = [];
  if (drillOpts.sub) labelParts.push(drillOpts.sub);
  if (drillOpts.ch)  labelParts.push('Ch.' + drillOpts.ch);
  if (drillOpts.top) labelParts.push(drillOpts.top.substring(0,28));
  if (drillOpts.dif && drillOpts.dif !== 'all') labelParts.push(drillOpts.dif);
  var statusLabel = {
    unattempted:'Unattempted',attempted:'Attempted',wrong:'Wrong',correct:'Correct',
    repeat_wrong:'Repeat Wrong',flagged:'Flagged',slow:'Slow',fast_wrong:'Fast Wrong'
  }[drillOpts.status] || '';
  if (statusLabel) labelParts.push(statusLabel);
  var label = drillOpts._label || (labelParts.length ? labelParts.join(' — ') : 'Custom Drill');
  delete drillOpts._label;

  var sessId = 'drill_' + Date.now();
  var qs = capped.map(function(item, i) {
    return {
      id: i + 1,
      sec: item.q.sec,
      text: item.q.text,
      opts: item.q.opts,
      ans: item.q.ans,
      expl: item.q.expl,
      caseRef: item.q.caseRef,
      lso: item.q.lso,
      canonId: item.canonId,
      sourceExamKey: item.sourceExamKey,
      sourceSeqId: item.sourceSeqId,
      ch: item.ch,
      cht: item.cht,
      top: item.top,
      dif: item.dif,
      examLabel: '🎯 ' + label
    };
  });

  drillSess = {
    label: label,
    qs: qs,
    cur: 0,
    answers: qs.map(function(){ return null; }),
    qTimes: qs.map(function(){ return 0; }),
    qStarts: {},
    totalSec: 0,
    started: true,
    finished: false,
    sessId: sessId,
    timerID: null
  };

  anlSess = { id: sessId, examKey: 'drill', startedAt: new Date().toISOString(), keys: [] };

  drillBuilderShow(false);
  document.getElementById('drill-session').style.display = 'flex';
  document.getElementById('drl-s-name').textContent = '🎯 ' + label;

  drillSess.qStarts[0] = Date.now();
  drillSess.timerID = setInterval(function() {
    if (!drillSess || drillSess.finished) return;
    drillSess.totalSec++;
    var cur = drillSess.cur;
    if (drillSess.qStarts[cur]) {
      drillSess.qTimes[cur] = Math.round((Date.now() - drillSess.qStarts[cur]) / 1000);
    }
    var m = Math.floor(drillSess.totalSec / 60);
    var s = drillSess.totalSec % 60;
    var el = document.getElementById('drl-timer');
    if (el) el.textContent = m + ':' + (s < 10 ? '0' : '') + s;
  }, 1000);

  drillRenderQ();
  drillBuildJump();
}

// ── Render ───────────────────────────────────────────────────
function drillEsc(str) {
  if (!str) return '';
  return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function drillRenderQ() {
  if (!drillSess) return;
  var body = document.getElementById('drl-s-body');
  if (!body) return;
  var i = drillSess.cur, q = drillSess.qs[i];
  var answered = drillSess.answers[i] !== null;
  var LABS = ['A','B','C','D'];

  var html = '<div class="drl-q-text">' + drillEsc(q.text) + '</div>';
  html += '<div class="drl-opts">';
  for (var k = 0; k < q.opts.length; k++) {
    var cls = 'drl-opt';
    if (answered) {
      if (k === q.ans) cls += ' correct';
      else if (k === drillSess.answers[i]) cls += ' wrong';
    }
    var click = answered ? 'disabled' : ('onclick="drillPick('+k+')"');
    html += '<button class="'+cls+'" '+click+'><span class="drl-opt-lbl">'+LABS[k]+'</span> '+drillEsc(q.opts[k])+'</button>';
  }
  html += '</div>';
  if (answered) {
    html += '<div class="drl-expl">' + drillEsc(q.expl);
    if (q.caseRef) html += '<div class="drl-ref">📖 ' + drillEsc(q.caseRef) + '</div>';
    if (q.lso)     html += '<div class="drl-ref">LSO: ' + drillEsc(q.lso) + '</div>';
    html += '</div>';
  }
  body.innerHTML = html;

  var correct  = 0, attempted = 0;
  for (var j = 0; j < drillSess.answers.length; j++) {
    if (drillSess.answers[j] !== null) {
      attempted++;
      if (drillSess.answers[j] === drillSess.qs[j].ans) correct++;
    }
  }
  var scEl = document.getElementById('drl-sc');
  if (scEl) scEl.textContent = (i+1)+'/'+drillSess.qs.length+' · '+correct+'/'+attempted+' correct';

  var fb = document.getElementById('drl-flag-btn');
  if (fb) {
    var flagged = anlIsFlagged(q.sourceExamKey, q.sourceSeqId);
    fb.textContent = flagged ? '⚑ Flagged' : '⚑ Flag';
    if (flagged) fb.classList.add('flagged'); else fb.classList.remove('flagged');
  }
}

function drillRecordQTime() {
  if (!drillSess) return;
  var cur = drillSess.cur;
  if (drillSess.qStarts[cur]) {
    drillSess.qTimes[cur] += Math.round((Date.now() - drillSess.qStarts[cur]) / 1000);
    drillSess.qStarts[cur] = 0;
  }
}

function drillPick(idx) {
  if (!drillSess || drillSess.finished) return;
  var i = drillSess.cur;
  if (drillSess.answers[i] !== null) return;
  drillRecordQTime();
  drillSess.answers[i] = idx;
  anlRecord('drill', drillSess.qs[i], idx, drillSess.qTimes[i]);
  drillRenderQ();
  drillBuildJump();
}

function drillNav(dir) {
  if (!drillSess) return;
  drillRecordQTime();
  var next = drillSess.cur + dir;
  if (next < 0 || next >= drillSess.qs.length) return;
  drillSess.cur = next;
  drillSess.qStarts[next] = Date.now();
  drillRenderQ();
  drillBuildJump();
}

function drillGoTo(i) {
  if (!drillSess) return;
  drillRecordQTime();
  drillSess.cur = i;
  drillSess.qStarts[i] = Date.now();
  drillRenderQ();
  drillBuildJump();
}

function drillBuildJump() {
  if (!drillSess) return;
  var el = document.getElementById('drl-jump');
  if (!el) return;
  var html = '';
  for (var i = 0; i < drillSess.qs.length; i++) {
    var q = drillSess.qs[i], a = drillSess.answers[i];
    var cls = 'drl-jb';
    if (i === drillSess.cur) cls += ' cur';
    if (a !== null) cls += (a === q.ans ? ' good' : ' bad');
    if (anlIsFlagged(q.sourceExamKey, q.sourceSeqId)) cls += ' flagged';
    html += '<button class="'+cls+'" onclick="drillGoTo('+i+')">'+(i+1)+'</button>';
  }
  el.innerHTML = html;
}

function drillToggleFlag() {
  if (!drillSess) return;
  var q = drillSess.qs[drillSess.cur];
  var key = q.sourceExamKey + ':' + q.sourceSeqId;
  var d = anlLoad();
  if (d.flaggedQuestions[key]) delete d.flaggedQuestions[key];
  else d.flaggedQuestions[key] = true;
  anlSave(d);
  drillRenderQ();
  drillBuildJump();
}

function drillFinish() {
  if (!drillSess) return;
  drillRecordQTime();
  if (drillSess.timerID) clearInterval(drillSess.timerID);
  drillSess.finished = true;
  anlEndSession();
  document.getElementById('drill-session').style.display = 'none';
  drillReportShow(true);
}

// ── Drill Report ─────────────────────────────────────────────
function drillReportShow(show) {
  var el = document.getElementById('drill-report');
  if (!el) return;
  if (show) {
    el.style.display = 'flex';
    document.getElementById('drl-report-body').innerHTML = drillBuildReport();
  } else {
    el.style.display = 'none';
  }
}

function drillBuildReport() {
  if (!drillSess) return '<div class="anl-empty">No drill data.</div>';
  var qs = drillSess.qs, ans = drillSess.answers, times = drillSess.qTimes;

  var total = 0, correct = 0;
  for (var i = 0; i < ans.length; i++) {
    if (ans[i] !== null) { total++; if (ans[i] === qs[i].ans) correct++; }
  }
  var wrong  = total - correct;
  var acc    = total ? Math.round((correct/total)*100) : 0;
  var timeSum = 0, timeCnt = 0;
  for (var i = 0; i < ans.length; i++) { if (ans[i] !== null) { timeSum += times[i]; timeCnt++; } }
  var avgTime = timeCnt ? Math.round(timeSum/timeCnt) : 0;

  var html = '<div style="background:rgba(99,102,241,.1);border:1px solid rgba(99,102,241,.3);border-radius:8px;padding:10px 12px;margin-bottom:12px;font-size:13px;color:var(--text2)">' +
    '🎯 <strong style="color:var(--text1)">'+drillEsc(drillSess.label)+'</strong> &mdash; '+drillSess.qs.length+' questions</div>';

  html += '<div class="anl-stats-grid">';
  html += anlStat('Attempted', total, '');
  html += anlStat('Correct', correct, '#22c55e');
  html += anlStat('Wrong', wrong, '#ef4444');
  html += anlStat('Accuracy', acc+'%', acc>=70?'#22c55e':acc>=50?'#f59e0b':'#ef4444');
  html += anlStat('Avg Time', avgTime+'s', '');
  html += '</div>';

  // Subject bars
  var subMap = {};
  for (var i = 0; i < qs.length; i++) {
    if (ans[i] === null) continue;
    var sub = qs[i].sec || 'Unknown';
    if (!subMap[sub]) subMap[sub] = {ok:0,total:0};
    subMap[sub].total++;
    if (ans[i] === qs[i].ans) subMap[sub].ok++;
  }
  var subs = Object.keys(subMap);
  if (subs.length > 1) {
    html += '<div class="anl-sec-hdr">Subject Accuracy</div><div class="anl-bars">';
    subs.sort().forEach(function(sub) {
      var m=subMap[sub], pct=Math.round((m.ok/m.total)*100);
      var col=pct>=70?'#22c55e':pct>=50?'#f59e0b':'#ef4444';
      html += '<div class="anl-bar-row"><div class="anl-bar-lbl">'+sub.split(' ')[0]+'</div>' +
        '<div class="anl-bar-bg"><div class="anl-bar-fill" style="width:'+pct+'%;background:'+col+'"></div></div>' +
        '<div class="anl-bar-pct">'+pct+'% ('+m.total+')</div></div>';
    });
    html += '</div>';
  }

  // Weak chapters
  var chMap = {};
  for (var i = 0; i < qs.length; i++) {
    if (ans[i] === null || !qs[i].cht) continue;
    if (!chMap[qs[i].cht]) chMap[qs[i].cht] = {ok:0,total:0};
    chMap[qs[i].cht].total++;
    if (ans[i] === qs[i].ans) chMap[qs[i].cht].ok++;
  }
  var weakChs = Object.keys(chMap).filter(function(ch){
    return chMap[ch].total >= 2 && Math.round((chMap[ch].ok/chMap[ch].total)*100) < 70;
  }).sort(function(a,b){return (chMap[a].ok/chMap[a].total)-(chMap[b].ok/chMap[b].total);});
  if (weakChs.length) {
    html += '<div class="anl-sec-hdr">Weak Chapters</div><div class="anl-list">';
    weakChs.slice(0,6).forEach(function(ch){
      var m=chMap[ch], pct=Math.round((m.ok/m.total)*100);
      html += '<div class="anl-list-item"><div class="anl-list-name">'+drillEsc(ch)+'</div><div class="anl-list-val anl-bad">'+pct+'%</div></div>';
    });
    html += '</div>';
  }

  // Slowest 5
  var answered = [];
  for (var i = 0; i < qs.length; i++) {
    if (ans[i] !== null) answered.push({q:qs[i], time:times[i], correct:ans[i]===qs[i].ans});
  }
  answered.sort(function(a,b){return b.time-a.time;});
  if (answered.length) {
    html += '<div class="anl-sec-hdr">Slowest Questions</div><div class="anl-list">';
    answered.slice(0,5).forEach(function(x){
      html += '<div class="anl-list-item"><div class="anl-list-name">'+drillEsc(x.q.sec||'')+(x.q.cht?' — '+drillEsc(x.q.cht):'')+'</div>' +
        '<div class="anl-list-val" style="color:#f59e0b">'+x.time+'s</div></div>';
    });
    html += '</div>';
  }

  // Fast wrong
  var fastWrong = answered.filter(function(x){return !x.correct && x.time<45;});
  if (fastWrong.length) {
    html += '<div class="anl-sec-hdr">Likely Guessing (wrong &lt;45s)</div><div class="anl-list">';
    fastWrong.slice(0,5).forEach(function(x){
      html += '<div class="anl-list-item"><div class="anl-list-name">'+drillEsc(x.q.sec||'')+'</div><div class="anl-list-val anl-bad">'+x.time+'s</div></div>';
    });
    html += '</div>';
  }

  // Recommendations
  var recs = [];
  subs.forEach(function(sub){
    var m=subMap[sub],pct=Math.round((m.ok/m.total)*100);
    if(pct<70) recs.push('Review '+sub+' material ('+pct+'% accuracy)');
  });
  if (avgTime>110) recs.push('Work on speed — avg '+avgTime+'s per question');
  if (fastWrong.length>=3) recs.push('Slow down — '+fastWrong.length+' quick wrong answers detected');
  weakChs.slice(0,3).forEach(function(ch){
    var pct=Math.round((chMap[ch].ok/chMap[ch].total)*100);
    recs.push('Focus on: '+ch+' ('+pct+'%)');
  });
  if (recs.length) {
    html += '<div class="anl-sec-hdr">Recommendations</div><div class="anl-recs">';
    recs.forEach(function(r){html+='<div class="anl-rec-item">'+r+'</div>';});
    html += '</div>';
  }

  return html;
}

// ── Visibility pause for drill ────────────────────────────────
document.addEventListener('visibilitychange', function() {
  if (!drillSess || drillSess.finished) return;
  var cur = drillSess.cur;
  if (document.hidden) {
    if (drillSess.qStarts[cur]) {
      drillSess.qTimes[cur] += Math.round((Date.now() - drillSess.qStarts[cur]) / 1000);
      drillSess.qStarts[cur] = 0;
    }
  } else {
    drillSess.qStarts[cur] = Date.now();
  }
});

// ── Dashboard quick-drill injection ──────────────────────────
(function() {
  var _origAnlDash = anlDashboard;
  anlDashboard = function(show) {
    _origAnlDash(show);
    if (!show) return;
    var body = document.getElementById('anl-dash-body');
    if (!body) return;
    body.insertAdjacentHTML('beforeend',
      '<div class="anl-sec-hdr">Quick Drills</div>' +
      '<div class="drl-presets">' +
      '<button class="drl-preset-btn" onclick="anlDashboard(false);drillStartPreset(\\'weak\\')">📉 Weak Areas Drill</button>' +
      '<button class="drl-preset-btn" onclick="anlDashboard(false);drillStartPreset(\\'wrong\\')">✗ Wrong Answers Drill</button>' +
      '<button class="drl-preset-btn" onclick="anlDashboard(false);drillStartPreset(\\'flagged\\')">⚑ Flagged Drill</button>' +
      '<button class="drl-preset-btn" onclick="anlDashboard(false);drillStartPreset(\\'unattempted\\')">○ Unattempted Drill</button>' +
      '</div>'
    );
  };
})();

"""

# ══════════════════════════════════════════════════════════════
# NAV BUTTON IIFE
# ══════════════════════════════════════════════════════════════
DRILL_NAV_INIT = """\
// Add Drill Builder nav button
(function(){
  var nav = document.querySelector('.anl-nav-btns') || document.querySelector('.topnav');
  if (nav) {
    var btn = document.createElement('button');
    btn.className = 'anl-dash-btn';
    btn.textContent = '🎯 Drill';
    btn.onclick = function(){ buildDrillCatalog(function(){ drillBuilderShow(true); }); };
    nav.appendChild(btn);
  }
})();
"""

# ══════════════════════════════════════════════════════════════
# anlRecord patches — support drill question metadata
# ══════════════════════════════════════════════════════════════

ANL_RECORD_POSMAP_OLD = \
    '  var posMap = (anlGetMeta().examPositions || {})[examId] || null;\n' \
    '  var actualId = posMap ? (posMap[String(q.id)] || (examId + \':\' + q.id)) : (examId + \':\' + q.id);'

ANL_RECORD_POSMAP_NEW = \
    '  var posMap = (anlGetMeta().examPositions || {})[examId] || null;\n' \
    '  var actualId = q.canonId ? q.canonId : (posMap ? (posMap[String(q.id)] || (examId + \':\' + q.id)) : (examId + \':\' + q.id));'

ANL_RECORD_META_OLD = \
    "    chapterNumber: meta ? (meta.ch || '') : '',\n" \
    "    chapterTitle: meta ? (meta.cht || '') : '',\n" \
    "    topicHeading: meta ? (meta.top || '') : '',"

ANL_RECORD_META_NEW = \
    "    chapterNumber: meta ? (meta.ch || '') : (q.ch || ''),\n" \
    "    chapterTitle: meta ? (meta.cht || '') : (q.cht || ''),\n" \
    "    topicHeading: meta ? (meta.top || '') : (q.top || ''),"

ANL_RECORD_LABEL_OLD = \
    "    examLabel: (EXAMS[examId] && EXAMS[examId].name) ? EXAMS[examId].name : examId,"

ANL_RECORD_LABEL_NEW = \
    "    examLabel: (EXAMS[examId] && EXAMS[examId].name) ? EXAMS[examId].name : (q.examLabel || examId),"


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════
def main():
    print('=== Phase 3B Drill Builder Patch ===')

    if not os.path.exists(INDEX_PATH):
        print(f'ERROR: {INDEX_PATH} not found')
        sys.exit(1)

    with open(INDEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f'Read index.html ({len(content):,} bytes)')

    # 1. CSS
    content = patch(content, '</style>', DRILL_CSS + '</style>', 'drill CSS')

    # 2. anlRecord: support q.canonId
    content = patch(content, ANL_RECORD_POSMAP_OLD, ANL_RECORD_POSMAP_NEW, 'anlRecord: canonId support')

    # 3. anlRecord: drill metadata fallbacks (ch/cht/top)
    content = patch(content, ANL_RECORD_META_OLD, ANL_RECORD_META_NEW, 'anlRecord: drill metadata fallbacks')

    # 4. anlRecord: examLabel fallback
    content = patch(content, ANL_RECORD_LABEL_OLD, ANL_RECORD_LABEL_NEW, 'anlRecord: examLabel fallback')

    # 5. Modal HTML before </body>
    content = patch(content, '</body>', DRILL_HTML + '</body>', 'drill modal HTML')

    # 6. Drill JS module before buildPanel('bar');
    content = patch(content, "buildPanel('bar');", DRILL_JS + "buildPanel('bar');", 'drill JS module')

    # 7. Nav button — append after existing analytics IIFE
    content = patch(
        content,
        "})();\n",                      # end of analytics nav-button IIFE
        "})();\n" + DRILL_NAV_INIT,
        'drill nav button'
    )

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'\nWrote index.html ({len(content):,} bytes)')
    print('=== Done — Phase 3B drill injected ===')


if __name__ == '__main__':
    main()
