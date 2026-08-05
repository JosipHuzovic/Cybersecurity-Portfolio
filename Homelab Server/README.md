<h1 align="center"><strong>Current Personal Homelab Server Project</strong></h1>

**This is my active homelab and the successor to my original VMware-based lab. It runs on dedicated server hardware with proper storage redundancy, network segmentation, and power protection. Unlike my previous lab, this environment is persistent and will be updated frequently as services are added and configurations mature.**

This lab moves beyond simulated enterprise systems and into actually operating one. This environment stays online continuously, generating real baseline traffic and log volume to tune detections against.

**Documentation Goal:** Everything here is written so that someone could replicate this
build from scratch by following along. That means starting at the fundamentals and
working up, so early entries will cover ground that may seem basic.

---
## Why I Rebuilt
My first homelab ran entirely inside VMware Workstation on my desktop. It taught me fundamentals, but with hard ceilings:
- VMs could not stay running when the host was needed for anything else
- No storage redundancy, so a disk failure meant losing all lab state
- Nested virtualization made VLAN segmentation unreliable and hard to trust
- No power protection, so an outage meant unclean shutdowns and corrupted VM disks

Every one of those is addressed by dedicated hardware in the current build.

---
## Hands-On Experience With
- Deploying and administering a bare-metal type 1 hypervisor (Proxmox VE)
- Designing ZFS storage layouts with redundancy and snapshot scheduling
- Building segmented VLAN architecture with default-deny inter-VLAN policy
- Operating a persistent SIEM against continuously generated log data
- Managing infrastructure lifecycle: backups, updates, and graceful shutdown handling
- Tuning detections against realistic baseline traffic rather than synthetic-only data

---
## Setup
- **Chassis:** UGREEN DXP4800 Plus (4-bay, repurposed as hypervisor host)
- **Boot & VM Storage:** Samsung 9100 PRO 1TB NVMe
- **Bulk Storage:** WD Red Plus + Toshiba 4TB HDD (ZFS mirror)
- **Power Protection:** APC BR1500MS2 UPS

---
## Tooling & Stack (Purpose-Driven)
- **Proxmox VE** – bare-metal hypervisor with native ZFS, no licensing limits, and direct Debian shell access when the web UI is not enough
- **ZFS** – mirrored pool for backups and log retention, with snapshot capability and checksum-based integrity protection
- **pfSense** – virtualized edge firewall handling routing, VLAN segmentation, and perimeter policy
- **Splunk** – central log platform ingesting firewall, system, and authentication events
- **APC UPS + NUT** – monitors power state and triggers graceful shutdown before battery exhaustion
- **Persistent Lab VMs** – always-on hosts generating realistic baseline activity for detection tuning

---
## Design Decisions
- **Mismatched drive brands in the mirror** were deliberate. Two disks from the same manufacturer and production batch have correlated failure risk, and a mirror rebuild is exactly when a second failure hurts most.
- **NVMe separated from bulk storage** so VM disk I/O never competes with backup and log retention writes.
- **Default-deny between VLANs** with explicit allow rules only where a scenario requires it, so lateral movement has to be granted intentionally rather than assumed.
- **Attack VMs isolated with no route to the production LAN**, keeping offensive testing fully contained.
- **UPS integration over a plain battery backup** because unclean hypervisor shutdowns risk corrupting every VM on the host at once, not just one machine.

---
## Network Topology

**WIP**

---
## Key Takeaways
- Running persistent infrastructure is a different skill from building a lab for one exercise, and the failure modes are the ones that actually show up at work
- Storage design, power handling, and backup verification matter as much as the security tooling sitting on top of them
- Detections tuned against real baseline noise behave very differently from detections tuned against clean synthetic data

---
## Project Phases & Milestones

This lab is being built in structured phases, each building on the last, progressing from bare hardware to a fully monitored and segmented environment.
Some of these phases are already in production but are still being implemented into the blueprint

| Phase | Focus Area                                                     | Status        |
|-------|----------------------------------------------------------------|---------------|
| 1     | Hardware Provisioning: NAS, NVMe, HDDs, UPS                   | ✅ Complete    |
| 2     | Hypervisor Deployment: Proxmox VE install and boot config     | ✅ Complete    |
| 3     | Storage Layout: ZFS mirror creation and pool configuration    | 🔄 Complete    |
| 4     | Power Protection: UPS integration and graceful shutdown test  | ✅ Complete    |
| 5     | Network Segmentation: pfSense deployment and VLAN buildout    | 🔄 In Progress |
| 6     | SIEM Deployment: Splunk install and log source onboarding     | 🔄 In Progress |
| 7     | Detection Engineering: Build and tune alert use-case library  | ⬜ Planned     |
| 8     | Backup Automation: Scheduled snapshots and restore validation | ⬜ Planned     |
| 9     | Identity Services: Directory and access control testing       | ⬜ Planned     |
| 10    | Incident Response: Full documented IR walkthrough             | ⬜ Planned     |

**Goal**: Operate a persistent, production-style environment where detection, response, and infrastructure management can be practiced against real system behavior rather than isolated one-off scenarios.

---
## Notes
All activity in this environment is conducted on hardware I own, within isolated network segments, for educational and demonstrative purposes. No testing is performed against systems or networks I do not control.

---
## About Me
Josip Huzovic  
josiphuzovic@gmail.com  
[LinkedIn Profile](https://www.linkedin.com/in/josip-huzovic)