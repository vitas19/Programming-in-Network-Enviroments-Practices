import socket

IP = "10.0.2.15"
PORT = 8080

# Step 1: creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: bind the socket to the servers IP and PORT
ls.bind((IP, PORT))

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Step 3: convert into a listening socket
ls.listen()

print("Server is configured")

while True:

    try:
        # Step 4: wait for client to connect
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server is done")
        ls.close()
        exit()

    else:
        # Step 5: receiving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        print(f"Received message: {msg}")

        # Step 6: send a response message to the client
        response = "Hi! I am a happy server :)\n"
        cs.send(response.encode())

        cs.close()
