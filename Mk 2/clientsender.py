import socket
import os
import random
from colorama import Fore, Style

HOST = '139.179.235.79'  # IP address of the server
PORT = 65432        # Port number of the server

def get_username():
    return input("Enter your username: ")

def assign_color():
    # Function to assign a random color for the username
    colors = [
        Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN,
        Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX
    ]
    return random.choice(colors)

def main():
    # Start the message receiver
    # Start the client message receiver in a new terminal
    username = get_username()
    user_color = assign_color()
    os.system("start python clientreceiver.py")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))  # Connect to the server
        print("Connected to the server.")

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
