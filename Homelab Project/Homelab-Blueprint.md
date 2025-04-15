# Homelab Blueprint & Learning Journal

This document tracks the creation, evolution, and exercises performed in my self-hosted cybersecurity homelab. It includes setup steps, hands-on experiments, troubleshooting, and takeaways from each phase.

---

## Table of Contents

- [Phase 1 – Core Components](#phase-1--core-components)
- [Phase 2 – Network Discovery](#phase-2--network-discovery)
- [Phase 3 – Initial Exploitation](#phase-3--initial-exploitation-with-metasploit)
- [Phase 4 – Installing Splunk (SIEM Integration)](#phase-4--installing-splunk-siem-integration)
- [Next Up](#next-up)

---

## Phase 1 - Core Components

**Objective:** Set up a self-contained, safe lab environment for cybersecurity testing and exploration.

**Overview:** This phase focuses on installing and configuring essential components: Kali Linux as the attacker machine and Metasploitable2 as the vulnerable target, both running within a host-only network using VMware Workstation.

- Downloaded **VMware Workstation**
- Installed **Kali Linux (Attacker)**
- Installed **Metasploitable2 (Target)**
- Configured both VMs to run on **Host-Only networking** for isolation and safety

---
## Phase 2 - Identifying the Target Machine (Network Discovery)

**Objective:** Identify live hosts and services within the isolated lab environment to simulate internal reconnaissance.

**Overview:** Using tools like `ifconfig` and `nmap`, this phase simulates an attacker scanning a local network to discover targets and enumerate exposed ports and services, laying the groundwork for future exploitation.

**Steps:**


1. : Ensure both VM's are running

2. Open command prompt on the Kali Linux VM and identify the local IP address and subnet of your Kali box **(e.g., 192.168.56.x)**.

3. Scan the subnet to identify other live hosts (including the vulnerable box): ```nmap -sn 192.168.56.0/24```


4. Once the Metasploitable2 IP is located, run a basic port scan: ```nmap [target_ip]```


5. : To identify running services and their versions, use the following: ```nmap -sV [target_ip]```. This provides more actionable detail for later exploitation or analysis.


At this stage, the vulnerable system has been identified and its services have been enumerated. This completes the initial reconnaissance phase. Next, we’ll begin exploring exploitation techniques using Metasploit.

---
## Phase 3 – Initial Exploitation with Metasploit

**Objective:** Leverage known vulnerabilities to gain unauthorized access to the target system using Metasploit Framework.

**Overview:** This phase simulates a real-world attack by exploiting the vulnerable vsFTPd service on Metasploitable2, providing experience with vulnerability identification, module selection, and command execution through a remote shell.

**Step 1**: Identify a Target Service. From our earlier nmap -sV results, we found that port 21 is open and running vsFTPd (version 2.3.4), which is known to have a backdoor vulnerability.

**Step 2**: Launch Metasploit Framework through the console with the following command: ```msfconsole```

**Step 3**: Search for a Matching Exploit. Inside the Metasploit console: ```search vsftpd```

**Step 4**: Load the Exploit Module, select the correct exploit for this vulnerability: ```use exploit/unix/ftp/vsftpd_234_backdoor```

**Step 5**: Set Target IP Address. Replace [target_ip] with the actual IP of your Metasploitable2 VM: ```set RHOSTS [target_ip]```

**Step 6**: Run the Exploit: ```exploit```

If successful, this will spawn a root shell on the target system. This is for educational purposes only and should never be performed outside of authorized lab environments.

---
## Phase 4 – Installing Splunk (SIEM Integration)

**Objective:** Install and configure Splunk on Kali Linux to serve as a SIEM platform for future log collection and monitoring.

**Overview:** Splunk will be used to ingest and analyze logs from the lab environment, enabling simulated alerting and incident response workflows. This phase sets the foundation for blue team operations.





---
## Next Up
- Phase 5 – Log Ingestion and Detection