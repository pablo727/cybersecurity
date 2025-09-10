# SSH Lab - Raw Notes

## Commands
- `nmap -sV -p 22 <target>`
- `nc -vn <target> 22`
- `sudo tcpdump -i <iface> host <target> -w ssh_lab_v1.pcap`

## Observations
- First packets: version exchange.
- Key exchange + host key visible.
- After handshake → gibberish (encrypted).

## Reminders
- Save screenshots to `screenshots/`
- If needed, transfer `.pcap` from Kali via `scp`:
  scp user@kali:/path/to/ssh_lab_v1.pcap ~/Desktop/cybersecurity/ssh_lab/
