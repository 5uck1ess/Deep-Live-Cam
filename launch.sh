#!/bin/bash
# Deep-Live-Cam May 2026 Fork — Optimized for RTX 5090
# Forked from upstream hacksider/Deep-Live-Cam v2.1.6
# run.py handles CUDA DLL discovery itself (no conda hack needed)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

.venv/Scripts/python run.py \
    --execution-provider cuda
