def gcd(num1, num2):
    while num2:
        num1, num2 = num2, (num1 % num2)
    return num1

def lcm(num1, num2):
    lcm = (num1 * num2) // gcd(num1, num2)
    return lcm

cases = int(input())
for _ in range(cases):
    num1, num2 = map(int, input().split(" "))
    print(gcd(num1, num2), lcm(num1, num2))

