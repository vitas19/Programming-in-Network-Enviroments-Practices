def seq_ping():
    print("OK!")

def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    index_start = file_contents.find("\n")
    seq_dna = file_contents[index_start + 1:]
    seq_dna = seq_dna.replace("\n", "")
    return seq_dna

def seq_len(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    index_start = file_contents.find("\n")
    seq_dna = file_contents[index_start + 1:]
    seq_dna = seq_dna.replace("\n", "")
    return len(seq_dna)