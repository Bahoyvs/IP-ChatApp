import socket

HOST = '127.0.0.1'        # IP address of the server
PORT = 65432              # Port number of the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to the server
    while True:
        data = s.recv(1024)  # Receive data from the server
        if not data:
            print("Server connection closed.")
            break
        print(data.decode())  # Print the received data
