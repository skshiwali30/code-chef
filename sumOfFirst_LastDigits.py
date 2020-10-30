testCases = int(input())
sum_list = []
for case in range(testCases):
    num = int(input())
    lastDigit = num % 10
    firstDigit = 0
    while num > 0:
        firstDigit = num
        num = num // 10
    sum = firstDigit + lastDigit
    sum_list.append(sum)

print(*sum_list, sep="\n")