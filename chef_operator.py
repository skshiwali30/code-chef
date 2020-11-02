cases = int(input())

operator_list = []
for case in range(cases):
    num1, num2 = map(int, input().split())
    if num1 > num2:
        operator_list.append(">")
    elif num1 < num2:
        operator_list.append("<")
    else:
        operator_list.append("=")
print(*operator_list, sep="\n")