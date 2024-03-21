import socket
import os
import random
from colorama import Fore, Style
import concurrent.futures

def get_username():
    return input("Enter your username: ")

def assign_color():
    # Function to assign a random color for the username
    colors = [
        Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN,
        Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX
    ]
    return random.choice(colors)

def is_port_open(server_host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_host, port))
        return port
    except ConnectionRefusedError:
        return None

def find_server_port(server_host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex((server_host, port))
            if result == 0:
                return port
    return None

def main():
    # Start the message receiver
    # Start the client message receiver in a new terminal
    username = get_username()
    user_color = assign_color()
    os.system("start python clientreceiver.py")

    # Server adresi ve başlangıç port numarası
    SERVER_HOST = '139.179.196.136'
    START_PORT = 8000
    END_PORT = 9000

    # Sabit portu kullanabilir miyiz kontrol etme
    server_port = find_server_port(SERVER_HOST, START_PORT, END_PORT)
    if server_port is None:
        print("No open port found.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, server_port))  # Connect to the server
        print("Connected to the server.", server_port)

        try:
            while True:
                # Get user input and send it to the server
                message = input("Enter the message to send to the server: ")
                full_message = f"{user_color}{username}{Style.RESET_ALL}: {message}"  # Add color to the username
                s.sendall(full_message.encode())  # Send the message to the server
        except KeyboardInterrupt:
            print("Closing...")
            s.close()  # Close the socket when interrupted

if __name__ == "__main__":
    main()
