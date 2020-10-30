totalNum = int(input())
num_list = []
for num in range(totalNum):
    num_list.append(int(input()))

num_list.sort()
print(*num_list, sep="\n")