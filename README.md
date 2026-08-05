# Josip Huzovic – Cybersecurity & IT Portfolio

I'm Josip, a cybersecurity graduate focused on building and testing real-world attack, defense, and analysis scenarios. Projects range from USB-based ransomware simulations to SIEM tuning and detection engineering across virtual labs and dedicated server hardware.

Everything here was built for educational and demonstrative purposes, and tested safely in isolated virtual labs.

---
## Projects

### > [Homelab Server: Virtualized Security Lab on Proxmox](./Homelab%20Server)

**Actively maintained.** 

A rebuilt homelab running on dedicated hardware, replacing my original nested-VM setup with proper storage redundancy, network segmentation, and persistent lab infrastructure.
- Proxmox VE hypervisor on a UGREEN DXP4800 Pro with NVMe VM storage and a ZFS mirror for backups
- pfSense edge firewall with segmented VLANs isolating lab, management, and services traffic
- Splunk ingesting firewall, system, and authentication logs for detection tuning
- UPS-backed for graceful shutdown and lab state preservation

### > [Legacy Homelab: Network Defense & SIEM Tuning](./Legacy%20Homelab%20Project)

**Superseded by my current homelab, kept here to show earlier work.**

This lab simulates internal reconnaissance, attack execution, and blue team response using Splunk, pfSense, and a segmented network of VMs.
- Simulated attack paths using Nmap, Metasploit, and reverse shells
- Configured pfSense to segment network traffic and control inbound exploitation attempts
- Ingested `.zsh_history` and synthetic logs into Splunk for near-real-time detection
- Documented incident response flow based on triggered alerts and manual correlation

### > [Malware Simulation: USB-Based Cross-Platform Ransomware](./Malware%20USB%20Simulation)
Simulated real-world ransomware behavior using a Bash Bunny Mark II USB emulation device, with OS-aware logic and ethical recovery workflows. Includes a full-featured Linux payload developed using Ducky Script, GPG-based encryption, and systemd-based persistence.
- Payload detects OS (Windows or Linux) and adjusts attack strategy accordingly
- Designed for AV evasion and privilege-aware execution using PowerShell and terminal-based delivery
- Includes full recovery script and test validation procedures
- Built and tested in VMware-based sandbox environments
- Awarded 2nd Place at the 2024 Mid-Hudson Valley TechMeet for innovation and safe malware handling

Full Report: [Capstone Technical Write-Up (PDF)](./Malware%20USB%20Simulation/Cybersecurity_Capstone_Bash_Bunny_Project.pdf)

### > [Beaconing Simulation: Safe C2-Style Traffic](./Simulated%20Beaconing%20Traffic)  
Developed a small-scale simulation of **malware-like beaconing traffic** to practice detection techniques in Wireshark. This project demonstrates how beaconing patterns can be identified through timing, payload consistency, and unusual port usage.  
- Wrote a Python script to generate UDP “beacon” packets at fixed intervals  
- Captured and analyzed the traffic in Wireshark using custom port filters  
- Identified detection points such as repeated intervals, consistent payloads, and non-standard port activity  
- Built as a **safe, educational lab project** for defensive training and portfolio demonstration  



---
## Tools & Technologies
- **Languages:** Python, PowerShell, Bash, SQL, JavaScript, Ducky Script
- **Security Tools:** Splunk, Wireshark, Nessus, pfSense, Metasploit, Nmap
- **Infrastructure:** Proxmox VE, ZFS, VLAN segmentation, VMware Workstation, VirtualBox
- **Operating Systems:** Linux (Arch, Debian, Kali), Windows
- **Hardware:** Bash Bunny Mark II, Cisco Packet Tracer

---
## Certifications
- **CompTIA Security Analytics Professional (CSAP)** – Jun 2026
- **CompTIA CySA+** – Jun 2026
- **CompTIA Security+** – Oct 2024
- **Google Cybersecurity Certificate** – Feb 2025

[Verify credentials on Credly](https://www.credly.com/users/josip-huzovic/badges/credly)

---
## Education
**Bachelor of Science in Cybersecurity** – Marist University, May 2025  
Minors in Information Technology, Information Systems, and Computer Science  
Dean's List: Fall 2023, Spring 2025

---
## License
All original content in this portfolio, including documentation, write-ups, and code, is licensed under the MIT License.
See the [LICENSE](./LICENSE) file for full details.

---
## Thanks for checking out my portfolio!
If you'd like to connect, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/josip-huzovic/) or email me at josiphuzovic@gmail.com.
