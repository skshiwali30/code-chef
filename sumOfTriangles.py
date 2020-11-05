def solve(arr, n, i, j, d):
    if i == n:
        return 0
    if j > i:
        return 0
    if (i, j) in d:
        return d[(i,j)]
    temp = arr[i][j] + max(solve(arr, n, i+1, j, d), solve(arr, n, i+1, j+1, d))
    d[(i,j)] = temp
    return temp

cases = int(input())
for case in range(cases):
    num = int(input())
    arr_list = []
    for i in range(num):
        l = [int(x) for x in input().split()]
        arr_list.append(l)
    arr_dict = {}
    print(solve(arr_list, num, 0, 0, arr_dict))