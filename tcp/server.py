import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 9998))
server_socket.listen(5)
print("[*] Server listening on port 9998...")

try:
    while True:
        client_socket, addr = server_socket.accept()
        print(f"[+] Accepted connection from {addr}")
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received from client: {data.decode('utf-8', errors='ignore')}")
                client_socket.send(b"ACK: " + data)
        except Exception as e:
            print(f"[!] Error: {e}")
        finally:
            client_socket.close()
except KeyboardInterrupt:
    print("\n[*] Server shutting down...")
finally:
    server_socket.close()
