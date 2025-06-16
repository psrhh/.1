import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = "192.168.220.132"
server_port = 9998

client_socket.connect((server_ip, server_port))
print(f"[*] Connected to {server_ip}:{server_port}")

try:
    while True:
        message = input("Enter message to send: ")
        client_socket.send(message.encode())
        response = client_socket.recv(1024)
        print(f"Server sequence number: {response.decode()}")

except KeyboardInterrupt:
    print("\n[*]disconnecting...")

finally:
    client_socket.close()

