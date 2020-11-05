def sum(num):
    total = 0
    for i in range(1, num+1):
        total = total + i
    return total

puppy_list = []
for _ in range(int(input())):
    D, num = map(int, input().split())
    while D:
        summation = sum(num)
        num = summation
        D = D - 1
    puppy_list.append(num)

print(*puppy_list, sep="\n")