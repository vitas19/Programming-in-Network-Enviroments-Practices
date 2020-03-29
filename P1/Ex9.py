from Seq1 import Seq

seq_1 = Seq("")

FOLDER = "../Session-04/"
GENE = "U5"

seq_1.read_fasta(FOLDER + GENE)
print(f"Sequence : (Length: {seq_1.len()}) {seq_1}")
print(f"  Bases: {seq_1.count()}")
print(f"  Rev:   {seq_1.reverse()}")
print(f"  Comp:  {seq_1.complement()}")