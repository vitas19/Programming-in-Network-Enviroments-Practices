from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(c)

print("Testing PING...")
print(c.talk("PING"))

print("Testing GET...")
for i in range(5):
    print(c.talk(f"GET {i}"))

print("Testing INFO...")
print(c.talk("INFO AACCGTA"))

print("Testing COMP...")
print(c.talk("COMP AACCGTA"))

print("Testing REV...")
print(c.talk("REV AACCGTA"))

print("Testing GENE...")
for gene in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]:
    print(f"GENE {gene}")
    print(c.talk(f"GENE {gene}"))
