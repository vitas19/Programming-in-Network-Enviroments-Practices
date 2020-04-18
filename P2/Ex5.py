from Client0 import Client
from Seq1 import Seq

IP = "127.0.0.1"
PORT = 8080

FOLDER = "../Session-04/"
GENE = "U5"

c = Client(IP, PORT)
print(c)
s = Seq("").read_fasta(FOLDER + GENE)
c.debug_talk(f"Sending {GENE} gene to the server")
c.debug_talk(str(s))
