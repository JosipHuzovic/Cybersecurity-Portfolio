# Homelab Blueprint & Learning Journal

This document tracks the creation, evolution, and exercises performed in my self-hosted cybersecurity homelab. It includes setup steps, hands-on experiments, troubleshooting, and takeaways from each phase.

---

# Lab Setup Steps

## Phase 1: Core Components

For this first phase we'll just be installing the proper components to this lab.

- Downloaded **VMware Workstation**
- Installed **Kali Linux (Attacker)**
- Installed **Metasploitable2 (Target)**
- Configured both VMs to run on **Host-Only networking** for isolation and safety

## Phase 2: Identifying the Target Machine (Network Discovery)

After both the attacker (Kali Linux) and target (Metasploitable2) virtual machines are running, the first step is to locate the IP address of the vulnerable machine so that scanning and testing can begin.

Step 1: Ensure both VM's are running

Step 2: Open command prompt on the Kali Linux VM and run: 'ifconfig'

Step 3: After locating the subnet of the IP address we're attacking, type the command: 'nmap scan (Kali IP address)' (NEEDS CLARIFICATION)

Step 4: To get a better read on what versions each port on the vulnerable machine is running, try the command: 'nmap -sV (Target IP address)'

## Phase 3: Actual Hacking (MSFconsole)

