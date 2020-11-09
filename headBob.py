result_list = []
for _ in range(int(input())):
    num = int(input())
    str = input()
    count = 1
    for char in str[0:num]:
        if char == 'I':
            result_list.append("INDIAN")
            count = 0
            break
        elif char == 'Y':
            result_list.append("NOT INDIAN")
            count = 0
            break

    if count == 1:
        result_list.append("NOT SURE")

print(*result_list, sep="\n")
