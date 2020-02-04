# 1+2+3+...+20
# 01+2+...+100


def sumn(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res


print("Total sum of 1-20: ", sumn(20))
print("Total sum of 1-100: ", sumn(100))
