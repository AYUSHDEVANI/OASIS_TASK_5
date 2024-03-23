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

# Main Server function
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server running on {HOST} : {PORT}")

    while True:
        client_socket, address = server.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

if __name__ == "__main__":
    start_server()