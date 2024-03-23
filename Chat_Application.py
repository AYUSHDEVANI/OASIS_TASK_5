
import socket
import threading

# Client configuration
HOST = "127.0.0.1"
PORT = 8888


# Function to receive messages from server 
def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        print(message)

        