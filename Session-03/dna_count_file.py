filename = input("Enter a filename: ")
with open(filename, "r") as f:
    count_a = 0
    count_c = 0
    count_t = 0
    count_g = 0
    i = 0
    for line in f:
        for character in line:
            if character == "A":
                count_a += 1
            elif character == "C":
                count_c += 1
            elif character == "T":
                count_t += 1
            elif character == "G":
                count_g += 1
            i += 1
print("Total length: ", count_a+count_c+count_g+count_t)
print("A: ", count_a)
print("C: ", count_c)
print("T: ", count_t)
print("G: ", count_g)
