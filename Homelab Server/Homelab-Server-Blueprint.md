# Homelab Server Blueprint & Build Journal

**This is my active homelab and the successor to my original VMware-based lab. Where the legacy lab ran nested inside a desktop, this one runs on dedicated server hardware with real storage redundancy, network segmentation, and power protection. This document will be updated frequently as the build progresses.**

**Documentation Goal:** Everything here is written so that someone could replicate this build from scratch by following along. That means starting at the fundamentals and working up, so early entries will cover ground that may seem basic.

<hr>

## Table of Contents

- [Phase 1 – Core Components](#phase1)
  - [Hardware Inventory](#Hardware_Inventory)
  - [Topology – Core Setup](#Topology_Core_Setup)
- [Next Up](#Next_Up)

<hr>

<a name="phase1"></a><h1 align="center"><strong>Phase 1 – Core Components</strong></h1>

### Objective
Assemble the physical foundation of the homelab: install storage and memory into the NAS chassis, connect it to the network and power protection, and confirm the system reaches firmware before any operating system work begins.

### Overview
The legacy lab ran entirely inside VMware Workstation on my desktop, which meant no VM could stay online when I needed the machine for anything else. This build moves the lab onto dedicated hardware so it can run continuously.

The chassis is a UGREEN NASync DXP4800 Pro. It ships as a turnkey NAS appliance, but the underlying hardware is standard x86 with an Intel CPU, DDR5 SODIMM slots, four SATA bays, and two M.2 NVMe slots, which makes it a viable hypervisor host. This phase covers only the physical build. Nothing is installed yet.

<hr>

<a name="Hardware_Inventory"></a><h1 align="center"><strong>Hardware Inventory</strong></h1>

### Included With the DXP4800 Pro

| Component | Specification |
|---|---|
| CPU | Intel Core i3-1315U (6 cores / 8 threads, up to 4.5GHz turbo) |
| Memory | 8GB DDR5 SODIMM (2 slots, expandable to 96GB) |
| System Storage | 128GB built-in SSD, preloaded with UGOS Pro |
| Drive Bays | 4x SATA (sold diskless) |
| Expansion Storage | 2x M.2 NVMe slots |
| Networking | 1x 10GbE, 1x 2.5GbE |
| Video Out | 4K HDMI |

### Added To The Build

| Component | Specification | Purpose |
|---|---|---|
| Memory | Crucial 16GB DDR5-5600 CL46 SODIMM (1.1V) | Expands host memory to 24GB for VM headroom |
| NVMe SSD | Samsung 9100 PRO 1TB | Proxmox VE install and active VM disks |
| HDD | WD Red Plus 4TB | ZFS mirror member |
| HDD | Toshiba 4TB | ZFS mirror member |
| Power Protection | APC BR1500MS2 UPS | Graceful shutdown on power loss |

<p align="center"><em>The two mirror drives were deliberately sourced from different manufacturers. Two disks from the same brand and production batch carry correlated failure risk, and a mirror rebuild is exactly the moment when a second failure does the most damage.</em></p>

### A Note On Memory Configuration

The DXP4800 Pro ships with a single 8GB DDR5 SODIMM and leaves the second slot empty. That gave two options for the upgrade.

| Option | Result | Trade-off |
|---|---|---|
| Add the 16GB alongside the stock 8GB | 24GB total, flex mode | 16GB runs dual-channel interleaved, the remaining 8GB runs single-channel |
| Replace the stock 8GB with the 16GB | 16GB total, single-channel | Leaves a slot open for a matched module later, but wastes the stock stick |

I went with adding it, for 24GB total. On a hypervisor, memory capacity is the binding constraint long before memory bandwidth is. Splunk alone will comfortably take 8GB or more, pfSense wants 2GB, and every lab VM after that competes for what's left. Losing some interleaving on a third of the pool is a far cheaper price than being unable to keep VMs powered on.

Two things worth documenting for anyone replicating this:

- **The module is rated DDR5-5600, but the i3-1315U memory controller tops out at DDR5-5200.** It will train down to 5200 automatically with no configuration needed. Buying 5600 is not a mistake, it just will not run at its rated speed on this platform.
- **This platform does not support ECC memory.** This matters because ZFS is being used later in the build, and ZFS is frequently paired with ECC in production guidance. Non-ECC ZFS is still substantially safer than a non-checksumming filesystem, but the distinction should be stated plainly rather than glossed over.

<p align="center"><em>Mixing an aftermarket module with the factory stick is not guaranteed stable. Memtest86 should be run before trusting the system with anything, and that validation is covered in the steps below.</em></p>

### A Note On The 128GB System SSD

The DXP4800 Pro ships with a soldered 128GB SSD carrying UGOS Pro, UGREEN's stock operating system. Proxmox is going on the Samsung NVMe instead, and the 128GB drive is being left completely untouched.

The reason is recoverability. UGOS Pro is not distributed as a downloadable image, so if that drive gets wiped there is no straightforward way to restore the appliance to factory condition. Leaving it intact preserves a rollback path if the hypervisor experiment ever needs to be reversed, and keeps warranty and resale options open.

<p align="center"><em>This is a reversible-by-default decision. Wiping the stock OS would free almost nothing useful, while keeping it costs nothing and preserves an exit.</em></p>

<hr>

### Steps

#### 1. Power down and open the chassis
- Disconnect power and any network cables before opening the unit.
- The DXP4800 Pro exposes both the SODIMM slots and the M.2 slots without requiring full disassembly.

#### 2. Install the memory module
- Locate the empty SODIMM slot. The factory 8GB module stays in place.
- Insert the Crucial 16GB stick at roughly a 30-degree angle until the contacts seat fully, then press down until both retention clips click.
- Do not force it. DDR5 SODIMMs are keyed, and a module that will not seat is almost always misaligned rather than incompatible.

#### 3. Install the NVMe SSD
- Seat the Samsung 9100 PRO in the first M.2 slot at roughly a 30-degree angle, then press flat and secure the retaining screw.
- The second M.2 slot is left empty for now, reserved for future expansion.

#### 4. Install the SATA drives
- Insert the WD Red Plus and Toshiba drives into the drive bays.
- Note which physical bay each drive occupies. This matters later when identifying disks by serial number during ZFS pool creation, and it is far easier to record now than to work out afterward.

#### 5. Reassemble and connect
- Close the chassis and reconnect power through the UPS, not directly to the wall outlet.
- Connect the network cable. The 2.5GbE port is sufficient for initial setup.

#### 6. Verify the system posts
- Connect a monitor via HDMI and a USB keyboard.
- Power on and confirm the system reaches firmware.
- Enter BIOS and confirm all of the following before going any further:
  - Total memory reports **24576 MB / 24GB**
  - Memory speed reports **5200 MT/s**
  - The Samsung NVMe is detected
  - Both SATA drives are detected

<p align="center"><em>Confirming every component appears in BIOS at this stage prevents a great deal of confusion later. A drive that is seated poorly will often look fine physically while remaining completely invisible to the operating system, and a memory module that reports the wrong total is usually a seating problem rather than a defect.</em></p>

#### 7. Validate memory stability with Memtest86
- Write Memtest86 to a USB drive and boot from it.
- Run at least one full pass. Overnight is better.
- Any errors at all mean the mixed-module configuration is not stable. In that case, test each module individually to identify whether the fault is a specific stick or the pairing itself.

<p align="center"><em>This step is easy to skip and expensive to skip. Memory faults on a hypervisor host do not present as clean failures, they present as random VM crashes and silent data corruption that get misattributed to software for weeks.</em></p>

<hr>

<a name="Topology_Core_Setup"></a><h1 align="center"><strong>Topology – Core Setup</strong></h1>

<p align="center">
  <img src="Images/Topology_Core_Setup_Phase_1.png" alt="Core Setup Topology" style="max-width: 100%;">
</p>

<p align="center"><em>At this stage the topology is deliberately flat. The NAS sits on the existing home network with no segmentation, no hypervisor, and no monitoring. Every diagram that follows will be a revision of this one as the architecture develops.</em></p>

<hr>

<a name="Next_Up"></a><h1 align="center"><strong>Next Up</strong></h1>
- Coming Soon

<hr>

## About Me
Josip Huzovic  
josiphuzovic@gmail.com  
[LinkedIn Profile](https://www.linkedin.com/in/josip-huzovic)