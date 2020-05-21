import socket
import termcolor
from Seq1 import Seq

sequences = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
             "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
             "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
             "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
             "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]
bases = ["A", "C", "T", "G"]
folder = "../Session-04/"
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

IP = "127.0.0.1"
PORT = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((IP, PORT))

ls.listen()

print("Server configured")
while True:
    print("Waiting for clients")
    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped")
        ls.close
        exit()

    else:
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()
        comps = msg.split(" ")

        if len(comps) >= 2:
            comp1 = comps[0]
            comp2 = comps[1]
        else:
            comp1 = msg

        if comp1 == "PING":
            termcolor.cprint("PING command!", 'green')
            response = "OK!\n"

        elif comp1 == "GET":
            for e in range(len(sequences)):
                if e == int(comp2):
                    termcolor.cprint("GET", 'green')
                    response = sequences[e]

        elif comp1 == "INFO":
            seq0 = Seq(comp2)
            termcolor.cprint("INFO", 'green')
            response = f"Sequence: {comp2} \n"
            response += f"Total length: {seq0.len()} \n"
            for e in bases:
                percentage = round(seq0.count_base(e) * (100 / seq0.len()), 2)
                response += f"{e}: {seq0.count_base(e)} ({percentage}%) \n"

        elif comp1 == "COMP":
            seq0 = Seq(comp2)
            termcolor.cprint("COMP", 'green')
            response = seq0.complement()

        elif comp1 == "REV":
            seq0 = Seq(comp2)
            termcolor.cprint("REV", 'green')
            response = seq0.reverse()

        elif comp1 == "GENE":
            seq0 = Seq("")
            seq0 = seq0.read_fasta(folder + comp2)
            termcolor.cprint("GENE", 'green')
            response = seq0.reverse()

    print(response, "\n")
    cs.send(response.encode())
    cs.close()
