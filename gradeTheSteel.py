grade = []
for _ in range(int(input())):
    hardness, cc, ts = map(float, input().split())
    hardness = int(hardness)
    ts = int(ts)
    if (hardness > 50) and (cc < 0.7) and (ts > 5600):
        grade.append("10")
    elif (hardness > 50) and (cc < 0.7):
        grade.append("9")
    elif (cc < 0.7) and (ts > 5600):
        grade.append("8")
    elif (hardness > 50) and (ts > 5600):
        grade.append("7")
    elif (hardness > 50) or (cc < 0.7) or (ts > 5600):
        grade.append("6")
    else:
        grade.append("5")

print(*grade, sep="\n")
