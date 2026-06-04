#!/bin/bash
# ResearchPilot — macOS / Linux launcher
# Usage:
#   ./START-SERVER.sh              # start on default port 8000
#   PORT=9000 ./START-SERVER.sh    # start on a different port
#   HOST=0.0.0.0 ./START-SERVER.sh # bind all interfaces (NOT recommended)

set -e
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

PORT="${PORT:-8000}"
HOST="${HOST:-127.0.0.1}"

if [ -t 1 ]; then
    BOLD="\033[1m"; GREEN="\033[32m"; CYAN="\033[36m"; RED="\033[31m"; RESET="\033[0m"
else
    BOLD=""; GREEN=""; CYAN=""; RED=""; RESET=""
fi

echo ""
echo -e "${BOLD}============================================================${RESET}"
echo -e "${BOLD}  ResearchPilot — Starting Server...${RESET}"
echo -e "${BOLD}============================================================${RESET}"
echo ""

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR]${RESET} python3 not found."
    echo "Install Python 3.10+:"
    echo "  macOS:   brew install python@3.11"
    echo "  Linux:   sudo apt install python3.11"
    echo "  Or:      https://www.python.org/downloads/"
    exit 1
fi

# Auto-install dependencies on first run
if [ ! -f ".installed" ]; then
    echo -e "${CYAN}[INFO]${RESET} First run — installing dependencies (1-3 minutes)..."
    python3 -m pip install --user -r requirements.txt
    touch .installed
    echo ""
fi

echo -e "${GREEN}  URL:    http://${HOST}:${PORT}${RESET}"
echo -e "  (Local only — not exposed to the network)"
echo ""
echo -e "${BOLD}  Press Ctrl+C to stop the server.${RESET}"
echo ""

# Try to open browser in the background
( sleep 2 && (xdg-open "http://${HOST}:${PORT}" 2>/dev/null || open "http://${HOST}:${PORT}" 2>/dev/null) ) &

HOST="$HOST" PORT="$PORT" python3 main.py

echo ""
echo "ResearchPilot stopped."
