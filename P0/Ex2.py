from P0.Seq0 import *

FOLDER = "../Session-04/"
filename = "U5"

DNA_FILE = FOLDER + filename

# -- Open the DNA file
seq = seq_read_fasta(DNA_FILE)

print("------> Exercise 2")
print(f"DNA file: {filename}")

print("The first 20 bases are:")
print(seq[:20])
