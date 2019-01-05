"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime
factors each. What is the first of these numbers?

134043
"""

from math import *

listPrime = []
with open('premier.txt', 'r') as f:
    for i in f:
        listPrime.append( int(i) )

nbFacteurs = 4

def decompo(x):
    facteurs = set()
    for i in listPrime:
        if i > x or len(facteurs) > nbFacteurs: break
        multiplicite = 0
        while not(x % i):
            multiplicite = True
            x //= i
        if multiplicite:
            facteurs.add(i)
    return facteurs



for i in range(10**5, 10**6):
    tab1 = decompo(i)
    if len(tab1) != nbFacteurs: continue
    tab2 = decompo(i+1)
    if len(tab2) != nbFacteurs : continue
    tab3 = decompo(i+2)
    if len(tab3) != nbFacteurs : continue
    tab4 = decompo(i+3)
    if len(tab4) != nbFacteurs : continue
    print(i)
    break
