import pathlib

class Seq:
    def __init__(self, strbases):
        if strbases == '':
            print("NULL Seq created!")
            self.strbases = "NULL"
        else:
            for e in strbases:
                if e not in ["A", "C", "T", "G"]:
                    print("INVALID seq")
                    self.strbases = "ERROR"
                    return
            print("New sequence created!")
            self.strbases = strbases

    def __str__(self):
        return self.strbases

    def len(self):
        for e in self.strbases:
            if e not in ["A", "C", "T", "G"]:
                return 0
        return len(self.strbases)

    def count_base(self, base):
        count_base = 0
        if self.strbases == '':
            return 0
        else:
            for e in self.strbases:
                if e not in ["A", "C", "T", "G"]:
                    return 0
                else:
                    if e in base:
                        count_base += 1
            return count_base

    def count(self):
        bases = ["A", "C", "T", "G"]
        count_bases = []
        for base in bases:
            count_bases.append(self.count_base(base))
        dictionary = dict(zip(bases, count_bases))
        return dictionary

    def reverse(self):
        rev_seq = ''
        if self.strbases == 'NULL':
            return self.strbases
        else:
            for e in self.strbases[::-1]:
                if e not in ["A", "C", "T", "G"]:
                    rev_seq = 'ERROR'
                    return rev_seq

                else:
                    rev_seq += e
        return (rev_seq)

    def complement(self):
        comp_seq = ""
        if self.strbases == 'NULL':
            return self.strbases
        else:
            for e in self.strbases:
                if e not in ["A", "C", "T", "G"]:
                    comp_seq = 'ERROR'
                    return comp_seq
                else:
                    if e in "A":
                        comp_seq += "T"
                    if e in "T":
                        comp_seq += "A"
                    if e in "C":
                        comp_seq += "G"
                    if e in "G":
                        comp_seq += "C"
            return (comp_seq)

    def read_fasta(self, filename):
        file_lines = pathlib.Path(filename).read_text().split("\n")
        body = (file_lines[1:])
        self.strbases = ''.join(body)
        return (self)


    pass