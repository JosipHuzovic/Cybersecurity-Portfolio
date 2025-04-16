# Homelab Blueprint & Learning Journal

This document tracks the creation, evolution, and exercises performed in my self-hosted cybersecurity homelab. It includes setup steps, hands-on experiments, troubleshooting, and takeaways from each phase.

---

## Table of Contents

- [Phase 1 – Core Components](#phase-1--core-components)
- [Phase 2 – Network Discovery](#phase-2--network-discovery)
- [Phase 3 – Initial Exploitation](#phase-3--initial-exploitation-with-metasploit)
- [Phase 4 – Installing Splunk (SIEM Integration)](#phase-4--installing-splunk-siem-integration)
- [Phase 5 - Splunk Log Ingestion and Detection](#phase-5--splunk-log-ingestion-and-detection)
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


1. Ensure both VM's are running

2. Open command prompt on the Kali Linux VM and identify the local IP address and subnet of your Kali box **(e.g., 192.168.56.x)**.

3. Scan the subnet to identify other live hosts (including the vulnerable box): ```nmap -sn 192.168.56.0/24```


4. Once the Metasploitable2 IP is located, run a basic port scan: ```nmap [target_ip]```


5. To identify running services and their versions, use the following: ```nmap -sV [target_ip]```. This provides more actionable detail for later exploitation or analysis.


*At this stage, the vulnerable system has been identified and its services have been enumerated. This completes the initial reconnaissance phase. Next, we’ll begin exploring exploitation techniques using Metasploit.*

---
## Phase 3 – Initial Exploitation with Metasploit

**Objective:** Leverage known vulnerabilities to gain unauthorized access to the target system using Metasploit Framework.

**Overview:** This phase simulates a real-world attack by exploiting the vulnerable vsFTPd service on Metasploitable2, providing experience with vulnerability identification, module selection, and command execution through a remote shell.

**Steps:**

1. Identify a Target Service. From our earlier nmap -sV results, we found that port 21 is open and running vsFTPd (version 2.3.4), which is known to have a backdoor vulnerability.

2. Launch Metasploit Framework through the console with the following command: ```msfconsole```

3. Search for a Matching Exploit. Inside the Metasploit console: ```search vsftpd```

4. Load the Exploit Module, select the correct exploit for this vulnerability: ```use exploit/unix/ftp/vsftpd_234_backdoor```

5. Set Target IP Address. Replace [target_ip] with the actual IP of your Metasploitable2 VM: ```set RHOSTS [target_ip]```

6. Run the Exploit: ```exploit```

*If successful, this will spawn a root shell on the target system. This is for educational purposes only and should never be performed outside of authorized lab environments.*

---
## Phase 4 – Installing Splunk (SIEM Integration)

**Objective:** Install and configure Splunk on Kali Linux to serve as a SIEM platform for future log collection and monitoring.

**Overview:** Splunk will be used to ingest and analyze logs from the lab environment, enabling simulated alerting and incident response workflows. This phase sets the foundation for blue team operations.

**Steps:**

1. Acquire `wget` link for SIEM in question (Splunk in this case)

2. Use `wget` command to download the latest version (as of this setup): `wget https://download.splunk.com/products/splunk/releases/9.4.1/linux/splunk-9.4.1-e3bdab203ac8-linux-amd64.deb`

3. To actually install the SIEM type: `sudo dpkg -i splunk-9.4.1-e3bdab203ac8-linux-amd64.deb`

4. To accept the license: `sudo /opt/splunk/bin/splunk start --accept-license`

*Note: Splunk version numbers and filenames may change over time, adjust the URL and commands accordingly.*

5. Input Username and Password for SIEM

6. Link for Splunk should look something like this: *http://kali:8000/en-US/manager/search/adddata*

7. Next time you reboot or want to start Splunk again: `sudo /opt/splunk/bin/splunk start`

8. If you want it to run on start automatically: `sudo /opt/splunk/bin/splunk enable boot-start`

---
## Phase 5 – Splunk Log Ingestion and Detection

**Objective:** Configure Splunk to monitor `.zsh_history` in near real-time on Kali Linux to log and analyze terminal commands as part of simulated blue team operations.

**Overview:** By setting up Splunk to watch the .zsh_history file, we can track executed terminal commands from the Kali Linux VM. This gives visibility into attacker behavior and supports future correlation and detection use cases. To make logs appear instantly in Splunk, we'll also configure the shell to write history after every command.

**Steps:**

1. Log in to Splunk via the browser (typically at *http://kali:8000*)

2. Scroll down and click on Add Data

3. Choose Monitor as the method of adding data

4. Select Files and Directories

5. Under File or Directory, enter the path: `/home/kali/.zsh_history`, then click Next

6. Set the Source Type to zsh_current, then click Next

7. On the input settings page, leave defaults and click Review

8. Click Submit to finalize the configuration

9. Click Start Searching to be taken to the Splunk Search & Reporting dashboard

10. In the search bar, verify you're search is the same as the one below: 

![`source="/home/kali/.zsh_history" host="kali" sourcetype="zsh_current"`](Images/Search_Parameters.png)

11. By default, the .zsh_history file only updates when the terminal session ends. To manually update it, use the command: ```fc -W```

*If everything was set up correctly, you should now see your terminal command logs appearing in Splunk. If something isn’t working, navigate to the top right of the Splunk interface and click on Settings. Under Data Inputs, go to Files & Directories, scroll down to find the entry for `/home/kali/.zsh_history`, and delete it. Then, restart the process from Step 1 above to reconfigure the input.*

---
## Next Up
- Phase 6 – 
