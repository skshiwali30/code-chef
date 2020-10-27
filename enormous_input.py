n, k = map(int, input().split())
count = 0
for i in range(n):
    number = int(input())
    if number % k == 0:
        count = count + 1
print(count)
