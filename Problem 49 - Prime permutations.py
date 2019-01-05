"""


The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating
the three terms in thissequence?

REPONSE :
2969 6299 9629
"""

import sys
sys.stdin = open("premier.txt", 'r')

nombre = int(input())
while nombre < 1000:
    nombre = int(input())

tab = []

while nombre < 10000:
    tab.append(nombre)
    nombre = int(input())

def dicho(cible):
    inf = 0
    sup = len(tab) - 1

    while inf <= sup:
        moitie = (inf + sup) // 2
        if tab[moitie] == cible:
            return True
        elif tab[moitie] < cible:
            inf = moitie + 1
        else:
            sup = moitie - 1
            
    return False

def isPerm(a, b):
    used = [0 for i in range(10)]
    for i in str(a):
        used[ int(i) ] += 1
    for i in str(b):
        if not( used[int(i)] ): return False
        used[ int(i) ] -= 1
    return True
        
for i in tab:
    for raison in range(2, 10**4 // 3 + 1, 2):
        if isPerm(i,i+raison) and isPerm(i, i+2*raison) and \
        dicho(i + raison) and dicho(i + 2*raison):
            print(i, i + raison, i + 2*raison)


