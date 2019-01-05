from copy import deepcopy

from math import sqrt 

import sys
sys.setrecursionlimit(10**6)

sys.stdin = open("Problem 96 - Su Doku.txt", "r")

tailleCote = 9
taillePetitCarre = int(sqrt(tailleCote))

def verif(grid):
    for lig in range(tailleCote):
        used = [False] * (tailleCote+1)
        used[0] = True 
        for col in range(tailleCote):
            nombre = grid[lig][col]
            if used[nombre] : return False 
            used[nombre] = True 
    
    for col in range(tailleCote):
        used = [False] * (tailleCote+1)
        used[0] = True 
        for lig in range(tailleCote):
            nombre = grid[lig][col]
            if used[nombre] : return False 
            used[nombre] = True 

    for debLig in range(0, tailleCote, taillePetitCarre):
        for debCol in range(0, tailleCote, taillePetitCarre):
            used = [False] * (tailleCote+1)
            used[0] = True 
            for ligPetitCarre in range(debLig, debLig + taillePetitCarre):
                for colPetitCarre in range(debCol, debCol + taillePetitCarre):
                    nombre = grid[ligPetitCarre][colPetitCarre]
                    if used[nombre] : return False 
                    used[nombre] = True          
    
    return True
            
def remplir(grid):
    global total
    total += int( str(grid[0][0]) + str(grid[0][1]) + str(grid[0][2]) )


def check(_grille, _possibilites):
    file = [ (_grille, _possibilites) ]

    while file:

        grille, possibilites = file.pop(-1)
        update = True 

        while update:
            update = False 
            for lig in range(tailleCote):
                for col in range(tailleCote):
                    if len(possibilites[lig][col]) == 1:
                        grille[lig][col] = possibilites[lig][col][0]
                        nombre = grille[lig][col]
                        
                        for curCol in range(tailleCote):
                            if nombre in possibilites[lig][curCol]: 
                                possibilites[lig][curCol].remove(nombre)

                        for curLig in range(tailleCote):
                            if nombre in possibilites[curLig][col]:
                                possibilites[curLig][col].remove(nombre)

                        ligCarre = lig - (lig % taillePetitCarre)
                        colCarre = col - (col % taillePetitCarre)

                        for curLig in range(ligCarre, ligCarre + taillePetitCarre):
                            for curCol in range(colCarre, colCarre + taillePetitCarre):
                                if nombre in possibilites[curLig][curCol]:
                                    possibilites[curLig][curCol].remove(nombre)

                        update = True 

        quitter = False 
        
        for lig in range(tailleCote):
            for col in range(tailleCote):
                if quitter : break 

                if len(possibilites[lig][col]) > 1:
                    quitter = True 

                    for nombre in possibilites[lig][col]:
                        possibilites[lig][col] = [nombre]
                        file.append( (deepcopy(grille), deepcopy(possibilites)) )

        if not(quitter) and verif(grille):
            remplir(grille)
            return


def main():
    grille = [ [int(i) for i in input()] for a in range(tailleCote)]
    possibilites = [ [ [i for i in range(1, tailleCote+1)] for a in range(tailleCote)] for b in range(tailleCote) ]

    for lig in range(tailleCote):
        for col in range(tailleCote):
            nombre = grille[lig][col]
            if nombre:
                possibilites[lig][col] = [nombre]

    check(grille, possibilites)

total = 0

for i in range(50):
    input()
    main()
    if not i % 10:
        print(i)

print(total)
