from Seq1 import Seq

FOLDER = "../Session-04/"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
BASES = ['A', 'T', 'C', 'G']

for gene in GENES:
    seq = Seq("").read_fasta(FOLDER + gene)
    dic = seq.count()
    values = list(dic.values())
    maxim = max(values)
    print(f"Gene {gene}: Most frequent base: {BASES[values.index(maxim)]}")