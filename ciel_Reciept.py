cases = int(input())
for case in range(cases):
    price = int(input())
    count = 0
    for i in range(11, -1, -1):
         menuPrice = 2 ** i
         count = count + (price // menuPrice)
         price = price % menuPrice
    print(count)