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
         DARK HACKER – FILE INTEGRITY MONITOR
```

# 🕵️‍♂️ Cybersecurity Labs

This repo contains my hands-on labs, notes, and reports while learning cybersecurity.

---

## 📂 File Integrity

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