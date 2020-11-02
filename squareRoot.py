import math

cases = int(input())
squareRoot_list = []
for case in range(cases):
    num = int(input())
    squareRoot_num = int(math.sqrt(num))
    squareRoot_list.append(squareRoot_num)

print(*squareRoot_list, sep="\n")