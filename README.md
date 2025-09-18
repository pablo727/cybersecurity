# 🕵️‍♂️ Cybersecurity Labs

This repo contains my hands-on labs, notes, and reports while learning cybersecurity.

---

## 📂 File Integrity

```text
        ██████╗ ███████╗ ██████╗ ██████╗ ██████╗███████╗
       ██╔════╝ ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
       ██║  ███╗███████║██║  ██║█████╗  █████╗  ██████╔╝
       ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══╝  ██╔══██╗
       ╚██████╔╝██║  ██║██████╔╝███████╗███████╗██║  ██║
        ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
           ██████╗  █████╗  ██████╗██╗  ██╗███████╗      
          ██╔════╝ ██╔══██╗██╔════╝██║  ██║██╔════╝      
          ██║  ███╗███████║██║     ███████║█████╗        
          ██║   ██║██╔══██║██║     ██╔══██║██╔══╝        
          ╚██████╔╝██║  ██║╚██████╗██║  ██║███████╗      
           ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝      
                  FILE INTEGRITY MONITOR
```

### Lab: File Integrity Verification
- **Tools Used:** `sha256sum`, `md5sum`, `cp`, `echo`, `scp`
- **Steps Performed:**
  1. Created a demo file (`integrity_demo.txt`)
  2. Generated initial hashes (`sha256sum`, `md5sum`)
  3. Tampered with the file and observed hash changes
  4. Restored original file from backup
  5. Transferred lab file between hosts and verified integrity

- **Lessons Learned:**
  - File hashes detect tampering (even a single character change).
  - Backups are essential for integrity verification.
  - Use `sha256` over `md5` for modern integrity checks.

---

### Script: `file_integrity_monitor.py`
A Python script that recursively scans a directory, computes **SHA-256 hashes** of all files, and saves the results in JSON format.  

#### Features:
- Recursively walk through a directory with `Path.rglob`.
- Compute SHA-256 checksums for every file.
- Save results in a JSON file (`hashes.json`) for later comparison.
- Simple logging for transparency.

#### Example Usage:
**(inside the script, replace /your/dir with the directory you want to scan)**
```bash
python3 file_integrity_monitor.py
```

```json
Output format:

{
  "base": "/home/pablo/Desktop/cybersecurity/ssh_lab",
  "files": {
    "ssh_lab.pcap": "25533b4...",
    "notes_ssh_lab.md": "a3f5e6..."
  }
}
```

💡 This folder combines manual labs (with Linux tools) and automation scripts (with Python) to strengthen cybersecurity skills.

---

## 🔪 John the Ripper Lab

```text

      ██╗ ██████╗███╗   ██╗     ██████╗ ███████╗██████╗ ██████╗ ██████╗ 
      ██║██╔════╝████╗  ██║    ██╔═══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗
      ██║██║     ██╔██╗ ██║    ██║   ██║█████╗  ██████╔╝██║  ██║██████╔╝
██   ██║██║     ██║╚██╗██║    ██║   ██║██╔══╝  ██╔══██╗██║  ██║██╔═══╝ 
╚█████╔╝╚██████╗██║ ╚████║    ╚██████╔╝███████╗██║  ██║██████╔╝██║     
 ╚════╝  ╚═════╝╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝     
                  JOHN THE RIPPER – PASSWORD CRACKING LAB
```

### Lab: Password Cracking with John the Ripper
- **Tools Used:** `john`, `openssl`, Bash scripting
- **Steps Performed:**
  1. Created a custom `unshadow.sh` script to combine `/etc/passwd` and `/etc/shadow`.
  2. Created test users (`alice`, `bob`, `charlie`) with SHA-512 encrypted passwords.
  3. Prepared a sample password hash file (`mypasswd.example`) for safe sharing.
  4. Used `john` with the RockYou wordlist to attempt cracking passwords.
  5. Learned to use `--format=sha512crypt`, `--show`, and session restoration (`--restore`) for efficient cracking.

- **Lessons Learned:**
  - John the Ripper can detect password weaknesses with wordlists.
  - SHA-512 hashes are stronger and slower to crack, so wordlists must be targeted.
  - Sensitive files (`mypasswd`) must never be pushed to GitHub—use examples or dummy data.
  - `.gitignore` prevents accidental commits of passwords and session artifacts.

### Included Files:
- `unshadow.sh`: Bash script to generate combined passwd/shadow file for John.
- `mypasswd.example`: Example hash file with dummy passwords.
- `testlist.txt`: Minimal test wordlist for fast cracking demonstration.
- `.gitignore`: Prevents sensitive files and John artifacts from being committed.

💡 This lab demonstrates password security, hash encryption, and safe handling of sensitive files when practicing password cracking exercises.