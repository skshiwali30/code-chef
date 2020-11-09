cases = int(input())
result_list = []
prime = False
for case in range(cases):
    num = int(input())
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
        else:
            prime = True
    if num == 2 or prime:
        result_list.append("yes")
    else:
        result_list.append("no")
print(*result_list, sep="\n")