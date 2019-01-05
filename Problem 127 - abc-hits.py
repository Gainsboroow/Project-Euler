"""
https://projecteuler.net/problem=127


The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

    GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
    a < b
    a + b = c
    rad(abc) < c

For example, (5, 27, 32) is an abc-hit, because:

    GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
    5 < 27
    5 + 27 = 32
    rad(4320) = 30 < 32

It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000.
"""

from math import *

def rad(n):
    nb = 2
    produit = 1
    while n != 1:
        changement = False
        while not n % nb:
            n //= nb 
            changement = True
        
        if changement:
            produit *= nb
        nb += 1
    
    return produit

total = 0
limite = 120000
for a in range(1, limite//2):
    for b in range(a+1, limite-a):
        if gcd(a,b) != 1:
            continue 

        c = a+b

        if gcd(a,c) != 1 or gcd(b,c) != 1 or rad(a*b*c) >= c: 
            continue 
        
        total += c

print(total)