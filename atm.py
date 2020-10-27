amount, balance = input().split()
amount = int(amount)
balance = float(balance)
bankCharges = 0.50

if (amount % 5 == 0) and ((amount + bankCharges) < balance):
    balance = balance - (amount + bankCharges)

print("{0:.2f}".format(balance))