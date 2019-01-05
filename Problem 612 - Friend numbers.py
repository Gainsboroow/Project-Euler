def friend(a,b):
    present = [0]*10

    for i in str(a):
        present[ int(i) ] = 1

    for i in str(b):
        if present[ int(i) ]:
            return 1

    return 0

total = 0

for a in range(1, 10**18):
        
    for b in range(a+1, 10**18):
        if friend(a,b):
            total += 1
            total %= 1000267129

print(total)
