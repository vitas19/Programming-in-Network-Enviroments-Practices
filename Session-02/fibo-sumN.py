def fibon(n):
    a = 0
    b = 1
    sumn = 1
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
            sumn += b
        return sumn

print ("Sum of the first 5 terms of the Fibonacci series: ",fibon(5))
print ("Sum of the first 10 terms of the Fibonacci series: ",fibon(10))

