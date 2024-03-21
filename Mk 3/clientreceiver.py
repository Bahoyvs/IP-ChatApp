import socket

def find_open_port(start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("localhost", port))
            return port
        except OSError:
            continue
    return None

def find_server_port(server_host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((server_host, port))
            return port
        except ConnectionRefusedError:
            continue
    return None

# Server adresi ve başlangıç port numarası
SERVER_HOST = '139.179.196.136'
START_PORT = 8000
END_PORT = 9000

# Sabit portu kullanabilir miyiz kontrol etme
server_port = find_server_port(SERVER_HOST, START_PORT, END_PORT)
if server_port is None:
    # Sabit port kullanılamıyorsa alternatif portlar arayarak kullanılabilir bir port bulma
    server_port = find_open_port(START_PORT, END_PORT)
    if server_port is None:
        print("No open port found.")
        exit()

print("Server is using port:", server_port)

HOST = SERVER_HOST        # IP address of the server
PORT = server_port       # Port number of the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to the server
    while True:
        data = s.recv(1024)  # Receive data from the server
        if not data:
            print("Server connection closed.")
            break
        print(data.decode())  # Print the received data
