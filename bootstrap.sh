#!/usr/bin/env bash

# bootstrap.sh - Setup development environment for the algorithms project

set -euo pipefail

# Detect OS
OS="$(uname)"

function info() { echo -e "\033[1;34m[INFO]\033[0m $*"; }
function warn() { echo -e "\033[1;33m[WARN]\033[0m $*"; }

function install_uv() {
    # Ensure potential uv installation paths are in PATH for this script execution
    export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"

    if command -v uv >/dev/null 2>&1; then
        info "uv already installed"
    else
        info "Installing uv (fast Python package manager)"
        if command -v curl >/dev/null 2>&1; then
            curl -Ls https://astral.sh/uv/install.sh | bash
            # Re-export PATH to ensure it's available for subsequent commands if uv was just installed
            export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
        else
            warn "curl not found. Please install curl and re-run the script."
            exit 1
        fi
    fi
}

function install_just() {
    if command -v just >/dev/null 2>&1; then
        info "just already installed"
    else
        info "Installing just (command runner)"
        if command -v cargo >/dev/null 2>&1; then
            info "Attempting to install just using cargo"
            if ! cargo install just; then
                warn "Failed to install just using cargo. Please check cargo output."
                exit 1
            fi
        elif command -v brew >/dev/null 2>&1; then # Typically macOS
            info "Attempting to install just using brew"
            if ! brew install just; then
                warn "Failed to install just using brew. Please check brew output."
                exit 1
            fi
        elif [[ "$OS" == "Linux"* ]] && command -v apt-get >/dev/null 2>&1; then
            info "Attempting to install just using apt"
            if ! (sudo apt-get update && sudo apt-get install -y just); then
                warn "Failed to install just using apt. Please check apt output."
                exit 1
            fi
        else
            warn "Could not find cargo, brew, or apt (for Linux) to install just. Please install 'just' manually."
            exit 1
        fi
    fi
}

function install_python_linux() {
    if ! command -v python3 >/dev/null 2>&1; then
        info "Installing Python"
        sudo apt-get update
        sudo apt-get install -y python3 python3-venv python3-pip
    fi
}

function install_python_mac() {
    if ! command -v python3 >/dev/null 2>&1; then
        if command -v brew >/dev/null 2>&1; then
            info "Installing Python via Homebrew"
            brew install python
        else
            warn "Homebrew not found. Please install Homebrew or Python manually."
            exit 1
        fi
    fi
}

case "$OS" in
    Linux*)
        install_python_linux
        ;;
    Darwin*)
        install_python_mac
        ;;
    *)
        echo "Unsupported OS: $OS" >&2
        exit 1
        ;;
esac

install_uv
install_just

info "Synchronizing dependencies with uv"
uv sync

info "Setup complete. Activate the environment with:\n  source .venv/bin/activate"
