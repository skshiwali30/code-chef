cases = int(input())

expenses_list = []
for case in range(cases):
    quan, price = map(int, input().split())
    expenses = quan * price
    if quan > 1000:
        expenses = expenses - (0.1 * expenses)
    expenses_list.append("{0:.6f}".format(expenses))

print(*expenses_list, sep="\n")