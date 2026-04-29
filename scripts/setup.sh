#!/usr/bin/env bash
# =============================================================
# Noctis — one-time Nano Banana 2 setup
# Installs Bun (if missing), clones the nano-banana-2 skill repo,
# links the CLI globally, and prompts for your Gemini API key.
#
# Run once:
#   bash scripts/setup.sh
# =============================================================
set -e

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Nano Banana 2 — one-time setup"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 1. Install Bun if missing
if ! command -v bun >/dev/null 2>&1; then
  echo "→ Installing Bun (JavaScript runtime)…"
  curl -fsSL https://bun.sh/install | bash
  # Bun installs to ~/.bun/bin — add to PATH for the rest of this script
  export PATH="$HOME/.bun/bin:$PATH"
  # Also hint to the user to add it to their shell profile if not already
  SHELL_RC="$HOME/.zshrc"
  if ! grep -q "bun/bin" "$SHELL_RC" 2>/dev/null; then
    echo '' >> "$SHELL_RC"
    echo '# Bun' >> "$SHELL_RC"
    echo 'export PATH="$HOME/.bun/bin:$PATH"' >> "$SHELL_RC"
    echo "   (Added Bun to PATH in $SHELL_RC — restart your terminal later)"
  fi
else
  echo "✓ Bun already installed"
fi

# 2. Check ffmpeg + imagemagick (needed for transparent mode; optional otherwise)
if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v convert >/dev/null 2>&1; then
  echo "→ Optional: install ffmpeg + imagemagick for transparent asset support"
  echo "   (not needed for the Noctis site). Run: brew install ffmpeg imagemagick"
fi

# 3. Clone nano-banana-2 if missing
TOOLS_DIR="$HOME/tools"
NB_DIR="$TOOLS_DIR/nano-banana-2"
if [ ! -d "$NB_DIR" ]; then
  mkdir -p "$TOOLS_DIR"
  echo "→ Cloning nano-banana-2 skill into $NB_DIR…"
  git clone --depth 1 https://github.com/kingbootoshi/nano-banana-2-skill.git "$NB_DIR"
else
  echo "✓ nano-banana-2 already cloned at $NB_DIR"
fi

# 4. Install deps + link globally
cd "$NB_DIR"
echo "→ Installing nano-banana dependencies…"
bun install
echo "→ Linking nano-banana globally…"
bun link

# 5. Set up API key if missing
ENV_FILE="$HOME/.nano-banana/.env"
if [ ! -f "$ENV_FILE" ]; then
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "  Gemini API key required"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Get a free key at:  https://aistudio.google.com/apikey"
  echo ""
  read -r -p "Paste your Gemini API key: " GEMINI_KEY
  mkdir -p "$HOME/.nano-banana"
  echo "GEMINI_API_KEY=$GEMINI_KEY" > "$ENV_FILE"
  echo "✓ Saved to $ENV_FILE"
else
  echo "✓ API key already configured at $ENV_FILE"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  ✔ Setup complete."
echo ""
echo "  Next step — generate all car photos:"
echo "    bash scripts/generate-images.sh"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
