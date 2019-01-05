"""
For a positive integer n, let σ2(n) be the sum of the squares of its divisors.
For example,
σ2(10) = 1 + 4 + 25 + 100 = 130.

Find the sum of all n, 0 < n < 64,000,000 such that σ2(n) is a perfect square.

"""

from math import *

prime = [True]*64000000
prime[0] = prime[1] = False

for i in range(4, 64000000, 2):
    prime[i] = False
    
for i in range(3, 64000000):
    if prime[i]:
        for p in range(i*i, 64000000, 2*i):
            prime[p] = False

premier = []
for indice, primalite in enumerate(prime):
    if primalite:
        premier.append(indice)

print("Fin génération premiers")

def diviseur(n):
    if prime[n]: return n
    sommeDiv = 1
    for i in premier:
        if i > n: break
        multiplicite = 0
        while not n % i:
            multiplicite += 1
            n //= i
        if multiplicite:
            sommeDiv *= ( (i**(2*(multiplicite+1)) - 1) / (i*i-1) )
    return sommeDiv

total = 0

for i in range(1, 64000000):
    if not i % 10**5 : print(i)

    somme = diviseur(i)
    if sqrt(somme) == int(sqrt(somme)):
        total += somme

print(total)
