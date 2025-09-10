# Lab: File Integrity Verification

**Environment:** Kali VM → file `ssh_lab.pcap`

**Tools Used:** `sha256sum`, `md5sum`, `cp`, `echo`

---

## Steps Performed
1. **Create a test file for integrity demo**
      integrity_demo.txt
2. **Check inital file hashes**
     sha256sum integrity_demo.txt
     md5sum integrity_demo.txt
3. **Tamper with the file**
     Append text: "attacker changed this"
4. **Verify hash changes**
     sha256sum integrity_demo.txt
     md5sum integrity_demo.txt
5. **Apply same process to lab capture file**
     sha256sum~.ssh_lab.pcap
     Append text: "modification test"
     sha256sum~/ssh_lab.pcap
6. **Attempt to restore original file**
     cp~/ssh_lab_backup.pcap~/ssh_lab.pcap
7. **Transfer lab file to Ubuntu target**
     scp~/ssh_lab.pcap pablo@192.XXX.XX.XX:/tmp/

---

## Lessons Learned

- File hashes detect tampering - even a single character change will change SHA256/MD5.
- Keep backups of original files to compare integrity.
- Home directory permissions can prevent SCP copy; `/tmp/` is usually writable.
- Always verify hash after transfer to ensure integrity isn't compromised.
- SHA256 is preferred pver MD5 for modern integrity checks.
