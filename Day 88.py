#Day 88: Chat application


#Implement a chat application using sockets.

#Server Code (server.py)

import socket
import threading

# Server Configuration
HOST = '127.0.0.1'
PORT = 5555

# List to store connected clients
clients = []

# Function to handle client messages
def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{address}] {message}")
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            print(f"[DISCONNECTED] {address} disconnected.")
            break

# Function to send messages to all clients
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)

# Function to start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

# Start the server
if __name__ == "__main__":
    start_server()



#Client Code (client.py)

import socket
import threading

# Client Configuration
HOST = '127.0.0.1'
PORT = 5555

# Function to receive messages
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\n{message}")
        except:
            print("[ERROR] Connection lost.")
            break

# Function to send messages
def send_messages(client_socket):
    while True:
        message = input("")
        if message.lower() == 'exit':
            client_socket.close()
            break
        client_socket.send(message.encode('utf-8'))

# Function to start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("[CONNECTED] Connected to the chat server. Type 'exit' to leave.")

    # Start receiving and sending messages in separate threads
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

# Start the client
if __name__ == "__main__":
    start_client()


#import socket
import threading

# Client Configuration
HOST = '127.0.0.1'
PORT = 5555

# Function to receive messages
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\n{message}")
        except:
            print("[ERROR] Connection lost.")
            break

# Function to send messages
def send_messages(client_socket):
    while True:
        message = input("")
        if message.lower() == 'exit':
            client_socket.close()
            break
        client_socket.send(message.encode('utf-8'))

# Function to start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("[CONNECTED] Connected to the chat server. Type 'exit' to leave.")

    # Start receiving and sending messages in separate threads
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

# Start the client
if __name__ == "__main__":
    start_client()

# This code snippet demonstrates a simple chat application using sockets in Python. The server code (server.py) listens for incoming connections from clients and handles messages sent by clients. The client code (client.py) connects to the server and allows users to send and receive messages in real-time.  
