for _ in range(int(input())):
    app, org, coin = map(int, input().split())
    diff = abs(app - org)
    if diff <= coin:
        print("0")
    else:
        print(diff - coin)
