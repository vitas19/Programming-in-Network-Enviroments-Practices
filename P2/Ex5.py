from Client0 import Client

IP = "10.0.2.15"
PORT = 8080

FOLDER = "../Session-04/"
GENE = "U5"

c = Client(IP, PORT)
print(c)
s = Seq().read_fasta(FOLDER + GENE)
c.debug_talk(f"Sending {GENE} gene to the server")
c.debug_talk(str(s))