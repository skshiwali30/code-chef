cases = int(input())
s1, s2 = '', ''
for case in range(cases):
    str = input()
    s1 = str[:len(str) // 2]
    if len(str) % 2 == 0:
        s2 = str[len(str)//2:]
    else:
        s2 = str[len(str)//2 + 1:]
    list1 = list(s1)
    list2 = list(s2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        print("YES")
    else:
        print("NO")
