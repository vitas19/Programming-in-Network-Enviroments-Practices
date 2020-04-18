from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)
print("Sending a message to the server...")
response = c.talk("Testing")
print(f"Response: {response}")
