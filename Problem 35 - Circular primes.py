"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

REPONSE :
55
"""

from math import * 
from itertools import *

premier = [True]*(10**6)
circulaire = [None]*(10**6)

def crible():
    for i in range(2, int(sqrt(10**6)) + 1):
        if premier[i]:
            for a in range(i**2, 10**6, i):
                premier[a] = False 

def rotation(n):
    tab = []
    n = str(n)
    for i in range( len(n) ):
        tab.append( n[i:] + n[:i] )

    return tab


print("Debut Crible")
crible()
print("Fin Crible")

total = 0

for i in range(2, 10**6):
    if circulaire[i] == 0:
        continue 
    if circulaire[i]:
        total += 1 
        continue

    if premier[i]:
        perm = rotation(i)

        
        cyclique = 1
        for curPerm in perm:
            nombre = int(curPerm)
            if not(premier[nombre]):
                cyclique = 0 
        
        for curPerm in perm:
            nombre = int(curPerm)
            circulaire[nombre] = cyclique
        
        total += cyclique
        

print(total)
