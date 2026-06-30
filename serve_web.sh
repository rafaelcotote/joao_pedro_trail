#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_DIR="${VENV_DIR:-$HOME/.venvs/joao_pedro_trail}"
if [ -x "$VENV_DIR/bin/python" ]; then
  PYTHON_BIN="$VENV_DIR/bin/python"
fi

HOST="${WEB_HOST:-}"
if [ -z "$HOST" ]; then
  HOST="$(hostname -I 2>/dev/null | awk '{print $1}')"
fi
if [ -z "$HOST" ]; then
  HOST="127.0.0.1"
fi

echo "Servindo em http://$HOST:8085"
"$PYTHON_BIN" -m pygbag --bind "$HOST" --port 8085 --ume_block 0 .
