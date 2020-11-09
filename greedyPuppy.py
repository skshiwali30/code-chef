puppy_list = []
for _ in range(int(input())):
    coin, people = map(int, input().split())
    puppy = coin % people
    puppy_list.append(puppy)
print(*puppy_list, sep="\n")