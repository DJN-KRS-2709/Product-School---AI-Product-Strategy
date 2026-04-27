"""Generate the Course Arc slide HTML per module.

Used once to replace the Syllabus slide across all 6 modules. Kept in
the repo so future modules can be regenerated in the same shape.
"""

from __future__ import annotations

MODULES = [
    {"n": 1, "name": "The Bet",        "color": "59,130,246",  "hex": "#3b82f6"},
    {"n": 2, "name": "The Moat",       "color": "59,130,246",  "hex": "#3b82f6"},
    {"n": 3, "name": "The Margin",     "color": "210,153,34",  "hex": "#d29922"},
    {"n": 4, "name": "The Contract",   "color": "188,140,255", "hex": "#bc8cff"},
    {"n": 5, "name": "The Guardrails", "color": "248,81,73",   "hex": "#f85149"},
    {"n": 6, "name": "The Pitch",      "color": "57,210,192",  "hex": "#39d2c0"},
]


def node(mod: dict, active_n: int) -> str:
    is_active = mod["n"] == active_n
    if is_active:
        style = (
            f'background:rgba({mod["color"]},0.2); '
            f'border:2px solid {mod["hex"]};'
        )
        cls = "arc-node active-node"
        label_op = "0.6"
    else:
        style = (
            f'background:rgba({mod["color"]},0.08); '
            f'border:1px solid rgba({mod["color"]},0.2);'
        )
        cls = "arc-node"
        label_op = "0.5"
    return (
        f'      <div class="{cls}" style="{style}">'
        f'<div style="font-size:10px; opacity:{label_op};">M{mod["n"]}</div>'
        f'{mod["name"]}</div>'
    )


def arc_html(active_n: int) -> str:
    nodes = []
    for i, mod in enumerate(MODULES):
        nodes.append(node(mod, active_n))
        if i < len(MODULES) - 1:
            nodes.append('      <div class="arc-arrow">→</div>')
    active = next(m for m in MODULES if m["n"] == active_n)
    return (
        f'<!-- 3: Course Arc -->\n'
        f'<section class="centered" data-title="Course Arc">\n'
        f'  <div class="inner">\n'
        f'    <div class="section-label">The Course Arc</div>\n'
        f'    <h2>Six Questions. One Living Strategy.</h2>\n'
        f'    <div class="arc-flow">\n'
        + "\n".join(nodes) + "\n"
        f'    </div>\n'
        f'    <div class="artifact-preview" style="max-width:640px; margin:20px auto;">\n'
        f'      <div class="ap-title">Your Living Strategy — A Repo You Build Across 6 Sessions</div>\n'
        f'      <p style="font-size:15px; color:#8899bb; line-height:1.5;">Not a doc. Not a slide deck. A <strong>GitHub repo</strong> — version-controlled, shareable, alive. One component per module. <strong>Today → Component {active_n}: {active["name"]}.</strong></p>\n'
        f'    </div>\n'
        f'  </div>\n'
        f'</section>'
    )


if __name__ == "__main__":
    for mod in MODULES:
        print(f"\n========== MODULE {mod['n']} ==========\n")
        print(arc_html(mod["n"]))
