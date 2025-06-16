from scapy.all import *

def p(packet):
	if packet.haslayer(TCP):
		print(packet.summary())
		packet.show()

sniff(filter="tcp",prn=p,iface="eth0")
