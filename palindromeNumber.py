cases = int(input())
result_list = []
for case in range(cases):
    num = int(input())
    number = 0
    originalNum = num
    while num > 0:
        digit = num % 10
        number = number * 10 + digit
        num = num // 10
    if originalNum == number:
        result_list.append("wins")
    else:
        result_list.append("loses")

print(*result_list, sep="\n")