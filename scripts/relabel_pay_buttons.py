#!/usr/bin/env python3
"""
Replace Apple Pay / Google Pay decorative buttons with honest 'Reserve by
card' and 'Reserve by wire' buttons. Cleaner for the luxury-rental flow
and avoids the awkward 'click Apple Pay → no Apple Pay sheet' demo gotcha.
"""
import re
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


def replacement(slug: str) -> str:
    return f'''<button type="button" class="pay-btn" aria-label="Reserve with card deposit" onclick="window.location.href='../index.html?car={slug}#reserve'">
          <svg width="18" height="14" viewBox="0 0 24 18" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">
            <rect x="2" y="3" width="20" height="14" rx="2"/><path d="M2 8h20M6 13h4"/>
          </svg>
          <span style="font-weight:500;">Reserve · card deposit</span>
        </button>
        <button type="button" class="pay-btn" aria-label="Reserve by wire transfer" onclick="window.location.href='../index.html?car={slug}#reserve'">
          <svg width="18" height="14" viewBox="0 0 24 18" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">
            <path d="M3 14V8l9-5 9 5v6"/><path d="M3 14h18"/><path d="M7 14V9M11 14V9M15 14V9M19 14V9"/>
          </svg>
          <span style="font-weight:500;">Reserve · by wire</span>
        </button>'''


# We want to find both buttons (Apple + Google) and replace them with our two.
PATTERN = re.compile(
    r'<button type="button" class="pay-btn" aria-label="Pay with Apple Pay"[\s\S]*?</button>\s*'
    r'<button type="button" class="pay-btn" aria-label="Pay with Google Pay"[\s\S]*?</button>',
    re.MULTILINE,
)


def main():
    for filename, slug in SLUGS.items():
        path = FLEET / filename
        text = path.read_text()
        new = PATTERN.sub(replacement(slug), text, count=1)
        if new == text:
            print(f"  · {filename}: pattern not found (already replaced?)")
            continue
        path.write_text(new)
        print(f"  ✓ {filename}")


if __name__ == "__main__":
    main()
