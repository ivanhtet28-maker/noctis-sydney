#!/usr/bin/env python3
"""
Inject the brand swap scripts (brands.js + noctis-brand.js) into every
HTML page just before </body>. Idempotent — won't double-inject.
"""
from pathlib import Path

ROOT = Path(__file__).parent.parent

PAGES = [
    (ROOT / "index.html",                              "assets"),
    (ROOT / "fleet" / "rolls-royce-spectre.html",      "../assets"),
    (ROOT / "fleet" / "aston-martin-db12.html",        "../assets"),
    (ROOT / "fleet" / "mclaren-750s.html",             "../assets"),
    (ROOT / "fleet" / "ferrari-purosangue.html",       "../assets"),
    (ROOT / "fleet" / "mercedes-g63.html",             "../assets"),
    (ROOT / "fleet" / "porsche-911-gt3.html",          "../assets"),
    (ROOT / "journal" / "index.html",                  "../assets"),
    (ROOT / "journal" / "db12-harbour-bridge.html",    "../assets"),
    (ROOT / "journal" / "breakfast-drives.html",       "../assets"),
    (ROOT / "journal" / "badges-come-off.html",        "../assets"),
    (ROOT / "legal" / "privacy.html",                  "../assets"),
    (ROOT / "legal" / "terms.html",                    "../assets"),
    (ROOT / "legal" / "responsible-driving.html",      "../assets"),
    (ROOT / "crm" / "index.html",                      "../assets"),
]

MARKER = "<!-- noctis-brand -->"


def inject(path: Path, prefix: str) -> str:
    text = path.read_text()
    if MARKER in text:
        return "skip (already injected)"

    block = (
        f'\n{MARKER}\n'
        f'<script src="{prefix}/brands.js" defer></script>\n'
        f'<script src="{prefix}/noctis-brand.js" defer></script>\n'
    )

    if "</body>" not in text:
        return "no </body> tag"

    text = text.replace("</body>", block + "</body>", 1)
    path.write_text(text)
    return "ok"


def main():
    for path, prefix in PAGES:
        if not path.exists():
            print(f"  ✗ {path.relative_to(ROOT)}: missing")
            continue
        result = inject(path, prefix)
        marker = "✓" if result == "ok" else "·"
        print(f"  {marker} {path.relative_to(ROOT)} — {result}")


if __name__ == "__main__":
    main()
