from pathlib import Path
FILENAME = input("Enter a filename: ")
file_contents = Path(FILENAME).read_text()

seq_dna = file_contents
index_finish = seq_dna.find("\n")
seq_dna = seq_dna[:index_finish]
print(seq_dna)
