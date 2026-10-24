#!/usr/bin/env bash
set -euo pipefail
cd /workspace
if curl -sf "http://127.0.0.1:8080/api/health" >/dev/null; then
  exit 0
fi
exec python3 -m ops --host 0.0.0.0 --port 8080
