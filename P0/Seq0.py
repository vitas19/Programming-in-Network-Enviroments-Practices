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
    file_contents = Path(seq).read_text()
    index_start = file_contents.find("\n")
    seq_dna = file_contents[index_start + 1:]
    seq_dna = seq_dna.replace("\n", "")
    count_base = 0
    for character in seq_dna:
        if character == base:
            count_base += 1
    return (count_base)

def seq_count(seq):
    from pathlib import Path
    file_contents = Path(seq).read_text()
    index_start = file_contents.find("\n")
    seq_dna = file_contents[index_start + 1:]
    seq_dna = seq_dna.replace("\n", "")
    count_base = 0
    bases = ["A", "T", "C", "G"]
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in bases:
        for character in seq_dna:
            if character == base:
                count_base += 1
                d[character] = count_base
        count_base = 0
    return (d)

def seq_reverse(seq):
    from pathlib import Path
    file_contents = Path(seq).read_text()
    index_start = file_contents.find("\n")
    seq_dna = file_contents[index_start + 1:]
    seq_dna = seq_dna.replace("\n", "")[0:20]
    rev_dna = seq_dna[::-1]
    return seq_dna, rev_dna

def seq_complement(seq):
    from pathlib import Path
    file_contents = Path(seq).read_text()
    index_start = file_contents.find("\n")
    seq_dna = file_contents[index_start + 1:]
    seq_dna = seq_dna.replace("\n", "")[0:20]
    compl_seq = ""
    for character in seq_dna:
        if character == "A":
            compl_seq = compl_seq + "T"
        elif character == "T":
            compl_seq = compl_seq + "A"
        elif character == "C":
            compl_seq = compl_seq + "G"
        elif character == "G":
            compl_seq = compl_seq + "C"
    return seq_dna, compl_seq

def process_genes(seq):
    from pathlib import Path
    file_contents = Path(seq).read_text()
    index_start = file_contents.find("\n")
    seq_dna = file_contents[index_start + 1:]
    seq_dna = seq_dna.replace("\n", "")
    count_base = 0
    bases = ["A", "T", "C", "G"]
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in bases:
        for character in seq_dna:
            if character == base:
                count_base += 1
                d[character] = count_base
        count_base = 0
    max_value = max(d.values())
    max_keys = [k for k, v in d.items() if v == max_value]
    return max_value, max_keys

