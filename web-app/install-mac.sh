#!/bin/bash
# ResearchPilot macOS / Linux one-time setup
# Usage:  ./install-mac.sh    or    bash install-mac.sh

set -e
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

BOLD="\033[1m"; GREEN="\033[32m"; CYAN="\033[36m"; RED="\033[31m"; RESET="\033[0m"

echo ""
echo -e "${BOLD}============================================================${RESET}"
echo -e "${BOLD}  ResearchPilot — First-Time Setup${RESET}"
echo -e "${BOLD}============================================================${RESET}"
echo ""

# 1. Check Python
echo -e "${CYAN}[1/4]${RESET} Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR]${RESET} python3 not found."
    echo "Install Python 3.10+:"
    echo "  macOS:   brew install python@3.11"
    echo "  Linux:   sudo apt install python3.11"
    echo "  Or:      https://www.python.org/downloads/"
    exit 1
fi
PY_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo -e "${GREEN}       OK${RESET} Python ${PY_VERSION} found"

# 2. Install dependencies
echo ""
echo -e "${CYAN}[2/4]${RESET} Installing required packages (1-3 minutes)..."
python3 -m pip install --user -r requirements.txt

# 3. Make launcher executable
echo ""
echo -e "${CYAN}[3/4]${RESET} Making launcher executable..."
chmod +x START-SERVER.sh

# 4. Create folders
echo ""
echo -e "${CYAN}[4/4]${RESET} Creating default folders..."
cd ..
mkdir -p 01-PROJECTS 00-SYSTEM-CORE/skills 99-SYSTEM-BACKEND/chats INCOMING/UNREAD-WEB

echo ""
echo -e "${BOLD}============================================================${RESET}"
echo -e "${GREEN}  Setup complete!${RESET}"
echo -e "${BOLD}============================================================${RESET}"
echo ""
echo "Next steps:"
echo "  1. To start ResearchPilot:"
echo "       cd web-app && ./START-SERVER.sh"
echo ""
echo "  2. To enable auto-start on login (macOS):"
echo "       System Settings → General → Login Items → + → web-app/START-SERVER.sh"
echo ""
echo "  3. For detailed help, see SETUP.md"
echo ""
