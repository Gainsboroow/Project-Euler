"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

possibilites = [0]*1001

for a in range(1,334):
    for b in range(a+1, 1000-a):
        c = int( (a**2 + b**2)**(1/2) )
        if c*c == a**2 + b**2:
            perimetre = a+b+c
            if perimetre < 1000:
                #print(perimetre, a,b,c)
                possibilites[perimetre] += 1

indice = 0
for i in range(1001):
    if possibilites[i] > possibilites[indice]:
        indice = i
        
print(indice)