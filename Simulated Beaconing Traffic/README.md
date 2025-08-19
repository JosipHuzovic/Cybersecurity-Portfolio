<h1 align="center"><strong>Simulated Beacon Traffic</strong></h1>

**This project was created while studying for CompTIA Network+ to put concepts of traffic analysis and Wireshark filtering into practice.**

---

This project simulates an extremely simple **malware-like beaconing behavior in a safe, controlled way** by sending repeated network packets to a designated IP and port using the Python script in [simulated_beacon.py](./simulated_beacon.py). The goal is to demonstrate how traffic patterns can be identified in a packet sniffer like Wireshark, without deploying any harmful code.  

The script generates UDP traffic at regular intervals, mimicking the way real malware communicates with a command-and-control (C2) server — but in a way that is **entirely safe and non-malicious**. When captured, the traffic reveals recognizable patterns such as consistent timing, repeated payloads, and unusual port usage — all common red flags in network monitoring and threat hunting.  



---



## Educational Purpose

This simulation is built for **educational and demonstrative use only** and can be followed along at [Sim-Beacon-Blueprint](./Sim-Beacon-Blueprint).  
  
This project provides a completely safe way to:

- Practice detecting beaconing traffic with Wireshark filters

- Explore how attackers use repetitive patterns to maintain persistence

- Build intuition for differentiating between normal web traffic and potential indicators of compromise



All testing should be conducted in isolated or controlled environments. No sensitive or external systems are targeted.


---
## About Me
Josip Huzovic  
josiphuzovic@gmail.com  
[LinkedIn Profile](https://www.linkedin.com/in/josip-huzovic)