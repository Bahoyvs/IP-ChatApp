# IP-ChatApp
This is a simple chat application built in Python using sockets for communication between clients and a server. It allows multiple clients to connect to a central server and send messages to each other.

# Features
* Multiple clients can connect to the server simultaneously.
* Each client is assigned a unique color for their messages.
* Users can enter a username before sending messages.
* Messages are displayed in real-time on the server and other clients.
* Clients can disconnect from the server gracefully without affecting other clients.
# Usage
* Run the server (server2.py) on a machine with a public IP address.
* Run the client message sender (clientsender.py) to send messages to the server. Upon running the sender, the client message receiver (clientreceiver.py) will automatically open in a separate terminal.
* Enter a username when prompted.
* Send messages to the server, which will be broadcasted to all connected clients.
* Press Ctrl + C to gracefully disconnect from the server.
# Requirements
* Python 3.x
* Colorama library for colorized output (install using pip install colorama)
