#!/bin/bash
set -euo pipefail

LABUSER="${SUDO_USER:-$(whoami)}"
BASEDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTDIR="${BASEDIR}/john-lab"
UNSHADOW_FILE="$OUTDIR/mypasswd"
WORDLIST_GZ="/usr/share/wordlists/rockyou.txt.gz"
WORDLIST="/usr/share/wordlists/rockyou.txt"

echo "[*] Make sure you snapshot the VM now. Press Ctrl-C to abort or Enter to continue."
read -r

# Ensure output dir exists and has proper ownership
mkdir -p "$OUTDIR"
sudo chown "$LABUSER:$LABUSER" "$OUTDIR" || true

# Remove any existing lab users
sudo userdel -r alice || true
sudo userdel -r bob   || true
sudo userdel -r charlie || true

# Create lab users
sudo useradd -m -s /bin/bash alice
sudo useradd -m -s /bin/bash bob
sudo useradd -m -s /bin/bash charlie

# Set SHA-512 passwords
echo "alice:AlicePass1!" | sudo chpasswd -e
echo "bob:BobPass!23"     | sudo chpasswd -e
echo "charlie:Passw0rd123!" | sudo chpasswd -e

# Show users
echo "[*] Users created:"
getent passwd alice bob charlie

# Combine passwd + shadow into mypasswd file
sudo bash -c "umask 077; unshadow /etc/passwd /etc/shadow > '$UNSHADOW_FILE'"

sudo chown "$LABUSER:$LABUSER" "$UNSHADOW_FILE"
chmod 600 "$UNSHADOW_FILE"

# Ensure rockyou wordlist is available
if [ -f "$WORDLIST_GZ" ] && [ ! -f "$WORDLIST" ]; then
    echo "[*] Decompressing rockyou.gz..."
    sudo gzip -dk "$WORDLIST_GZ" || true
fi

if [ ! -f "$WORDLIST" ]; then
    echo "[!] rockyou.txt not found. Install with: sudo apt install wordlists"
    exit 1
fi

# Run John with SHA-512 format
echo "[*] Starting John the Ripper (dictionary + rules)... Ctrl-C to stop."
john --format=sha512crypt --wordlist="$WORDLIST" --rules --session=labsession "$UNSHADOW_FILE"

echo "[*] Cracked accounts:"
john --show "$UNSHADOW_FILE"

echo "[*] Created files in $OUTDIR:"
ls -l "$OUTDIR"
