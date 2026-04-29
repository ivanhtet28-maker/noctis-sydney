#!/usr/bin/env python3
"""Inject the Noctis chat widget script tag before </body> on every HTML page."""
from pathlib import Path

ROOT = Path(__file__).parent.parent

PAGES = [
    (ROOT / "index.html",                              "assets/noctis-chat.js"),
    (ROOT / "fleet" / "rolls-royce-spectre.html",      "../assets/noctis-chat.js"),
    (ROOT / "fleet" / "aston-martin-db12.html",        "../assets/noctis-chat.js"),
    (ROOT / "fleet" / "mclaren-750s.html",             "../assets/noctis-chat.js"),
    (ROOT / "fleet" / "ferrari-purosangue.html",       "../assets/noctis-chat.js"),
    (ROOT / "fleet" / "mercedes-g63.html",             "../assets/noctis-chat.js"),
    (ROOT / "fleet" / "porsche-911-gt3.html",          "../assets/noctis-chat.js"),
    (ROOT / "journal" / "index.html",                  "../assets/noctis-chat.js"),
    (ROOT / "journal" / "db12-harbour-bridge.html",    "../assets/noctis-chat.js"),
    (ROOT / "journal" / "breakfast-drives.html",       "../assets/noctis-chat.js"),
    (ROOT / "journal" / "badges-come-off.html",        "../assets/noctis-chat.js"),
    (ROOT / "legal" / "privacy.html",                  "../assets/noctis-chat.js"),
    (ROOT / "legal" / "terms.html",                    "../assets/noctis-chat.js"),
    (ROOT / "legal" / "responsible-driving.html",      "../assets/noctis-chat.js"),
]

MARKER = "<!-- noctis-chat -->"


def inject(path: Path, src: str) -> str:
    text = path.read_text()
    if MARKER in text:
        return "skip (already injected)"

    tag = f'\n{MARKER}\n<script src="{src}" defer></script>\n'

    if "</body>" not in text:
        return "no </body> tag"

    text = text.replace("</body>", tag + "</body>", 1)
    path.write_text(text)
    return "ok"


def main():
    for path, src in PAGES:
        if not path.exists():
            print(f"  ✗ {path.name}: missing")
            continue
        result = inject(path, src)
        print(f"  {'✓' if result == 'ok' else '·'} {path.relative_to(ROOT)} — {result}")


if __name__ == "__main__":
    main()
