# Simple code meant to show packets on Wireshark in a beaconing way

import socket
import time

# Target IP and port (use your own machine, test VM, or a reserved documentation IP)

target_ip = "192.0.2.123" # Reserved Documentation IP
target_port = 4444 # Unused Port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Loops forever, sending a fake beacon every 5 seconds
while True:
    message = b"BEACON - Simulated Beacon Ping"
    sock.sendto(message, (target_ip, target_port))
    print(f"Sent beacon to {target_ip}:{target_port}")
    time.sleep(5)  # Wait 5 seconds before next packet
