from scapy.all import *

def sniff_packets(packet):
    if packet.haslayer(TCP):
        print(packet.summary())
        packet.show()

sniff(filter="tcp", prn=sniff_packets, iface="eth0")

