#!/usr/bin/env python3
"""
patch_3ui.py — Phase 3UI: Light Mode + Bar Exam Hub Dashboard
Patches index.html with:
  1. UI_CSS  — light mode variable override + hub/card CSS
  2. UI_HTML — #hub overlay with sections, cards, nav
  3. UI_JS   — hub JS: stats, build, event delegation, init
"""
import os, sys

BASE  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(BASE, 'index.html')

# ============================================================
# 1. CSS — Light Mode + Hub Styles
# ============================================================
UI_CSS = """
/* ============================================================
   Phase 3UI — Light Mode Override + Hub Dashboard Styles
   ============================================================ */
:root{
  --bg:#f5f7fa;--surface:#ffffff;--surface2:#edf1f7;
  --border:#dde3ef;--border2:#c5cfdf;
  --text:#0d1526;--text2:#3d4f6e;--text3:#7a8da8;
  --bg0:#f5f7fa;--bg1:#ffffff;--bg2:#edf1f7;
  --text1:#0d1526;--border1:#dde3ef;--accent:#6366f1;
  --blue-dim:#dbeafe;--green-dim:#dcfce7;--red-dim:#fee2e2;
  --purple-dim:#ede9fe;--teal-dim:#ccfbf1;--amber-dim:#fef3c7;
  --blue-light:#2563eb;--green-light:#16a34a;--red-light:#dc2626;
  --purple-light:#7c3aed;--teal-light:#0d9488;--amber-light:#d97706;
}
body{background:var(--bg)!important;color:var(--text)!important}
.nav-brand h1{color:var(--text)!important}
.opt{color:var(--text2)!important;background:var(--surface)!important}
.opt:hover:not(:disabled){background:var(--surface2)!important}
.timer{color:var(--text)!important;background:var(--surface2)!important;border-color:var(--border)!important}
.qnum{color:var(--text)!important;background:var(--surface2)!important}
.expl{background:var(--surface2)!important}

/* ---- HUB OVERLAY ---- */
#hub{position:fixed;inset:0;z-index:1000;background:var(--bg);overflow-y:auto;
     display:flex;flex-direction:column}

/* Hub top nav */
#hub-nav{display:flex;align-items:center;gap:0;background:var(--surface);
         border-bottom:1px solid var(--border);padding:0 20px;
         position:sticky;top:0;z-index:10;flex-shrink:0;flex-wrap:wrap}
#hub-brand{font-size:16px;font-weight:800;color:var(--text);
           padding:14px 20px 14px 0;margin-right:8px;
           border-right:1px solid var(--border);letter-spacing:-.3px;
           white-space:nowrap;flex-shrink:0}
#hub-brand-accent{color:var(--accent)}
.hub-nav-btn{padding:6px 13px;border:none;background:transparent;cursor:pointer;
             font-size:13px;color:var(--text2);font-family:inherit;font-weight:500;
             border-radius:8px;transition:all .15s;white-space:nowrap}
.hub-nav-btn:hover{background:var(--surface2);color:var(--text)}
.hub-nav-btn.hub-nav-active{color:var(--accent);font-weight:700}
#hub-nav-right{margin-left:auto;display:flex;align-items:center;gap:4px}

/* Hub body */
#hub-body{max-width:1060px;width:100%;margin:0 auto;padding:28px 24px 52px}

/* Section */
.hub-section{margin-bottom:36px}
.hub-section-title{font-size:11px;font-weight:700;text-transform:uppercase;
                   letter-spacing:.08em;color:var(--text3);margin-bottom:14px;
                   padding-bottom:8px;border-bottom:1px solid var(--border)}

/* Card grid */
.hub-card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:14px}
.hub-card-grid-sm{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px}

/* Exam card */
.hub-card{background:var(--surface);border:1px solid var(--border);border-radius:12px;
          padding:16px 18px 14px;display:flex;flex-direction:column;
          transition:border-color .15s,box-shadow .15s}
.hub-card:hover{border-color:var(--border2);box-shadow:0 2px 14px rgba(0,0,0,.06)}
.hub-card-header{display:flex;align-items:flex-start;justify-content:space-between;
                 gap:8px;margin-bottom:6px}
.hub-card-title{font-size:14px;font-weight:700;color:var(--text);line-height:1.35}
.hub-card-badge{font-size:10px;font-weight:700;padding:3px 8px;border-radius:20px;
                white-space:nowrap;flex-shrink:0;margin-top:2px}
.hub-badge-imported{background:#fef3c7;color:#92400e}
.hub-badge-generated{background:#dcfce7;color:#15803d}
.hub-badge-pr{background:#ede9fe;color:#6d28d9}
.hub-card-sub{font-size:11px;color:var(--text3);margin-bottom:10px;line-height:1.4}

/* Card stats */
.hub-card-stats{display:flex;align-items:center;gap:10px;
                padding:8px 0;border-top:1px solid var(--border);
                border-bottom:1px solid var(--border);margin-bottom:10px;
                flex-wrap:wrap}
.hub-stat{display:flex;flex-direction:column;align-items:flex-start;gap:1px}
.hub-stat-val{font-size:15px;font-weight:800;color:var(--text);
              font-variant-numeric:tabular-nums;line-height:1}
.hub-stat-lbl{font-size:9px;color:var(--text3);text-transform:uppercase;
              letter-spacing:.06em;white-space:nowrap}
.hub-stat-div{width:1px;height:26px;background:var(--border);flex-shrink:0}

/* Card progress bar */
.hub-card-pb{height:3px;background:var(--surface2);border-radius:2px;
             margin-bottom:10px;overflow:hidden}
.hub-card-pb-fill{height:100%;border-radius:2px;background:var(--accent);
                  transition:width .3s}

/* Card action buttons */
.hub-card-btns{display:flex;flex-wrap:wrap;gap:6px;margin-top:auto;padding-top:2px}
.hub-cbtn{padding:5px 12px;border-radius:7px;border:1px solid var(--border);
          background:transparent;cursor:pointer;font-size:11px;font-weight:600;
          color:var(--text);font-family:inherit;transition:all .15s;white-space:nowrap}
.hub-cbtn:hover{background:var(--surface2);border-color:var(--border2)}
.hub-cbtn-primary{background:var(--accent)!important;border-color:var(--accent)!important;color:#fff!important}
.hub-cbtn-primary:hover{opacity:.88!important}
.hub-cbtn-wrong{background:#fef2f2!important;border-color:#fecaca!important;color:#b91c1c!important}
.hub-cbtn-wrong:hover{background:#fee2e2!important}
.hub-cbtn-flag{background:#fffbeb!important;border-color:#fde68a!important;color:#b45309!important}
.hub-cbtn-flag:hover{background:#fef3c7!important}

/* Tool cards */
.hub-tools-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}
.hub-tool-card{background:var(--surface);border:1px solid var(--border);border-radius:12px;
               padding:18px 20px;cursor:pointer;transition:all .15s;
               display:flex;flex-direction:column;align-items:flex-start;gap:6px}
.hub-tool-card:hover{border-color:var(--accent);box-shadow:0 2px 14px rgba(99,102,241,.13)}
.hub-tool-icon{font-size:24px;line-height:1}
.hub-tool-label{font-size:14px;font-weight:700;color:var(--text)}
.hub-tool-desc{font-size:12px;color:var(--text3);line-height:1.4}

/* Quick drill buttons */
.hub-quick-grid{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px}
.hub-quick-btn{padding:7px 16px;border-radius:8px;border:1px solid var(--border);
               background:var(--surface);cursor:pointer;font-size:12px;
               color:var(--text);font-family:inherit;font-weight:600;transition:all .15s}
.hub-quick-btn:hover{background:var(--surface2);border-color:var(--border2)}

/* Recent exam cards */
.hub-recent-strip{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px}
.hub-recent-card{background:var(--surface);border:1.5px solid var(--accent);
                 border-radius:10px;padding:10px 14px;cursor:pointer;
                 transition:box-shadow .15s;flex:1 1 190px;max-width:280px}
.hub-recent-card:hover{box-shadow:0 2px 12px rgba(99,102,241,.16)}
.hub-recent-title{font-size:13px;font-weight:700;color:var(--text)}
.hub-recent-meta{font-size:11px;color:var(--text3);margin-top:2px}
.hub-recent-acc{font-size:12px;font-weight:700;color:var(--accent);margin-top:4px}

/* Empty state */
.hub-empty{padding:28px;text-align:center;color:var(--text3);font-size:13px;
           border:1px dashed var(--border);border-radius:10px}

/* Back-to-hub button (injected into existing topnav) */
#hub-back-btn{padding:5px 12px;border-radius:8px;border:1px solid var(--border);
              background:transparent;cursor:pointer;font-size:12px;color:var(--text2);
              font-family:inherit;font-weight:600;margin-right:8px;
              display:none;transition:all .15s;flex-shrink:0}
#hub-back-btn:hover{background:var(--surface2);color:var(--text)}

@media(max-width:640px){
  #hub-body{padding:14px 12px 36px}
  .hub-card-grid{grid-template-columns:1fr}
  .hub-card-grid-sm{grid-template-columns:1fr}
  #hub-nav{padding:0 12px}
  #hub-brand{font-size:14px;padding:10px 12px 10px 0}
}
"""

# ============================================================
# 2. HTML — Hub Overlay
# ============================================================
UI_HTML = """<!-- ====================================================
     Phase 3UI — Bar Exam Hub Dashboard Overlay
     ==================================================== -->
<div id="hub">
  <nav id="hub-nav">
    <div id="hub-brand"><span id="hub-brand-accent">&#9878;</span> Bar Exam Hub</div>
    <button class="hub-nav-btn hub-nav-active" data-hub-nav="home">Home</button>
    <button class="hub-nav-btn" data-hub-nav="exams">Exams</button>
    <button class="hub-nav-btn" data-hub-nav="pr">Professional Responsibility</button>
    <div id="hub-nav-right">
      <button class="hub-nav-btn" data-hub-tool="drill">&#127919; Drill</button>
      <button class="hub-nav-btn" data-hub-tool="progress">&#128202; Progress</button>
      <button class="hub-nav-btn" data-hub-tool="studyplan">&#129517; Study Plan</button>
    </div>
  </nav>
  <div id="hub-body"></div>
</div>
"""

# ============================================================
# 3. JS — Hub Logic (ES5, data-* event delegation)
# ============================================================
UI_JS = r"""
// ============================================================
// Phase 3UI — Bar Exam Hub Dashboard
// ============================================================
(function() {
'use strict';

// --- Exam catalogue ---
var HUB_EXAMS = [
  {id:'bar',   title:'LSO Barrister A',      count:160, type:'Imported',  typeClass:'imported', group:'bar',
   subs:['Civil Litigation','Criminal Law','Family Law','Public Law','Professional Responsibility']},
  {id:'sol',   title:'LSO Solicitor A',       count:160, type:'Imported',  typeClass:'imported', group:'bar',
   subs:['Civil Litigation','Criminal Law','Family Law','Public Law','Professional Responsibility']},
  {id:'bar2',  title:'LSO Barrister B',       count:160, type:'Imported',  typeClass:'imported', group:'bar',
   subs:['Civil Litigation','Criminal Law','Family Law','Public Law','Professional Responsibility']},
  {id:'barc',  title:'Generated Barrister C', count:160, type:'Generated', typeClass:'generated',group:'bar',
   subs:['Civil Litigation','Criminal Law','Family Law','Public Law','Professional Responsibility']},
  {id:'bard',  title:'Generated Barrister D', count:160, type:'Generated', typeClass:'generated',group:'bar',
   subs:['Civil Litigation','Criminal Law','Family Law','Public Law','Professional Responsibility']},
  {id:'bare',  title:'Generated Barrister E', count:160, type:'Generated', typeClass:'generated',group:'bar',
   subs:['Civil Litigation','Criminal Law','Family Law','Public Law','Professional Responsibility']},
  {id:'barf',  title:'Generated Barrister F', count:160, type:'Generated', typeClass:'generated',group:'bar',
   subs:['Civil Litigation','Criminal Law','Family Law','Public Law','Professional Responsibility']},
  {id:'abp',   title:'ABP Full Barrister',    count:160, type:'Imported',  typeClass:'imported', group:'bar',
   subs:['Civil Litigation','Criminal Law','Family Law','Public Law','Professional Responsibility']},
  {id:'mini',  title:'ABP Mini Exam',         count:80,  type:'Imported',  typeClass:'imported', group:'bar',
   subs:['Civil Litigation','Criminal Law','Family Law','Public Law','Professional Responsibility']},
  {id:'prdra', title:'Generated PR Drill A',  count:100, type:'PR Drill',  typeClass:'pr',       group:'pr',
   subs:['Professional Responsibility']},
  {id:'prdrb', title:'Generated PR Drill B',  count:100, type:'PR Drill',  typeClass:'pr',       group:'pr',
   subs:['Professional Responsibility']},
  {id:'prb200',title:'Generated PR Bank 200', count:200, type:'PR Bank',   typeClass:'pr',       group:'pr',
   subs:['Professional Responsibility']}
];

// --- Analytics ---
function hubLoadData() {
  try { return JSON.parse(localStorage.getItem('acethebar.analytics.v1') || '{}'); }
  catch(e) { return {}; }
}

function hubExamStats(examId) {
  var d = hubLoadData();
  var attempts = d.attempts || {};
  var flagged  = d.flaggedQuestions || {};
  var pfx = examId + ':';
  var attempted = 0, correct = 0, wrong = 0, lastMs = 0;
  var keys = Object.keys(attempts);
  for (var i = 0; i < keys.length; i++) {
    var k = keys[i];
    if (k.indexOf(pfx) !== 0) continue;
    var arr = attempts[k];
    if (!arr || !arr.length) continue;
    attempted++;
    var last = arr[arr.length - 1];
    if (last.isCorrect) correct++; else wrong++;
    if (last.answeredAt) {
      var t = new Date(last.answeredAt).getTime();
      if (t > lastMs) lastMs = t;
    }
  }
  var total = correct + wrong;
  var accuracy = total > 0 ? Math.round(correct / total * 100) : null;
  var nFlagged = 0;
  var fkeys = Object.keys(flagged);
  for (var j = 0; j < fkeys.length; j++) {
    if (fkeys[j].indexOf(pfx) === 0 && flagged[fkeys[j]]) nFlagged++;
  }
  return {attempted:attempted, correct:correct, wrong:wrong,
          accuracy:accuracy, lastMs:lastMs, flagged:nFlagged};
}

function hubRelTime(ms) {
  if (!ms) return '';
  var diff = Date.now() - ms;
  var m = Math.floor(diff / 60000);
  if (m < 2)  return 'just now';
  if (m < 60) return m + 'm ago';
  var h = Math.floor(m / 60);
  if (h < 24) return h + 'h ago';
  var dd = Math.floor(h / 24);
  if (dd < 7) return dd + 'd ago';
  return Math.floor(dd / 7) + 'w ago';
}

// --- Card HTML builder ---
function hubBuildCard(cfg) {
  var st = hubExamStats(cfg.id);
  var pct = cfg.count > 0 ? Math.round(st.attempted / cfg.count * 100) : 0;
  var accStr = st.accuracy !== null ? st.accuracy + '%' : '--';
  var lastStr = st.lastMs ? hubRelTime(st.lastMs) : 'Not started';

  var pbFill = pct > 0 ? '<div class="hub-card-pb-fill" style="width:' + pct + '%"></div>' : '';

  var statsHtml =
    '<div class="hub-card-stats">' +
      '<div class="hub-stat"><div class="hub-stat-val">' + st.attempted + '</div>' +
        '<div class="hub-stat-lbl">Done</div></div>' +
      '<div class="hub-stat-div"></div>' +
      '<div class="hub-stat"><div class="hub-stat-val">' + (cfg.count - st.attempted) + '</div>' +
        '<div class="hub-stat-lbl">Left</div></div>' +
      '<div class="hub-stat-div"></div>' +
      '<div class="hub-stat"><div class="hub-stat-val">' + accStr + '</div>' +
        '<div class="hub-stat-lbl">Accuracy</div></div>' +
      '<div class="hub-stat-div"></div>' +
      '<div class="hub-stat"><div class="hub-stat-val" style="font-size:11px;font-weight:600">' + lastStr + '</div>' +
        '<div class="hub-stat-lbl">Last used</div></div>' +
    '</div>';

  var startLabel = st.attempted > 0 ? '&#9654; Resume' : '&#9654; Start';
  var btns = '<button class="hub-cbtn hub-cbtn-primary" data-hub-go="' + cfg.id + '">' + startLabel + '</button>';
  if (st.wrong > 0) {
    btns += ' <button class="hub-cbtn hub-cbtn-wrong" data-hub-wrong="' + cfg.id + '">' +
            '&#10007; Wrong (' + st.wrong + ')</button>';
  }
  if (st.flagged > 0) {
    btns += ' <button class="hub-cbtn hub-cbtn-flag" data-hub-flagged="' + cfg.id + '">' +
            '&#9873; Flagged (' + st.flagged + ')</button>';
  }

  return '<div class="hub-card">' +
    '<div class="hub-card-header">' +
      '<div class="hub-card-title">' + cfg.title + '</div>' +
      '<span class="hub-card-badge hub-badge-' + cfg.typeClass + '">' + cfg.type + '</span>' +
    '</div>' +
    '<div class="hub-card-sub">' + cfg.count + ' questions</div>' +
    '<div class="hub-card-pb">' + pbFill + '</div>' +
    statsHtml +
    '<div class="hub-card-btns">' + btns + '</div>' +
    '</div>';
}

// --- Recent exams (sorted by last used) ---
function hubGetRecent(n) {
  var rows = [];
  for (var i = 0; i < HUB_EXAMS.length; i++) {
    var cfg = HUB_EXAMS[i];
    var st = hubExamStats(cfg.id);
    if (st.lastMs > 0) rows.push({cfg:cfg, st:st});
  }
  rows.sort(function(a, b) { return b.st.lastMs - a.st.lastMs; });
  return rows.slice(0, n);
}

// --- Build hub page body ---
function hubBuildBody(section) {
  section = section || 'home';
  var html = '';

  // ---- Continue Studying ----
  if (section === 'home') {
    var recent = hubGetRecent(3);
    html += '<div class="hub-section">' +
            '<div class="hub-section-title">Continue Studying</div>';
    if (recent.length === 0) {
      html += '<div class="hub-empty">No exams started yet &mdash; open any exam below to begin.</div>';
    } else {
      html += '<div class="hub-recent-strip">';
      for (var r = 0; r < recent.length; r++) {
        var item = recent[r];
        var accLine = item.st.accuracy !== null ? '<div class="hub-recent-acc">' + item.st.accuracy + '% accuracy</div>' : '';
        html += '<div class="hub-recent-card" data-hub-go="' + item.cfg.id + '">' +
                  '<div class="hub-recent-title">' + item.cfg.title + '</div>' +
                  '<div class="hub-recent-meta">' + item.st.attempted + ' / ' + item.cfg.count +
                    ' done &middot; ' + hubRelTime(item.st.lastMs) + '</div>' +
                  accLine +
                '</div>';
      }
      html += '</div>';
    }
    html += '<div class="hub-quick-grid">' +
              '<button class="hub-quick-btn" data-hub-tool="drill-weak">&#128197; Weak Areas</button>' +
              '<button class="hub-quick-btn" data-hub-tool="drill-wrong">&#10007; Wrong Answers</button>' +
              '<button class="hub-quick-btn" data-hub-tool="drill-flagged">&#9873; Flagged</button>' +
              '<button class="hub-quick-btn" data-hub-tool="drill-unattempted">&#9900; Unattempted</button>' +
            '</div>' +
    '</div>';
  }

  // ---- Full Practice Exams ----
  if (section === 'home' || section === 'exams') {
    var barExams = [];
    for (var b = 0; b < HUB_EXAMS.length; b++) {
      if (HUB_EXAMS[b].group === 'bar') barExams.push(HUB_EXAMS[b]);
    }
    html += '<div class="hub-section">' +
            '<div class="hub-section-title">Full Practice Exams</div>' +
            '<div class="hub-card-grid">';
    for (var c = 0; c < barExams.length; c++) {
      html += hubBuildCard(barExams[c]);
    }
    html += '</div></div>';
  }

  // ---- Professional Responsibility ----
  if (section === 'home' || section === 'pr') {
    var prExams = [];
    for (var p = 0; p < HUB_EXAMS.length; p++) {
      if (HUB_EXAMS[p].group === 'pr') prExams.push(HUB_EXAMS[p]);
    }
    html += '<div class="hub-section">' +
            '<div class="hub-section-title">Professional Responsibility</div>' +
            '<div class="hub-card-grid-sm">';
    for (var q = 0; q < prExams.length; q++) {
      html += hubBuildCard(prExams[q]);
    }
    html += '</div></div>';
  }

  // ---- Study Tools ----
  if (section === 'home') {
    html += '<div class="hub-section">' +
            '<div class="hub-section-title">Study Tools</div>' +
            '<div class="hub-tools-grid">' +
              '<div class="hub-tool-card" data-hub-tool="progress">' +
                '<div class="hub-tool-icon">&#128202;</div>' +
                '<div class="hub-tool-label">Progress Dashboard</div>' +
                '<div class="hub-tool-desc">Session history, accuracy trends, time analysis</div>' +
              '</div>' +
              '<div class="hub-tool-card" data-hub-tool="drill">' +
                '<div class="hub-tool-icon">&#127919;</div>' +
                '<div class="hub-tool-label">Drill Builder</div>' +
                '<div class="hub-tool-desc">Custom drills by subject, chapter, topic, status</div>' +
              '</div>' +
              '<div class="hub-tool-card" data-hub-tool="studyplan">' +
                '<div class="hub-tool-icon">&#129517;</div>' +
                '<div class="hub-tool-label">Study Plan</div>' +
                '<div class="hub-tool-desc">Weak-area ranking, priority scoring, action plan</div>' +
              '</div>' +
            '</div></div>';
  }

  return html;
}

// --- Hub open / close ---
var hubCurrentSection = 'home';

function hubOpen(section) {
  section = section || hubCurrentSection;
  hubCurrentSection = section;
  var hub  = document.getElementById('hub');
  var body = document.getElementById('hub-body');
  if (!hub) return;
  hub.style.display = 'flex';
  if (body) body.innerHTML = hubBuildBody(section);
  // Update nav active state
  var navBtns = document.querySelectorAll('.hub-nav-btn[data-hub-nav]');
  for (var i = 0; i < navBtns.length; i++) {
    var active = navBtns[i].getAttribute('data-hub-nav') === section;
    if (active) navBtns[i].classList.add('hub-nav-active');
    else navBtns[i].classList.remove('hub-nav-active');
  }
  var backBtn = document.getElementById('hub-back-btn');
  if (backBtn) backBtn.style.display = 'none';
}

function hubClose() {
  var hub = document.getElementById('hub');
  if (hub) hub.style.display = 'none';
  var backBtn = document.getElementById('hub-back-btn');
  if (backBtn) backBtn.style.display = 'inline-block';
}

// --- Navigate to exam ---
function hubGoExam(examId) {
  hubClose();
  // Activate tab + panel (same logic as switchExam, no btn ref needed)
  var tabs = document.querySelectorAll('.etab');
  for (var i = 0; i < tabs.length; i++) tabs[i].classList.remove('act');
  var etab = document.querySelector('.etab[data-exam="' + examId + '"]');
  if (etab) etab.classList.add('act');
  var panels = document.querySelectorAll('.epanel');
  for (var j = 0; j < panels.length; j++) panels[j].classList.remove('act');
  var panel = document.getElementById('panel-' + examId);
  if (panel) panel.classList.add('act');
  activeExam = examId;
  buildPanel(examId);
  window.scrollTo(0, 0);
}

function hubGoWrong(examId) {
  hubGoExam(examId);
  setTimeout(function() { anlReviewWrong(examId); }, 80);
}

function hubGoFlagged(examId) {
  hubGoExam(examId);
  setTimeout(function() { anlReviewFlagged(examId); }, 80);
}

// --- Event delegation on hub div ---
document.getElementById('hub').addEventListener('click', function(e) {
  var t = e.target;
  while (t && t !== this) {
    var goId      = t.getAttribute('data-hub-go');
    var wrongId   = t.getAttribute('data-hub-wrong');
    var flagId    = t.getAttribute('data-hub-flagged');
    var navSect   = t.getAttribute('data-hub-nav');
    var toolName  = t.getAttribute('data-hub-tool');

    if (goId)    { hubGoExam(goId); return; }
    if (wrongId) { hubGoWrong(wrongId); return; }
    if (flagId)  { hubGoFlagged(flagId); return; }
    if (navSect) { hubOpen(navSect); return; }
    if (toolName === 'progress')        { hubClose(); anlDashboard(true); return; }
    if (toolName === 'drill')           { hubClose(); buildDrillCatalog(function(){ drillBuilderShow(true); }); return; }
    if (toolName === 'studyplan')       { hubClose(); splShow(true); return; }
    if (toolName === 'drill-weak')      { hubClose(); drillStartPreset('weak'); return; }
    if (toolName === 'drill-wrong')     { hubClose(); drillStartPreset('wrong'); return; }
    if (toolName === 'drill-flagged')   { hubClose(); drillStartPreset('flagged'); return; }
    if (toolName === 'drill-unattempted'){ hubClose(); drillStartPreset('unattempted'); return; }
    t = t.parentElement;
  }
});

// --- Init IIFE: inject back button, open hub on load ---
(function hubInit() {
  var topnav = document.querySelector('.topnav');
  if (topnav) {
    var backBtn = document.createElement('button');
    backBtn.id = 'hub-back-btn';
    backBtn.innerHTML = '← Hub';
    backBtn.title = 'Back to Bar Exam Hub';
    backBtn.addEventListener('click', function() {
      hubOpen(hubCurrentSection);
    });
    topnav.insertBefore(backBtn, topnav.firstChild);
  }
  hubOpen('home');
})();

})(); // end Phase 3UI IIFE
"""

# ============================================================
# APPLY PATCHES
# ============================================================
def patch():
    print('Phase 3UI patch starting...')
    with open(INDEX, 'r', encoding='utf-8') as f:
        html = f.read()

    # Safety: ensure markers exist
    STYLE_MARKER = '</style>'
    BODY_MARKER  = '</body>'
    JS_MARKER    = "buildPanel('bar');"

    if STYLE_MARKER not in html:
        print('ERROR: </style> not found'); sys.exit(1)
    if BODY_MARKER not in html:
        print('ERROR: </body> not found'); sys.exit(1)
    if JS_MARKER not in html:
        print("ERROR: buildPanel('bar'); not found"); sys.exit(1)

    # Already patched guard
    if 'Phase 3UI' in html:
        print('WARNING: Phase 3UI markers already present — aborting to avoid double-patch.'); sys.exit(0)

    # 1. CSS before first </style>
    idx = html.index(STYLE_MARKER)
    html = html[:idx] + UI_CSS + '\n' + html[idx:]
    print('  [1] CSS injected ({} chars)'.format(len(UI_CSS)))

    # 2. HTML before last </body>
    idx = html.rindex(BODY_MARKER)
    html = html[:idx] + UI_HTML + '\n' + html[idx:]
    print('  [2] HTML injected ({} chars)'.format(len(UI_HTML)))

    # 3. JS before first buildPanel('bar');
    idx = html.index(JS_MARKER)
    html = html[:idx] + UI_JS + '\n' + html[idx:]
    print('  [3] JS injected ({} chars)'.format(len(UI_JS)))

    with open(INDEX, 'w', encoding='utf-8') as f:
        f.write(html)

    size = os.path.getsize(INDEX)
    print('  index.html written — {:.1f} KB ({:,} bytes)'.format(size / 1024, size))
    print('Phase 3UI patch complete.')

if __name__ == '__main__':
    patch()
