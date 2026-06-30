#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_DIR="${VENV_DIR:-$HOME/.venvs/joao_pedro_trail}"
if [ -x "$VENV_DIR/bin/python" ]; then
  PYTHON_BIN="$VENV_DIR/bin/python"
fi

TAILSCALE_IP="$(tailscale ip -4 2>/dev/null | head -n 1 || true)"
HOST="${WEB_HOST:-}"
if [ -z "$HOST" ]; then
  HOST="$TAILSCALE_IP"
fi
if [ -z "$HOST" ]; then
  HOST="$(hostname -I 2>/dev/null | awk '{print $1}')"
fi
if [ -z "$HOST" ]; then
  HOST="127.0.0.1"
fi

LOCAL_IPS="$(hostname -I 2>/dev/null || true) $TAILSCALE_IP"
case " $LOCAL_IPS 127.0.0.1 localhost " in
  *" $HOST "*) ;;
  *)
    echo "ERRO: WEB_HOST=$HOST nao esta configurado nesta maquina."
    echo "IPs locais detectados: ${LOCAL_IPS:-nenhum}"
    echo "Use um dos IPs acima. Se estiver usando Tailscale, confirme no servidor com: tailscale ip -4"
    exit 2
    ;;
esac

echo "Servindo em http://$HOST:8085"
WEB_APP_DIR="build/pygbag_app"
rm -rf "$WEB_APP_DIR"
mkdir -p "$WEB_APP_DIR"
cp main.py "$WEB_APP_DIR/main.py"

"$PYTHON_BIN" -m pygbag --bind "$HOST" --port 8085 --ume_block 0 "$WEB_APP_DIR"
