testCases = int(input())
sum1, sum2 = 0, 0
lead1, lead2 = [], []
for case in range(testCases):
    player1, player2 = map(int, input().split())
    sum1 += player1
    sum2 += player2
    if sum1 > sum2:
        lead1.append(sum1 - sum2)
    else:
        lead2.append(sum2 - sum1)

if sum(lead1) > sum(lead2):
    print("1", max(lead1))
else:
    print("2", max(lead2))
