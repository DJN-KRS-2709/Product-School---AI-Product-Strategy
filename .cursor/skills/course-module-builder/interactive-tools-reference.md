# Interactive Tool Patterns

Interactive tools are self-contained HTML files linked from slides. Students open them in-class and their work persists via `localStorage`.

## Common Tool Types

### Scorecard (e.g., M1 - Vulnerability Scorecard)
- Multiple scoring axes with slider or segmented-button inputs (1–5 scale)
- Auto-calculated composite score with color-coded result
- Text input for qualitative notes (e.g., "weakest competitor")
- Visual bar indicators per axis

### Calculator (e.g., M3 - Margin Calculator)
- Input fields for cost parameters (inference cost, volume, caching rate, etc.)
- Live-updating calculations showing margins, break-even, stress scenarios
- Sliders for scenario exploration ("what if inference costs 3x?")
- Before/after comparison (old SaaS vs. AI usage revenue)

### Audit (e.g., M5 - Shadow AI Audit)
- Multi-step workflow: Discovery → Risk scoring → Decision
- Table-based tool entry with risk tier assignment (L/M/H/Critical)
- Triage action per tool: Keep, Replace, Ban
- Exportable results as markdown

### Builder (e.g., M4 - Golden Dataset Builder)
- Multi-panel layout for filling in structured artifacts
- Named sections matching the framework from lecture
- Fill-in fields with placeholder prompts
- Output assembled into a structured document

### Checklist (e.g., M4 - Confidence UX Checklist)
- Categorized items with Y/N or score toggles
- Coverage percentage per category
- Gap identification based on unchecked items

### Positioning Map (e.g., M2 - Positioning Map)
- Two-axis canvas with draggable company dots
- Label inputs for axis names
- Visual quadrant layout

## Design System

Tools use a darker variant of the slide theme:

| Token | Value |
|-------|-------|
| Background | `#0b0b10` |
| Surface | `#13131a` |
| Surface 2 | `#1a1a24` |
| Border | `#252535` |
| Border highlight | `#35354a` |
| Text | `#e0e0f0` |
| Text dim | `#7a7a9a` |
| Blue accent | `#5b8def` |
| Green | `#3dd68c` |
| Yellow | `#f0c040` |
| Red | `#ef5b5b` |
| Purple | `#a07be8` |
| Font | `DM Sans` (body), `JetBrains Mono` (scores/data) |

## Shared Behaviors

Every interactive tool must include:

1. **localStorage persistence**: Auto-save on input change with debounce (~450ms). Load on page open.
   ```javascript
   const KEY = 'mN-tool-name';
   function save() { localStorage.setItem(KEY, JSON.stringify(getData())); }
   function load() { const d = JSON.parse(localStorage.getItem(KEY) || 'null'); if (d) applyData(d); }
   ```

2. **Export as markdown**: Download button that generates a `.md` file with structured output.
   ```javascript
   function exportMd() {
     const blob = new Blob([buildExportBody()], { type: 'text/markdown' });
     const a = document.createElement('a');
     a.href = URL.createObjectURL(blob);
     a.download = 'mN-tool-name.md';
     a.click();
     URL.revokeObjectURL(a.href);
   }
   ```

3. **Auto-save toast**: Brief "Auto-saved" notification on save.

4. **Reset button**: Clear localStorage and reload (with confirmation).

5. **Responsive layout**: Works on laptop screens (720px max-width centered page).

## File Naming

`M{N} - {Tool Name}.html` — e.g., `M2 - Flywheel Scorer.html`

## Linking from Slides

Tools are linked from their corresponding slide using a `.bottom-cta` bar:
```html
<div class="bottom-cta">
  Open the tool: <a href="M2 - Flywheel Scorer.html" target="_blank">Flywheel Scorer →</a>
</div>
```
