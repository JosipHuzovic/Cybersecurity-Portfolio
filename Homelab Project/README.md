<h1 align="center"><strong>Personal Homelab Project</strong></h1>

This self-hosted lab simulates enterprise systems using virtual machines, firewall segmentation, and network monitoring tools to build hands-on experience in IT support, diagnostics, and incident response workflows.

---
## Hands-On Experience With
- Simulating internal reconnaissance (e.g., live host scans, port/service fingerprinting)
- Exploiting known vulnerabilities and observing behavior (reverse shells, privilege escalation)
- Using Splunk to ingest logs and emulate SOC detection workflows
- Designing and applying firewall segmentation policies with pfSense
- Capturing and analyzing packet data using Wireshark for post-incident review

---
## Setup
- VMware Workstation
- Hosts: Kali Linux & Metasploitable2

---
## Tooling & Stack (Purpose-Driven)
- **VMware Workstation** – runs fully isolated lab for safe offensive/defensive testing
- **Kali Linux** – attacker machine for scanning, exploitation, and shell delivery
- **Metasploitable2** – intentionally vulnerable target for red team scenarios
- **pfSense** – handles segmentation and simulates enterprise perimeter defense
- **Splunk** – central log aggregation and search interface to emulate blue team workflows
- **Wireshark** – packet capture used to analyze traffic during attacks and incident simulation

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

## Network Topology

<p align="center">
  <img src="./Images/Topology_After_SIEM_and_Log_Integration.png" alt="Network Topology Diagram">
</p>

---
## Key Takeaways
- Built the full stack myself — network design, firewall config, SIEM setup, and testing
- Gained real insight into how attackers move and how logs tell the story
- Practiced not just tool use, but **system-level thinking** across offense and defense

---
## Project Phases & Milestones

This lab was developed in structured phases, each building on the last. It mirrors a small enterprise network progressing from vulnerable baseline to layered defense and SIEM monitoring.

| Phase | Focus Area                                               | Status        |
|-------|----------------------------------------------------------|---------------|
| 1     | Core Setup: Kali & Metasploitable2 on host-only network  | ✅ Complete    |
| 2     | Network Discovery: Internal recon using `nmap`, `ifconfig`| ✅ Complete    |
| 3     | Initial Exploitation: vsFTPd vulnerability via Metasploit| ✅ Complete    |
| 4     | Firewall Segmentation: Deployed pfSense and isolated LAN | ✅ Complete    |
| 5     | SIEM Deployment: Splunk on Windows 10 VM                 | ✅ Complete    |
| 6     | Log Integration: Syslog from pfSense into Splunk         | ✅ Complete    |
| 7     | Detection Validation: Simulate attacks, tune Splunk alerts| 🔄 In Progress |
| 8     | Packet Inspection: Use Wireshark to validate traffic flows| ⬜ Planned     |



**Goal**: Build a fully self-contained environment for simulating attacks, logging incidents, and practicing remediation across multiple OSes and network layers.

---
## About Me
Josip Huzovic  
josiphuzovic@gmail.com  
[LinkedIn Profile](https://www.linkedin.com/in/josip-huzovic)