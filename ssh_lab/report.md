# SSH Lab - Handshake Analysis

**Date:** 2025-09-10
**Lab folder:** `ssh_lab`

## Objective
Capture and analyze SSH handshakes between Kali (attacker) and Ubuntu (target).

## Tools Used
- nmap
- netcat
- ssh
- tcpdump / Wireshark

## Steps Taken
1. Discovery / scanning with `nmap`.
2. Packet capture with `tcpdump`.
3. Opened `.pcap` in Wireshark and identified the SSH handshake.

## Findings
- SSH handshake visible.
- Session data fully encrypted (no plaintext credentials).

## Lessons Learned
- Difference between handshake vs. encrypted payload.
- Reinforced that SSH is secure when configured properly.

