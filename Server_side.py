import socket
import threading


# Server Configuration
HOST = "127.0.0.1"
PORT = 8888

# List to store client connections
clients = []

# Function to handle client connections
def handle_client(client_socket, address):
    while True:
        message = client_socket.recv(1024).decode()
        for client in clients:
            if client != client_socket:
                client.send(message.encode())

