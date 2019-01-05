"""
Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?

REPONSE :
669171001
"""

cote = 1001
tab = [ [0 for i in range(cote)] for a in range(cote)]

etape = 1
lig, col = cote//2, cote//2

delta = [ (0,1), (1,0), (0,-1), (-1,0) ]
indice = 0

i = 1
while i < cote**2:
    for a in range(etape):
        tab[lig][col] = i
        i+= 1
        lig += delta[indice][0]
        col += delta[indice][1]
    
    indice = (indice+1) % 4
    if not(indice % 2):
        etape += 1

somme = 0
for i in range(cote):
    somme += tab[i][i] + tab[i][-i-1]
    
print(somme-1) #Substracting the middle case (1), double counted 
    
