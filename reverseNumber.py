testCases = int(input())
reverse_list = []
for case in range(testCases):
    num = int(input())
    revNum = 0
    while num > 0:
        digit = num % 10
        revNum = revNum * 10 + digit
        num = num // 10
    reverse_list.append(revNum)

print(*reverse_list, sep="\n")