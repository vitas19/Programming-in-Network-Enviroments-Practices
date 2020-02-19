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

def seq_count_base(seq, base):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    index_start = file_contents.find("\n")
    seq_dna = file_contents[index_start + 1:]
    seq_dna = seq_dna.replace("\n", "")
    count_a = 0
    count_c = 0
    count_t = 0
    count_g = 0
    for character in seq_dna:
        if character == "A":
            count_a += 1
        elif character == "C":
            count_c += 1
        elif character == "T":
            count_t += 1
        elif character == "G":
            count_g += 1
    return (count_a, count_c, count_t, count_g)