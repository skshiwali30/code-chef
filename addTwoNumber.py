lines = int(input())
sum_list = []
for i in range(lines):
    a, b = map(int, input().split())
    sum = a + b
    sum_list.append(sum)
print(*sum_list, sep="\n")