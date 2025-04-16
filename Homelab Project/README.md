# Personal Homelab Project
This self-hosted lab simulates enterprise systems using virtual machines, firewall segmentation, and network monitoring tools to build hands-on experience in IT support, diagnostics, and incident response workflows.

---
## Skills Demonstrated
- Network Scanning & Reconnaissance
- Vulnerability Identification & Exploitation
- Log Analysis & SIEM Tuning
- Firewall Configuration & Segmentation
- Incident Response Documentation

---
## Setup
- VMware Workstation
- Hosts: Kali Linux & Metasploitable2

---
## Tools Used
- Wireshark for packet inspection and troubleshooting
- Splunk for log monitoring and simulated ticket triage
- pfSense for firewall policy and subnet segmentation

---
## Scenarios Practiced
- **Discovered and profiled live hosts** using `nmap` and `ifconfig` to map internal network topology
- **Enumerated open ports and services** with `nmap -sV` to identify potential attack vectors
- **Simulated brute-force login attempts** on vulnerable services (e.g., Telnet, SSH)
- **Captured network traffic** using Wireshark to analyze reconnaissance activity and reverse shell payloads
- **Tested Splunk SIEM ingestion** by generating synthetic logs and manually uploading system logs for event correlation
- **Executed basic privilege escalation scenarios** using Metasploit modules and post-exploitation tools (sandboxed)
- **Configured pfSense firewall rules** to segment networks and observe blocked vs. allowed traffic patterns
- **Documented incident response workflows** based on Splunk alerting and log search queries

---
## Key Takeaways
- Gained hands-on experience with log analysis, troubleshooting, and user/system behavior
- Learned to simulate real-world IT support cases using controlled environments

---
## Project Roadmap & Goals

This lab is an evolving project designed to simulate key elements of a real-world IT and cybersecurity environment. Below is a snapshot of tracked tasks and planned scenarios, prioritized by importance.

| Project Task                             | Priority | Status       |
|------------------------------------------|----------|--------------|
| Download VMWare                          | High     | ✅ Done       |
| Download Kali Linux                      | High     | ✅ Done       |
| Acquire Defense Box (Metasploitable2)    | High     | ✅ Done       |
| Conduct Initial Exploitation             | High     | ✅ Done       |
| Conduct a Reverse Shell                  | Low      | ✅ Done       |
| Install a SIEM (Splunk)                  | Medium   | ✅ Done       |
| Manage SIEM Effectively                  | Medium   | ✅ Done       |
| Set up pfSense Firewall                  | Medium   | 🔄 In Progress |
| Use Wireshark to Capture Packets         | Low      | 🔄 In Progress |
| OverTheWire Wargames                     | Low      | ⬜ Not Started |
| Mini Hidden Logger (Tool Dev)            | Low      | ⬜ Not Started |
| Patch Vulnerabilities (Metasploitable2)  | Low      | ⬜ Not Started |

**Goal**: Build a fully self-contained environment for simulating attacks, logging incidents, and practicing remediation across multiple OSes and network layers.

---
## Contact
Josip Huzovic  
josiphuzovic@gmail.com  
[LinkedIn Profile](https://www.linkedin.com/in/josip-huzovic)
