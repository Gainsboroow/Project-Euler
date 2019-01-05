"""
A composite is a number containing at least two prime factors. For example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < 108, have precisely two, not necessarily distinct, prime factors?
"""

from math import *

"""
def isSemiPrime(n):
    nb = 2
    nbFacteurs = 0
    while n != 1 and nbFacteurs != 2:
        while not n % nb:
            n //= nb 
            nbFacteurs += 1
        nb += 1
    if n == 1 and nbFacteurs == 2:
        return True 
    return False

compteur = 0
for i in range(2,10**8):
    if not i % 10**6: print(i)
    if isSemiPrime(i):
        compteur += 1
"""

nbPremiers = int(10**8 / log(10**8))

print(factorial(nbPremiers+1)/(factorial(nbPremiers-2)*2) )
