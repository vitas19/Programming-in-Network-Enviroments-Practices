from Client0 import Client

IP = "10.0.2.15"
PORT = 8080

c = Client(IP, PORT)
print(c)
c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing")