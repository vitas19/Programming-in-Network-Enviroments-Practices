dna = input("Enter a DNA sequence: ")
count_a = 0
count_c = 0
count_t = 0
count_g = 0
i = 0
while i < len(dna):
    if dna[i] == "A":
        count_a += 1
    elif dna[i] == "C":
        count_c += 1
    elif dna[i] == "T":
        count_t += 1
    elif dna[i] == "G":
        count_g += 1
    i += 1
print("Total length: ", len(dna))
print("A: ", count_a)
print("C: ", count_c)
print("T: ", count_t)
print("G: ", count_g)
