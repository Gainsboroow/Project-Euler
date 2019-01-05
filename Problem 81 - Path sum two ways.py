grid = []

with open("Problem 81 - Path sum two ways.txt", "r") as file:
    for i in file:
        grid.append( list(map(int, i.split(",") ) ) )
        

score = [ [0 for i in range(80)] for a in range(80) ]

def parcours(lig, col):
    if not( 0 <= lig < 80 and 0 <= col < 80):
        return 0
    
    if score[lig][col]:
        return score[lig][col]

    points = grid[lig][col]

    droite = parcours(lig, col+1)
    bas = parcours(lig+1, col) 

    ajout = 0
    if droite and bas:
        ajout = min(droite, bas)
    else:
        ajout = max(droite, bas)
        
    points += ajout

    score[lig][col] = points

    return points

print(parcours(0,0))
