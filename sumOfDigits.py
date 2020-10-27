lines = int(input())
sum_list = []
for line in range(lines):
    num = int(input())
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10
    sum_list.append(sum)

print(*sum_list, sep="\n")