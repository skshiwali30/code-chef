totalSoldier = int(input())
soldier_list = list(map(int, input().split()))
evenCount, oddCount = 0, 0
for soldier in soldier_list:
    if soldier % 2 == 0:
        evenCount = evenCount + 1
    else:
        oddCount = oddCount + 1

if evenCount > oddCount:
    print("READY FOR BATTLE")
else:
    print("NOT READY")