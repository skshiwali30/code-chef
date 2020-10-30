import math

testCases = int(input())
fact_list = []
for case in range(testCases):
    num = int(input())
    fact = math.factorial(num)
    fact_list.append(fact)

print(*fact_list, sep="\n")


