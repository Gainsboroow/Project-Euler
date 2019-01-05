"""
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.

REPONSE :
142857
"""

def memeChiffre(a, b):
    used = [0 for i in range(10)]

    for i in str(a):
        used[int(i)] += 1

    for i in str(b):
        used[int(i)] -= 1

    for i in used:
        if i: return False
    return True

for i in range(10**8):
    valide = True
    tab = [i*facteur for facteur in range(1,7)]
    for indice in range(6):
        if not(memeChiffre(tab[indice], tab[(indice+1)%6])):
               valide = False
    if valide:
               print(i)
               break
