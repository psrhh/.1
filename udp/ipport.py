from scapy.all import sniff, IP, UDP

def udp_sniffer(packet):
    if packet.haslayer(UDP):
        print(f"Victim IP: {packet[IP].src}, Victim Port: {packet[UDP].sport}")
        print(f"Server IP: {packet[IP].dst}, Server Port: {packet[UDP].dport}")

# Start sniffing for UDP packets
sniff(filter="udp", prn=udp_sniffer, store=0)

