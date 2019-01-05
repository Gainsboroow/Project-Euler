"""
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right
to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

REPONSE :
748317
"""

from math import *

def isPrime(n):
    if n < 2 : return False
    
    for i in range(2, int(sqrt(n))+1):
        if not n % i : return False
    return True

compteur = 0
nb = 11
total = 0

while compteur != 11:
    if isPrime(nb):
        valide = True
        
        for i in range(1, len(str(nb))):
            gauche = str(nb)[:i]
            droite = str(nb)[i:]
            if not(isPrime(int(gauche)) and isPrime(int(droite))):
                   valide = False
                   break
        if valide:
                   compteur += 1
                   total += nb
                   print(nb)

    
    nb += 2

print(total)
