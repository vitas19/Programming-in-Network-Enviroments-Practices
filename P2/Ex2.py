from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(f"Connection to SERVER at {c.ip}, PORT: {c.port}")
