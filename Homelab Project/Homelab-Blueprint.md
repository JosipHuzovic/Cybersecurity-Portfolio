# Homelab Blueprint & Learning Journal

This document tracks the creation, evolution, and exercises performed in my self-hosted cybersecurity homelab. It includes setup steps, hands-on experiments, troubleshooting, and takeaways from each phase.

---

## Phase 1 - Core Components

For this first phase we'll just be installing the proper components to this lab.

- Downloaded **VMware Workstation**
- Installed **Kali Linux (Attacker)**
- Installed **Metasploitable2 (Target)**
- Configured both VMs to run on **Host-Only networking** for isolation and safety

---
## Phase 2 - Identifying the Target Machine (Network Discovery)

After both the attacker (Kali Linux) and target (Metasploitable2) virtual machines are running, the first step is to locate the IP address of the vulnerable machine so that scanning and testing can begin.

**Step 1**: Ensure both VM's are running

**Step 2**: Open command prompt on the Kali Linux VM and identify the local IP address and subnet of your Kali box **(e.g., 192.168.56.x)**.

**Step 3**: Scan the subnet to identify other live hosts (including the vulnerable box): ```nmap -sn 192.168.56.0/24```


**Step 4**: Once the Metasploitable2 IP is located, run a basic port scan: ```nmap [target_ip]```


**Step 5**: To identify running services and their versions, use the following: ```nmap -sV [target_ip]```. This provides more actionable detail for later exploitation or analysis.


At this stage, the vulnerable system has been identified and its services have been enumerated. This completes the initial reconnaissance phase. Next, we’ll begin exploring exploitation techniques using Metasploit.

---
## Phase 3 – Initial Exploitation with Metasploit

