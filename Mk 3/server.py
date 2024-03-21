import socket
import threading

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

def find_open_port(start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("localhost", port))
            return port
        except OSError:
            continue
    return None

HOST = '0.0.0.0'  # Listen on all available network interfaces
START_PORT = 8000  # Starting port for scanning
END_PORT = 9000    # Ending port for scanning

# Sabit bir port belirleme
MAIN_PORT = 8005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Sabit portu kullanabilir miyiz kontrol etme
    try:
        s.bind((HOST, MAIN_PORT))
        print("Main port found:", MAIN_PORT)
    except OSError:
        # Sabit port kullanılamıyorsa alternatif portlar arayarak kullanılabilir bir port bulma
        MAIN_PORT = find_open_port(START_PORT, END_PORT)
        if MAIN_PORT is None:
            print("No open port found.")
        else:
            print("Open port found:", MAIN_PORT)
        
        s.bind((HOST, MAIN_PORT))  # Bind the socket to the specified host and port
    s.listen()  # Start listening for incoming connections
    client_connections = []  # List to store client connections
    
    while True:
        conn, addr = s.accept()  # Accept incoming connection
        client_connections.append(conn)  # Add the new connection to the list
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # Create a new thread to handle the client
        thread.start()  # Start the thread
