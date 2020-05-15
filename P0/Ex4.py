from P0.Seq0 import *

filename = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "T", "G"]
FOLDER = "../Session-04/"
for gene_file in filename:
    print("Gene", gene_file, ":")
    for base in bases:
        print(" ", base, ":", seq_count_base(FOLDER+gene_file, base))
