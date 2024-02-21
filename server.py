import socket
import threading

HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 65432       # Port number of the server

def handle_client(conn, addr):
    print('Connection established:', addr)
    with conn:
        try:
            while True:
                data = conn.recv(1024)  # Receive data from the client
                if not data:
                    print('Connection closed:', addr)
                    break
                print('Client message:', data.decode())
                # Send the received message to all connected clients
                for client_conn in client_connections:
                    if client_conn != conn:  # Avoid sending data back to the sender
                        try:
                            client_conn.sendall(data)
                        except Exception as e:
                            print("Error:", e)
        except Exception as e:
            print("Error:", e)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Bind the socket to the specified host and port
    s.listen()  # Start listening for incoming connections
    client_connections = []  # List to store client connections
    while True:
        conn, addr = s.accept()  # Accept incoming connection
        client_connections.append(conn)  # Add the new connection to the list
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # Create a new thread to handle the client
        thread.start()  # Start the thread
