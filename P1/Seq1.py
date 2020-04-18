from pathlib import Path


class Seq:
    NULL = "NULL"
    ERROR = "ERROR"

    def __init__(self, strbases=NULL):
        if strbases == self.NULL:
            print("NULL Seq created!")
            self.strbases = "NULL"
            return

        if not self.valid_str:
            self.starbases = self.ERROR
            print("INVALID seq")
            return

        print("New sequence created!")
        self.strbases = strbases

    def __str__(self):
        return self.strbases

    @staticmethod
    def valid_str(strbases):
        valid_bases = ['A', 'C', 'T', 'G']
        for b in strbases:
            if b not in valid_bases:
                return False
        return True

    def len(self):
        if self.strbases in [self.NULL, self.ERROR]:
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        return self.strbases.count(base)

    def count(self):
        bases = ["A", "C", "T", "G"]
        count_bases = []
        for base in bases:
            count_bases.append(self.count_base(base))
        dictionary = dict(zip(bases, count_bases))
        return dictionary

    def reverse(self):
        if self.strbases in [self.NULL, self.ERROR]:
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases in [self.NULL, self.ERROR]:
            return self.strbases
        else:
            comp_base = {"A": "T", "T": "A", "C": "G", "G": "C"}
            comp_seq = ""
            for b in self.strbases:
                comp_seq += comp_base[b]
            return comp_seq

    def read_fasta(self, filename):
        file_lines = Path(filename).read_text().split("\n")
        body = (file_lines[1:])
        self.strbases = "".join(body)
        return self
