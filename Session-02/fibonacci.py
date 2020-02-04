n = 11
a = 0
b = 1
if n < 0:
    print("Incorrect input")
elif n == 0:
    print("0")
elif n == 1:
    print("1")
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(b)