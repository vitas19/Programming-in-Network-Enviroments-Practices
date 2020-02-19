from Seq0 import *
filename = ["U5", "ADA", "FRAT1", "FXN"]
FOLDER = "../Session-04/"
for gene_file in filename:
    print("Gene ", gene_file, "---> Length: ", seq_len(FOLDER+gene_file))
