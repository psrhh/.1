import socket

victim_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = "192.168.126.128"

server_port = 9998

while True:

message = input("Enter message: ")

victim_socket.sendto(message.encode(), (server_ip, server_port))