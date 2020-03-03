import socket
import termcolor

IP = "212.128.253.151"
PORT = 8080

# Step 1: creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: bind the socket to the servers IP and PORT
ls.bind((IP, PORT))

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Step 3: convert into a listening socket
ls.listen()

number_connections = 0

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
        number_connections += 1
        print(f"CONNECTION {number_connections}. Client IP,PORT: {client_ip_port}")
        # Step 5: receiving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        print("Message received: ", end="")
        termcolor.cprint(msg, "green")

        # -- Send a response message to the client
        response = "ECHO: " + msg + "\n"

        cs.send(response.encode())

        cs.close()
