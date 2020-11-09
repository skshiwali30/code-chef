for case in range(int(input())):
    noOfElement = int(input())
    arr_list = list(map(int, input().split()))
    arr_list.sort()
    print(arr_list[0] + arr_list[1])