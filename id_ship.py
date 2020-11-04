cases = int(input())
id_list = []
ship_dict = {'B': 'BattleShip', 'C': 'Cruiser', 'D': 'Destroyer', 'F': 'Frigate'}
for case in range(cases):
    letter = input().upper()
    if letter in ship_dict:
        id_list.append(ship_dict[letter])

print(*id_list, sep="\n")