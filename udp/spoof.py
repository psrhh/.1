from scapy.all import IP, UDP, send

p = IP(src="192.168.220.133", dst="192.168.220.132") / UDP(sport=33772, dport=9998) / "This is broken"
send(p)
print("[+] Spoofed UDP packet sent!")

