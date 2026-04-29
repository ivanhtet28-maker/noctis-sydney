#!/usr/bin/env python3
"""
Append a 'Recent' photo grid + social-follow section to each fleet page,
just before the FOOTER block. Skips files that already have the markers.
"""
from pathlib import Path

ROOT = Path(__file__).parent.parent
FLEET = ROOT / "fleet"

SLUGS = {
    "rolls-royce-spectre.html": "spectre",
    "aston-martin-db12.html":   "db12",
    "mclaren-750s.html":        "750s",
    "ferrari-purosangue.html":  "purosangue",
    "mercedes-g63.html":        "g63",
    "porsche-911-gt3.html":     "911",
}

# A short caption for each of the 4 supplementary images per car (Sydney locations).
LOCATIONS = [
    ("West Head Road", "Sat 11:42"),
    ("Walsh Bay workshop", "Mon 06:18"),
    ("Mona Vale → Palm Beach", "Sat 07:05"),
    ("Mosman, returning", "Tue 21:14"),
]

# The new sections — anchored to a single marker comment so it can be re-run idempotently.
MARKER_OPEN = "<!-- INJECTED:recent-social START -->"
MARKER_CLOSE = "<!-- INJECTED:recent-social END -->"


def block_for_slug(slug: str) -> str:
    cards = ""
    for i, (place, when) in enumerate(LOCATIONS, start=1):
        cards += f"""
        <figure class="recent-card">
          <div class="recent-img" style="background-image:url('../images/{slug}-{i}.jpg');"></div>
          <figcaption>
            <span class="recent-place">{place}</span>
            <span class="recent-when">{when}</span>
          </figcaption>
        </figure>"""

    return f"""{MARKER_OPEN}
<style>
.recent-section {{ padding: 96px 0 64px; border-top: 1px solid var(--line); }}
.recent-section .recent-head {{ display:flex; flex-wrap:wrap; align-items:flex-end; justify-content:space-between; gap:24px; margin-bottom:48px; }}
.recent-section h2 {{ font-family:'Fraunces', serif; font-size:clamp(32px, 4.5vw, 52px); line-height:1.05; letter-spacing:-0.028em; margin:0; color:var(--cream); }}
.recent-section h2 em {{ font-style:italic; font-weight:300; }}
.recent-section .recent-sub {{ color:rgba(245,241,234,0.55); font-size:14px; max-width:42ch; margin:8px 0 0; }}
.recent-section .recent-cta {{ color:rgba(245,241,234,0.85); border-bottom:1px solid rgba(245,241,234,0.35); padding-bottom:4px; text-decoration:none; font-size:13px; letter-spacing:0.08em; text-transform:uppercase; transition:border-color .3s; }}
.recent-section .recent-cta:hover {{ border-color:var(--cream); }}

.recent-grid {{ display:grid; grid-template-columns:repeat(4, 1fr); gap:8px; }}
.recent-card {{ position:relative; margin:0; overflow:hidden; aspect-ratio: 1 / 1; background:var(--surface); border:1px solid var(--line); }}
.recent-img {{ position:absolute; inset:0; background-size:cover; background-position:center; transition:transform 800ms cubic-bezier(0.22, 1, 0.36, 1); }}
.recent-card:hover .recent-img {{ transform:scale(1.04); }}
.recent-card figcaption {{ position:absolute; left:0; right:0; bottom:0; padding:14px 16px 12px; background:linear-gradient(to top, rgba(10,10,10,0.92), rgba(10,10,10,0)); display:flex; justify-content:space-between; align-items:flex-end; gap:8px; font-size:11px; letter-spacing:0.04em; }}
.recent-card .recent-place {{ color:var(--cream); font-weight:500; }}
.recent-card .recent-when {{ color:rgba(245,241,234,0.55); font-variant-numeric:tabular-nums; }}

@media (max-width: 900px) {{
  .recent-grid {{ grid-template-columns:repeat(2, 1fr); }}
}}
@media (max-width: 480px) {{
  .recent-section {{ padding: 64px 0 48px; }}
}}

.social-section {{ padding: 80px 0 96px; border-top:1px solid var(--line); }}
.social-row {{ display:grid; grid-template-columns:1fr; gap:48px; align-items:center; }}
@media (min-width:768px) {{ .social-row {{ grid-template-columns:1.4fr 1fr; gap:64px; }} }}
.social-row h2 {{ font-family:'Fraunces', serif; font-size:clamp(28px, 3.8vw, 42px); line-height:1.1; letter-spacing:-0.024em; margin:0; color:var(--cream); }}
.social-row h2 em {{ font-style:italic; font-weight:300; }}
.social-row p {{ color:rgba(245,241,234,0.6); font-size:15px; line-height:1.6; max-width:46ch; margin:16px 0 0; }}
.social-handles {{ list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:14px; }}
.social-handles a {{ display:flex; align-items:center; gap:14px; padding:18px 22px; border:1px solid var(--line); border-radius:6px; color:var(--cream); text-decoration:none; transition:border-color .25s, background .25s; }}
.social-handles a:hover {{ border-color:rgba(245,241,234,0.4); background:rgba(245,241,234,0.02); }}
.social-handles svg {{ flex-shrink:0; }}
.social-handles .label {{ font-size:13px; color:var(--muted); letter-spacing:0.08em; text-transform:uppercase; }}
.social-handles .handle {{ font-family:'Fraunces', serif; font-size:18px; letter-spacing:-0.018em; color:var(--cream); margin-top:2px; }}
.social-handles .arrow {{ margin-left:auto; color:var(--muted); font-size:18px; line-height:1; }}
</style>

<!-- ===== Recent ===== -->
<section class="recent-section">
  <div class="container">
    <div class="recent-head">
      <div>
        <p class="eyebrow" style="margin:0 0 16px;">Out lately</p>
        <h2>Recently <em>photographed.</em></h2>
        <p class="recent-sub">A handful of moments from the last fortnight, captured by drivers and guests on the way somewhere.</p>
      </div>
      <a href="https://instagram.com/noctis.sydney" class="recent-cta" target="_blank" rel="noopener">Follow on Instagram &nbsp;→</a>
    </div>
    <div class="recent-grid">{cards}
    </div>
  </div>
</section>

<!-- ===== Social ===== -->
<section class="social-section">
  <div class="container">
    <div class="social-row">
      <div>
        <p class="eyebrow" style="margin:0 0 16px;">Quietly online</p>
        <h2>One handle. <em>Three places.</em></h2>
        <p>We post sparingly — maybe four times a month. Every photograph is from a real delivery somewhere on our roads. No paid promotion, no influencer trips. If you enjoyed this car, you will probably enjoy our feed.</p>
      </div>
      <ul class="social-handles">
        <li>
          <a href="https://instagram.com/noctis.sydney" target="_blank" rel="noopener" aria-label="Instagram">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">
              <rect x="3" y="3" width="18" height="18" rx="5" ry="5"/>
              <circle cx="12" cy="12" r="4"/>
              <circle cx="17.5" cy="6.5" r="0.6" fill="currentColor"/>
            </svg>
            <div>
              <span class="label">Instagram</span>
              <div class="handle">@noctis.sydney</div>
            </div>
            <span class="arrow">›</span>
          </a>
        </li>
        <li>
          <a href="https://au.pinterest.com/noctissydney/" target="_blank" rel="noopener" aria-label="Pinterest">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">
              <circle cx="12" cy="12" r="9"/>
              <path d="M11 7c2.5 0 4 1.5 4 4s-1.5 4-3.5 4c-0.5 0-1-0.2-1.4-0.5M10.5 11l-1.5 6"/>
            </svg>
            <div>
              <span class="label">Pinterest</span>
              <div class="handle">noctissydney</div>
            </div>
            <span class="arrow">›</span>
          </a>
        </li>
        <li>
          <a href="https://signal.me/#noctis" aria-label="Signal">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">
              <path d="M21 11.5a8.4 8.4 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.4 8.4 0 0 1-3.8-.9L3 21l1.9-5.7a8.4 8.4 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.4 8.4 0 0 1 3.8-.9h.5a8.5 8.5 0 0 1 8 8v.5z"/>
            </svg>
            <div>
              <span class="label">Signal</span>
              <div class="handle">@noctis.sydney</div>
            </div>
            <span class="arrow">›</span>
          </a>
        </li>
      </ul>
    </div>
  </div>
</section>
{MARKER_CLOSE}

"""


def main():
    anchor = "<!-- FOOTER -->"
    for filename, slug in SLUGS.items():
        path = FLEET / filename
        text = path.read_text()
        if MARKER_OPEN in text:
            # Replace existing block (idempotent)
            start = text.index(MARKER_OPEN)
            end = text.index(MARKER_CLOSE) + len(MARKER_CLOSE)
            text = text[:start] + block_for_slug(slug).rstrip() + text[end:]
            path.write_text(text)
            print(f"  ↻ {filename} (replaced existing block)")
            continue

        if anchor not in text:
            print(f"  ✗ {filename}: no '<!-- FOOTER -->' anchor found")
            continue

        new_text = text.replace(anchor, block_for_slug(slug) + anchor, 1)
        path.write_text(new_text)
        print(f"  ✓ {filename}")


if __name__ == "__main__":
    main()
