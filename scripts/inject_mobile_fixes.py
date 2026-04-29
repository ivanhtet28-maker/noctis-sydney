#!/usr/bin/env python3
"""
Inject mobile-friendly CSS adjustments into fleet pages and homepage:
- Shift background-position on gallery & cards so cars stay in frame on mobile
- Darken the top of the booking-gallery main image (residual Miami skyline)
- Tighten heading sizes on small screens
- Ensure recent gallery / booking layout stacks gracefully
"""
from pathlib import Path

ROOT = Path(__file__).parent.parent

FLEET_FILES = [
    ROOT / "fleet" / "rolls-royce-spectre.html",
    ROOT / "fleet" / "aston-martin-db12.html",
    ROOT / "fleet" / "mclaren-750s.html",
    ROOT / "fleet" / "ferrari-purosangue.html",
    ROOT / "fleet" / "mercedes-g63.html",
    ROOT / "fleet" / "porsche-911-gt3.html",
]

HOMEPAGE = ROOT / "index.html"

MARKER_OPEN = "/* INJECTED:mobile-fixes START */"
MARKER_CLOSE = "/* INJECTED:mobile-fixes END */"

FLEET_CSS = """
""" + MARKER_OPEN + """
/* Cars are now re-cropped so they sit in the vertical centre of every
   image — using default `background-position: center` keeps the car
   in frame on every device. */
.gallery-main, .booking-gallery .gallery-main {
  background-position: center !important;
}
.gallery-thumb { background-position: center !important; }
.recent-img { background-position: center !important; }

/* Tighten the H1 and breadcrumb on small screens */
@media (max-width: 600px) {
  .crumb { font-size: 11px !important; }
  .car-title { font-size: clamp(40px, 11vw, 64px) !important; line-height: 1.0 !important; }
  .booking-section { padding-top: 24px !important; }
  .booking-card { padding: 22px !important; }
  .vehicle-details .cards { grid-template-columns: 1fr !important; gap: 12px !important; }
  .spec-strip { grid-template-columns: repeat(2, 1fr) !important; }
  .recent-section { padding: 56px 0 40px !important; }
  .recent-section h2 { font-size: clamp(28px, 8vw, 40px) !important; }
  .recent-grid { gap: 6px !important; }
  .social-section { padding: 56px 0 64px !important; }
}

/* iPad portrait — keep gallery prominent without full-width sidebar bumping */
@media (min-width: 600px) and (max-width: 959px) {
  .booking-grid { gap: 36px !important; }
  .booking-card { padding: 28px !important; }
}

/* Avoid horizontal overflow on description blocks */
.description-block, .vehicle-details, .spec-strip, .booking-grid { max-width: 100%; overflow-wrap: anywhere; }
""" + MARKER_CLOSE + """
"""

HOMEPAGE_CSS = """
""" + MARKER_OPEN + """
/* Mobile image friendliness — shift focus, dim top gradients more on
   small screens, prevent horizontal overflow. */
@media (max-width: 768px) {
  .car-photo { background-position: center !important; }
  .car-card { aspect-ratio: 5/6 !important; }   /* slightly less tall on mobile */
}

/* The Sydney hero — favor middle of image (bridge + opera) on portrait */
@media (max-width: 600px) {
  #top > div[style*="background-image"] {
    background-position: 60% 45% !important;
  }
}
""" + MARKER_CLOSE + """
"""


def apply(path: Path, css_block: str) -> str:
    text = path.read_text()
    if MARKER_OPEN in text:
        # Replace existing block
        a = text.index(MARKER_OPEN)
        b = text.index(MARKER_CLOSE) + len(MARKER_CLOSE)
        text = text[:a] + css_block.strip() + text[b:]
        path.write_text(text)
        return "replaced"

    # Insert just before the closing </style>
    if "</style>" not in text:
        return "no </style> found"
    text = text.replace("</style>", css_block + "\n</style>", 1)
    path.write_text(text)
    return "inserted"


def main():
    for path in FLEET_FILES:
        if not path.exists():
            print(f"  ✗ {path.relative_to(ROOT)}: missing")
            continue
        result = apply(path, FLEET_CSS)
        print(f"  ✓ {path.relative_to(ROOT)} — {result}")

    if HOMEPAGE.exists():
        result = apply(HOMEPAGE, HOMEPAGE_CSS)
        print(f"  ✓ index.html — {result}")


if __name__ == "__main__":
    main()
