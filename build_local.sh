#!/usr/bin/env bash
#This script allows you to build the blocklist locally
echo """
   _____             __  _ ____         ___       __        __    _      __ 
  / ___/____  ____  / /_(_) __/_  __   /   | ____/ /____   / /   (_)____/ /_
  \__ \/ __ \/ __ \/ __/ / /_/ / / /  / /| |/ __  / ___/  / /   / / ___/ __/
 ___/ / /_/ / /_/ / /_/ / __/ /_/ /  / ___ / /_/ (__  )  / /___/ (__  ) /_  
/____/ .___/\____/\__/_/_/  \__, /  /_/  |_\__,_/____/  /_____/_/____/\__/  
    /_/                    /____/                                           

License: https://github.com/Isaaker/Spotify-AdsList/blob/main/LICENSE.txt
"""

echo "---------------------------------------------"
echo "Checking the environment before running..."
echo "---------------------------------------------"
set -euo pipefail
IFS=$'\n\t'

# Logging helpers
info()  { echo "INFO: $*"; }
warn()  { echo "WARN: $*"; }
error() { echo "ERROR: $*" >&2; exit 1; }

echo "Verifying Python 3"

# -------------------------
# Check for Python 3
# -------------------------
PYBIN=""
if command -v python3 >/dev/null 2>&1; then
  PYBIN=python3
elif command -v python >/dev/null 2>&1; then
  # check if 'python' is Python 3
  if python -c 'import sys; sys.exit(0 if sys.version_info[0] >= 3 else 1)' >/dev/null 2>&1; then
    PYBIN=python
  fi
fi

if [ -z "$PYBIN" ]; then
  error "Python 3 not found in PATH. Install Python 3 or add it to PATH."
fi

PYVER=$($PYBIN -c 'import sys; print("{}.{}.{}".format(*sys.version_info[:3]))')
PYMAJOR=$($PYBIN -c 'import sys; print(sys.version_info[0])')

if [ "$PYMAJOR" -lt 3 ]; then
  error "Found $PYBIN ($PYVER) but it is not Python 3."
fi

info "Python verified: $PYBIN $PYVER"

echo "Verifying SpotifyAdsList scripts and directory"

# -------------------------
# For this repository the directory MUST be the current working directory "./"
# -------------------------
SPOTIFY_ADS_DIR="./"

if [ ! -d "$SPOTIFY_ADS_DIR" ]; then
  error "Current directory ($SPOTIFY_ADS_DIR) does not exist or is not a directory."
fi
info "Using current directory as project directory: $SPOTIFY_ADS_DIR"

# Look for Python scripts at repo root (not deeper)
PY_SCRIPTS_COUNT=$(find "$SPOTIFY_ADS_DIR" -maxdepth 1 -type f -name "*.py" 2>/dev/null | wc -l || true)
if [ "$PY_SCRIPTS_COUNT" -eq 0 ]; then
  warn "No .py files found at repository root ($SPOTIFY_ADS_DIR). Check if scripts are present in subdirectories."
else
  info "Found $PY_SCRIPTS_COUNT .py script(s) at repository root."
fi

# Check for common top-level files for this project
check_topfile() {
  local f="$1"
  if [ -f "$SPOTIFY_ADS_DIR/$f" ]; then
    info "Found $f"
  else
    warn "$f not found at repository root"
  fi
}

check_topfile "README.md"
check_topfile "./Lists/BLACKLIST.txt"
check_topfile "./Lists/WHITELIST.txt"
check_topfile "./scripts/add_default-ads-blocklist.py"
check_topfile "./scripts/update_lists.py"

echo "Verifying write permissions"

# -------------------------
# Check write permissions on current directory
# -------------------------
CWD_OK=false
if touch "$SPOTIFY_ADS_DIR/.__writable_test__" >/dev/null 2>&1; then
  rm -f "$SPOTIFY_ADS_DIR/.__writable_test__"
  CWD_OK=true
fi

if $CWD_OK; then
  info "Write permission in current directory: OK"
else
  warn "No write permission in current directory ($SPOTIFY_ADS_DIR). If the script needs to write files, adjust permissions (chmod/chown) or run as appropriate user."
fi

echo "Environment check completed."

# Exit 0 if critical checks passed (we already exited on critical failures)
exit 0

echo "Verifying write permissions"

# -------------------------
# Check write permissions
# -------------------------
# Check if current working directory is writable
CWD_OK=false
if touch "./.__writable_test__" >/dev/null 2>&1; then
  rm -f "./.__writable_test__"
  CWD_OK=true
fi

# Check if SpotifyAdsList directory is writable
SPOTIFY_DIR_OK=false
if touch "$SPOTIFY_ADS_DIR/.__writable_test__" >/dev/null 2>&1; then
  rm -f "$SPOTIFY_ADS_DIR/.__writable_test__"
  SPOTIFY_DIR_OK=true
fi

# Permission results
if $CWD_OK; then
  info "Write permission in current directory: OK"
else
  warn "No write permission in current directory."
fi

if $SPOTIFY_DIR_OK; then
  info "Write permission in $SPOTIFY_ADS_DIR: OK"
else
  warn "No write permission in $SPOTIFY_ADS_DIR. If the script needs to write there, adjust permissions (chmod/chown)."
fi

# If you want to enforce an output directory, uncomment/adjust:
# OUT_DIR="${OUT_DIR:-$SPOTIFY_ADS_DIR/output}"
# mkdir -p "$OUT_DIR"
# if [ ! -w "$OUT_DIR" ]; then error "Cannot write to $OUT_DIR"; fi

echo "Environment check completed successfully."
# Exit 0 if critical checks passed (we already exited on critical failures)
exit 0

echo "---------------------------------------------"
echo "Spotify Ads List build ready for running!"
echo "---------------------------------------------"
echo "\n"
echo "---------------------------------------------"
echo "Starting to build..."
echo "---------------------------------------------"
echo "Remove duplicated domains"
python3 ./scripts/check_whitelist.py
echo "Download and mix default add blocklist"
python3 ./scripts/add_default-ads-blocklist.py
echo "Remove whitelist domains from WHITELIST-mixed.txt"
python3 ./scripts/check_whitelist_mixed.py
echo "Remove domain exclusion domains from WHITELIST-mixed.txt"
python3 ./scripts/domain_exclusion.py
echo "Build blocklist"
python3 ./scripts/update_lists.py
echo "Build blocklist mixed"
python3 ./scripts/update_list_mixed.py
echo "---------------------------------------------"
echo "Spotify Ads List built succesfully"
echo "Check LISTS at: ./Lists/"
echo "---------------------------------------------"
echo "DONE"
echo "---------------------------------------------"