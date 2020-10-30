testCases = int(input())
rem_list = []
for case in range(testCases):
    num1, num2 = map(int, input().split())
    rem = num1 % num2
    rem_list.append(rem)
print(*rem_list, sep="\n")