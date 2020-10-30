testCases = int(input())
occuranceOf4_list = []
for case in range(testCases):
    num = int(input())
    occuranceOf4 = 0
    while num > 0:
        digit = num % 10
        if digit == 4:
            occuranceOf4 = occuranceOf4 + 1
        num = num // 10
    occuranceOf4_list.append(occuranceOf4)

print(*occuranceOf4_list, sep="\n")