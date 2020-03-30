from Client0 import Client

IP = "10.0.2.15"
PORT = 8080

FOLDER = "../Session-04/"
GENE = "FRAT1"

c1 = Client(IP, PORT)
c2 = Client(IP, PORT + 1)
print(c1)
print(c2)
s = Seq().read_fasta(FOLDER + GENE)
bases = str(s)
print(f"Gene {GENE}: {bases}")
LENGTH = 10
init_msg = f"Sending {GENE} gene to the server, in fragments of {LENGTH} bases"
c1.talk(init_msg)
c2.talk(init_msg)
for i in range(10):
    frag = bases[i*LENGTH:(i+1)*LENGTH]
    print(f"Fragment {i+1}: {frag}")
    msg = f"Fragment {i+1}: {frag}"
    if i%2:
        c2.talk(msg)
    else:
        c1.talk(msg)
