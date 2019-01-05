a, b = 1, 1

for i in range(3, 10**6):
    a, b = a+b, a

    if len(str(a)) == 1000:
        print(i)
        break
