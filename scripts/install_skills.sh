#!/usr/bin/env bash
# LifeOS Skills Installer for Hermes Agent
# This script installs LifeOS skills into your Hermes Agent setup.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"

echo "LifeOS Skills Installer"
echo "======================="
echo ""

# Check if Hermes home exists
if [ ! -d "$HERMES_HOME" ]; then
    echo "Hermes home not found at $HERMES_HOME"
    echo "Please install Hermes Agent first: https://hermes-agent.nousresearch.com/"
    exit 1
fi

# Check if skills directory exists
if [ ! -d "$SCRIPT_DIR/skills" ]; then
    echo "Skills directory not found at $SCRIPT_DIR/skills"
    echo "Make sure you're running this from the LifeOS root directory."
    exit 1
fi

echo "Hermes home: $HERMES_HOME"
echo ""

# Install lifeos-agent-operations skill
if [ -d "$SCRIPT_DIR/skills/lifeos-agent-operations" ]; then
    echo "Installing lifeos-agent-operations skill..."
    mkdir -p "$HERMES_HOME/skills/productivity"
    cp -r "$SCRIPT_DIR/skills/lifeos-agent-operations" "$HERMES_HOME/skills/productivity/"
    echo "  ✓ lifeos-agent-operations installed"
else
    echo "  ✗ lifeos-agent-operations skill not found"
    echo "    Make sure the skills directory contains the skill."
    exit 1
fi

echo ""
echo "Installation complete!"
echo ""
echo "To use the skill:"
echo "  1. Start Hermes: hermes"
echo "  2. Load skill: /skill lifeos-agent-operations"
echo "  3. Or preload: hermes -s lifeos-agent-operations"
echo ""
echo "For more information, see skills/README.md"
