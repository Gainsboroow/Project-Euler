maximum = 0

for a in range(100):
    print(a)
    for b in range(100):
            maximum = max(maximum, sum(int(i) for i in str(a**b) ))

print(maximum)	
