sal_list =[]
for _ in range(int(input())):
    basic_sal = int(input())
    if basic_sal < 1500:
        HRA = basic_sal * 0.1
        DA = basic_sal * 0.9
    else:
        HRA = 500
        DA =  basic_sal * 0.98
    gross_sal = HRA + DA + basic_sal
    sal_list.append("{0:.2f}".format(gross_sal))
print(*sal_list, sep="\n")