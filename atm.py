amount, balance = map(float, input().split())
amount = int(amount)
bankCharges = 0.50

if (amount % 5 == 0) and ((amount + bankCharges) < balance):
    balance = balance - (amount + bankCharges)

print("{0:.2f}".format(balance))