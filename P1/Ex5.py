from Seq1 import Seq

seq_1 = Seq("")
seq_2 = Seq("ACTGA")
seq_3 = Seq("Invalid sequence")
for i,s in enumerate([seq_1, seq_2, seq_3]):
    print(f"Sequence {i}: (Length: {s.len()}) {s}")
    for base in ["A", "T", "C", "G"]:
        print(f"{base}:{s.count_base(base)}", end=", ")
    print()