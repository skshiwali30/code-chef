import math

def isPrime(num):
    flag = False
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
        else:
            flag = True
    if num == 2 or flag:
        return True
    else:
        return False

def nextPrime(N):
    prime = N
    found = False
    while (not found):
        prime = prime + 1

        if (isPrime(prime) == True):
            found = True
    return prime

for _ in range(int(input())):
    x, y = map(int, input().split())
    num = x + y
    z = nextPrime(num)
    print(z - num)