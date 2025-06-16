import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9998))
print("[*] UDP Server is listening...")

try:
    while True:
        try:
            data, addr = s.recvfrom(1024)
            try:
                decoded = data.decode('utf-8')
            except UnicodeDecodeError:
                decoded = f"[Non-UTF-8 data received: {data}]"
            print(f"Received from {addr}: {decoded}")
        except KeyboardInterrupt:
            print("\n[*] Server shutting down...")
            break
        except Exception as e:
            print(f"[!] Error: {e}")
finally:
    s.close()
    print("[*] Socket closed.")

