file = open("Problem 18 - Maximum path sum I.txt", 'r',)

triangle = []

nbLignes = 0

for i in file:
    triangle.append( list(map(int, i.split())) )
    nbLignes += 1
    
file.close()

note = [ [ [] for i in range(nbLignes) ] for a in range(nbLignes) ]

def dyna(ligne, emplacement):
    global nbLignes

    if ligne >= nbLignes:
        return -1

    if emplacement >= len(triangle[ligne]):
        return -1

    
    if note[ligne][emplacement]:
        return note[ligne][emplacement]

    score = triangle[ligne][emplacement]

    ajout = max(0, max(dyna(ligne+1,emplacement), dyna(ligne+1, emplacement+1)))

    score += ajout

    note[ligne][emplacement] = score

    return score

dyna(0,0)
