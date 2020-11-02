cases = int(input())

var_list = []
for case in range(cases):
    var = int(input())
    if var < 10:
        var_list.append("Thanks for helping Chef!")
    else:
        var_list.append("-1")

print(*var_list, sep="\n")