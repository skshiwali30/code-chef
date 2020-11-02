cases = int(input())
max2_list = []
for case in range(cases):
    input_list = list(map(int, input().split()))
    input_list.sort(reverse=True)
    max2_list.append(input_list[1])

print(*max2_list, sep="\n")

