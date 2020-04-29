import socket

PORT = 8080
IP = "127.0.0.1"

while True:
    # Ask the user for a message
    message = input("Message to send: ")
    # Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Establish the connection to the server (IP, PORT)
    s.connect((IP, PORT))
    # Send data
    s.send(str.encode(message))
    # Closing the socket
    s.close()