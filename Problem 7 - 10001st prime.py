a = 0
with open("\Project_Euler\Programmes\premier.txt","r") as premier:
    for ligne in premier:
        if a == 100001:
            print(ligne)
        a += 1
