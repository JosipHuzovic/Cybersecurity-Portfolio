# Josip Huzovic – Cybersecurity & IT Portfolio

I'm Josip, a cybersecurity graduate focused on building and testing real-world attack and defense scenarios. Projects range from USB-based ransomware simulations to SIEM tuning and log correlation inside enterprise-style virtual labs.

Everything here was built for educational and demonstrative purposes, and tested safely in isolated virtual labs.

---
## Projects

### [Homelab: Network Defense & SIEM Tuning](./Homelab%20Project)
This lab simulates internal reconnaissance, attack execution, and blue team response using Splunk, pfSense, and a segmented network of VMs.
- Simulated attack paths using Nmap, Metasploit, and reverse shells
- Configured pfSense to segment network traffic and control inbound exploitation attempts
- Ingested `.zsh_history` and synthetic logs into Splunk for near-real-time detection
- Documented incident response flow based on triggered alerts and manual correlation

### [Malware Simulation: USB-Based Cross-Platform Ransomware](./Malware%20USB%20Simulation)
Simulated real-world ransomware behavior using a Bash Bunny Mark II USB emulation device, with OS-aware logic and ethical recovery workflows. Includes a full-featured Linux payload developed using Ducky Script, GPG-based encryption, and systemd-based persistence.
- Payload detects OS (Windows or Linux) and adjusts attack strategy accordingly
- Designed for AV evasion and privilege-aware execution using PowerShell and terminal-based delivery
- Includes full recovery script and test validation procedures
- Built and tested in VMware-based sandbox environments
- Awarded 2nd Place at the 2024 Mid-Hudson Valley TechMeet for innovation and safe malware handling

Full Report: [Capstone Technical Write-Up (PDF)](./Malware%20USB%20Simulation/Cybersecurity_Capstone_Bash_Bunny_Project.pdf)

---
## Tools & Technologies
- **Languages:** Python, PowerShell, Bash, SQL, JavaScript, Ducky Script
- **Tools:** Splunk, Wireshark, Nessus, pfSense, Cisco Packet Tracer
- **Platforms:** VMware Workstation, VirtualBox, Bash Bunny Mark II

---
## Credentials
- CompTIA Security+ (Issued Oct 2024)
- Google Cybersecurity Foundations (Issued Feb 2025)
- Bachelor of Science in Cybersecurity, Marist University (Expected May 2025)

---
## License
All original content in this portfolio, including documentation, write-ups, and code, is licensed under the MIT License.
See the [LICENSE](./LICENSE) file for full details.

---
## Thanks for checking out my portfolio!
If you'd like to connect, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/josip-huzovic/) or email me at josiphuzovic@gmail.com.