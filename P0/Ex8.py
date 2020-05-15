from P0.Seq0 import *
filename = ["U5", "ADA", "FRAT1", "FXN"]
FOLDER = "../Session-04/"
for gene_file in filename:
    print("Gene ", gene_file, ": Most frequent Base: ", process_genes(FOLDER+gene_file)[1])
