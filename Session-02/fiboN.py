def fibon(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        return b

print("5th fibonacci term:", fibon(5))
print("10th fibonacci term:", fibon(10))
print("15th fibonacci term:", fibon(15))