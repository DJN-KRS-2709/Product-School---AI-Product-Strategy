# HTML Slide Deck Template

Every slide deck is a **single self-contained HTML file**. No build tools, no bundler, no external JS. Just open in a browser.

## Skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Module N: Title — Subtitle</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700;900&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&display=swap');

  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { height: 100%; overflow: hidden; background: #07162C; }
  body { font-family: 'Lato', -apple-system, sans-serif; color: #e8e8f0; -webkit-font-smoothing: antialiased; }
  h1, h2 { font-family: 'Poppins', sans-serif; }

  /* --- Slide container --- */
  .slide { position: absolute; inset: 0; display: none; flex-direction: column; justify-content: center; align-items: center; padding: 60px 80px; opacity: 0; transition: opacity 0.35s ease; }
  .slide.active { display: flex; opacity: 1; }
  .slide-inner { max-width: 960px; width: 100%; }

  /* --- Typography --- */
  .module-tag { font-size: 12px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: #1241B0; margin-bottom: 16px; }
  h1 { font-size: 48px; font-weight: 900; line-height: 1.1; color: #fff; margin-bottom: 20px; }
  h2 { font-size: 38px; font-weight: 800; line-height: 1.15; color: #fff; margin-bottom: 18px; }
  .subtitle { font-size: 18px; font-weight: 400; color: #8899bb; line-height: 1.6; margin-bottom: 28px; max-width: 720px; }
  p, li { font-size: 18px; color: #b0b4c8; line-height: 1.7; }
  strong { color: #fff; font-weight: 700; }
  em { color: #60a5fa; font-style: normal; font-weight: 600; }

  /* --- Slide type tags --- */
  .demo-tag { display: inline-block; font-size: 11px; font-weight: 800; letter-spacing: 0.12em; text-transform: uppercase; padding: 6px 16px; border-radius: 6px; margin-bottom: 18px; }
  .tag-provocation { background: rgba(248,113,113,0.12); color: #fca5a5; }
  .tag-lecture { background: rgba(96,165,250,0.12); color: #93c5fd; }
  .tag-case { background: rgba(251,191,36,0.12); color: #fde68a; }
  .tag-exercise { background: rgba(52,211,153,0.12); color: #6ee7b7; }
  .tag-activity { background: rgba(192,132,252,0.12); color: #d8b4fe; }
  .tag-build { background: rgba(244,114,182,0.12); color: #f9a8d4; }
  .tag-break { background: rgba(100,116,139,0.12); color: #94a3b8; }
  .tag-recall { background: rgba(59,130,246,0.12); color: #93c5fd; }
  .tag-framework { background: rgba(251,191,36,0.12); color: #fde68a; }

  /* (Paste remaining CSS classes from any Module N - Slides.html) */

  /* --- Navigation chrome --- */
  .nav { position: fixed; bottom: 20px; right: 24px; display: flex; gap: 8px; z-index: 100; }
  .nav-btn { width: 42px; height: 42px; border-radius: 8px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.1); color: #888; font-size: 18px; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.2s; font-family: 'Lato', sans-serif; }
  .nav-btn:hover { background: rgba(255,255,255,0.1); color: #fff; }
  .progress { position: fixed; bottom: 0; left: 0; right: 0; height: 3px; background: rgba(255,255,255,0.05); z-index: 100; }
  .progress-bar { height: 100%; background: #1241B0; transition: width 0.35s ease; }
  .slide-counter { position: fixed; bottom: 26px; left: 24px; font-size: 13px; font-weight: 600; color: #444; z-index: 100; }
  .help-hint { position: fixed; top: 16px; right: 24px; font-size: 11px; color: #333; z-index: 100; }
  .speaker-notes { display: none; position: fixed; bottom: 0; left: 0; right: 0; background: #1a1a24; border-top: 2px solid #1241B0; padding: 16px 32px; max-height: 200px; overflow-y: auto; font-size: 14px; color: #8899bb; line-height: 1.6; z-index: 200; }
  .speaker-notes.visible { display: block; }
  .notes-tag { font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #1241B0; margin-bottom: 6px; }
</style>
</head>
<body>

<!-- ===== SLIDE 1: Title ===== -->
<div class="slide active" data-notes="Brief speaker note for this slide.">
  <div class="slide-inner">
    <div class="module-tag">Module N | Course Name</div>
    <h1>Module Title</h1>
    <h2 style="font-size:30px; font-weight:600; color:#8899bb;">Subtitle / Strategic Question</h2>
    <div class="waypoints">
      <div class="waypoint"><div class="waypoint-num">1</div><div class="waypoint-text"><div class="wt-title">Waypoint 1</div><div class="wt-desc">Description</div></div></div>
      <div class="waypoint"><div class="waypoint-num">2</div><div class="waypoint-text"><div class="wt-title">Waypoint 2</div><div class="wt-desc">Description</div></div></div>
      <div class="waypoint"><div class="waypoint-num">3</div><div class="waypoint-text"><div class="wt-title">Waypoint 3</div><div class="wt-desc">Description</div></div></div>
    </div>
  </div>
</div>

<!-- ===== SLIDE 2: ... ===== -->
<!-- Add more slides here. Each is a <div class="slide" data-notes="..."> -->

<!-- ===== UI CHROME ===== -->
<div class="nav">
  <button class="nav-btn" onclick="prev()" title="Previous (←)">‹</button>
  <button class="nav-btn" onclick="next()" title="Next (→)">›</button>
</div>
<div class="slide-counter"><span id="current">1</span> / <span id="total">1</span></div>
<div class="progress"><div class="progress-bar" id="progress-bar"></div></div>
<div class="help-hint">← → navigate · S speaker notes · F fullscreen</div>
<div class="speaker-notes" id="speaker-notes">
  <div class="notes-tag">Speaker Notes</div>
  <div id="notes-content"></div>
</div>

<script>
  const slides = document.querySelectorAll('.slide');
  const total = slides.length;
  let current = 0;
  let notesVisible = false;

  function show(idx) {
    slides.forEach((s, i) => { s.classList.toggle('active', i === idx); });
    current = idx;
    document.getElementById('current').textContent = idx + 1;
    document.getElementById('total').textContent = total;
    document.getElementById('progress-bar').style.width = ((idx + 1) / total * 100) + '%';
    const notes = slides[idx].getAttribute('data-notes') || '';
    document.getElementById('notes-content').innerHTML = notes || '<em style="color:#444;">No notes for this slide.</em>';
  }

  function next() { if (current < total - 1) show(current + 1); }
  function prev() { if (current > 0) show(current - 1); }

  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); next(); }
    else if (e.key === 'ArrowLeft') { e.preventDefault(); prev(); }
    else if (e.key === 's' || e.key === 'S') {
      notesVisible = !notesVisible;
      document.getElementById('speaker-notes').classList.toggle('visible', notesVisible);
    }
    else if (e.key === 'f' || e.key === 'F') {
      if (!document.fullscreenElement) document.documentElement.requestFullscreen();
      else document.exitFullscreen();
    }
  });

  let touchStartX = 0;
  document.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; });
  document.addEventListener('touchend', e => {
    const diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 60) { diff > 0 ? next() : prev(); }
  });

  show(0);
</script>
</body>
</html>
```

## Design System

| Token | Value | Usage |
|-------|-------|-------|
| Background | `#07162C` | Body / slide background |
| Surface | `#0c2340` | Cards, panels |
| Border | `#1a3a5c` | Card borders |
| Accent | `#1241B0` | Module tag, progress bar, active elements |
| Heading | `#fff` | h1, h2, strong |
| Body text | `#b0b4c8` | Paragraphs, list items |
| Subtle text | `#8899bb` | Subtitles, descriptions |
| Emphasis | `#60a5fa` | `<em>` tags (blue, not italic) |
| Heading font | `Poppins` | h1, h2 |
| Body font | `Lato` | Everything else |
| Mono font | `IBM Plex Mono` | Agenda times, code |
| Exercise mono | `JetBrains Mono` | Fill-in blanks |

## Common Slide Patterns

### Title slide
Module tag + h1 + subtitle + waypoints (3 numbered goals for the session).

### Provocation slide (True/False)
Tag: `.tag-provocation`. Grid of 3 claims, all FALSE, with `.tf-grid` / `.tf-item` / `.tf-verdict`. Each has a claim + short explanation.

### Case study slide (3-act)
Three cards side by side: `.act-bet` (blue), `.act-crack` (yellow), `.act-correct` (green). Lead with the big number. Minimal text.

### Exercise / build slide (split layout)
`.split-slide` with `.split-left` (context + goal) and `.split-right` (numbered steps). Lab badge + timer in header. Goal box at bottom-left. Tool link as `.bottom-cta`.

### Agenda slide
`.agenda` container with `.agenda-item` rows: `.agenda-time` (mono, blue) + `.agenda-text`.

### Recall slide
Tag: `.tag-recall`. Waypoints with green checkmark icons showing what students brought from the previous module.

### Syllabus slide
`.syllabus-grid` (2-column) with `.syllabus-card` items. Current module gets `.syl-active`.

### Debrief / pair prompt
`.debrief-box` with centered prompt text and subtitle.

### Synthesis / completion slide
`.complete-stats` (big numbers) + `.complete-shifts` (before → after cards) + bridge to next module.

## Key Rules

1. Every slide is a `<div class="slide" data-notes="...">` — the `data-notes` attribute holds brief inline speaker notes
2. First slide gets `class="slide active"`
3. Navigation, progress bar, and speaker notes toggle are always at the bottom (copy the UI chrome block)
4. Copy the full CSS from an existing module — it's stable and shared across all decks
5. Update `<span id="total">` to match the number of slides (or rely on the JS which auto-counts)
