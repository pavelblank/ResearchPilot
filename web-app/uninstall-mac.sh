#!/bin/bash
# ResearchPilot macOS / Linux Uninstaller
# Removes: auto-start, server processes, Python cache
# Does NOT remove your data — delete the folder manually to wipe.

set -e
BOLD="\033[1m"; GREEN="\033[32m"; CYAN="\033[36m"; RED="\033[31m"; RESET="\033[0m"

echo ""
echo -e "${BOLD}============================================================${RESET}"
echo -e "${BOLD}  ResearchPilot Uninstaller${RESET}"
echo -e "${BOLD}============================================================${RESET}"
echo ""

# 1. Remove auto-start (macOS uses launchd, Linux uses systemd/autostart)
echo -e "${CYAN}[1/3]${RESET} Removing auto-start entries..."

# macOS LaunchAgent
LAUNCH_AGENT="$HOME/Library/LaunchAgents/com.researchpilot.server.plist"
[ -f "$LAUNCH_AGENT" ] && launchctl unload "$LAUNCH_AGENT" 2>/dev/null || true
[ -f "$LAUNCH_AGENT" ] && rm -f "$LAUNCH_AGENT" && echo "       Removed LaunchAgent"
[ ! -f "$LAUNCH_AGENT" ] && echo "       No macOS LaunchAgent found"

# Linux autostart
AUTOSTART="$HOME/.config/autostart/researchpilot.desktop"
[ -f "$AUTOSTART" ] && rm -f "$AUTOSTART" && echo "       Removed Linux autostart" || true
[ ! -f "$AUTOSTART" ] && echo "       No Linux autostart found"

# 2. Kill server
echo ""
echo -e "${CYAN}[2/3]${RESET} Stopping any running servers..."
pkill -f "python.*main.py" 2>/dev/null && echo "       Stopped server" || echo "       No server running"

# 3. Clean cache
echo ""
echo -e "${CYAN}[3/3]${RESET} Cleaning Python cache..."
find "$SCRIPT_DIR/../01-PROJECTS" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
echo "       Done"

echo ""
echo -e "${BOLD}============================================================${RESET}"
echo -e "${GREEN}  Uninstall complete.${RESET}"
echo -e "${BOLD}============================================================${RESET}"
echo ""
echo "Your research data is still in the ResearchPilot folder."
echo "Delete the folder manually to remove it permanently."
echo ""
