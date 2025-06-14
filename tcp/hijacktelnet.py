import socket

attacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
attacker_socket.bind(("0.0.0.0", 9999))
attacker_socket.listen(5)
print("[*] Attacker server listening on port 9999...")

try:
    while True:
        client_socket, addr = attacker_socket.accept()
        print(f"[+] Connection hijacked from {addr}")
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(data.decode('utf-8', errors='ignore'))
                client_socket.send(b"You have been hacked!\n")
        except Exception as e:
            print(f"[!] Attacker error: {e}")
        finally:
            client_socket.close()

except KeyboardInterrupt:
    print("\n[*] Attacker server shutting down...")
finally:
    attacker_socket.close()

