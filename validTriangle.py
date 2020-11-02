cases = int(input())
valid_list = []

for case in range(cases):
    a, b, c = map(int, input().split())
    sumOfTriangle = a + b + c
    if sumOfTriangle == 180:
        valid_list.append("YES")
    else:
        valid_list.append("NO")

print(*valid_list, sep="\n")