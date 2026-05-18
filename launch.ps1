# Deep-Live-Cam May 2026 Fork — Optimized for RTX 5090
# Forked from upstream hacksider/Deep-Live-Cam v2.1.6
# run.py handles CUDA DLL discovery itself (no conda hack needed)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

& .\.venv\Scripts\python.exe run.py `
    --execution-provider cuda
