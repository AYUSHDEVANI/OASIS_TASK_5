
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


# Main Client Function
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        message = input("Enter message: ")
        client.send(message.encode())

if __name__ == "__main__":
    start_client()