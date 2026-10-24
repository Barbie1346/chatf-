#!/usr/bin/env bash
set -euo pipefail
cd /workspace
python3 -m compileall -q ops tests
