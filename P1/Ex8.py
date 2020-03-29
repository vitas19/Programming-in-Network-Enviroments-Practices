from Seq1 import Seq

seq_1 = Seq("")
seq_2 = Seq("ACTGA")
seq_3 = Seq("Invalid sequence")
for i,s in enumerate([seq_1,seq_2,seq_3]):
    print(f"Sequence {i}: (Length: {s.len()}) {s}")
    print(f"Bases: {s.count()}")
    print(f"Rev: {s.reverse()}")
    print(f"Comp: {s.complement()}")