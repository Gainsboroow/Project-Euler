grid = []

with open("Problem 82 - Path sum three ways.txt", "r") as file:
    for i in file:
        grid.append( list(map(int, i.split(",") ) ) )
            
height, width = 80, 80

"""
height, width = 5,5
grid = [ [131,673,234,103,18],
         [201,96,342,965,150],
         [630,803,746,422,111],
         [537,699,497,121,956],
         [805,732,524,37,331]]
"""

INFINI = float("inf")
score = [ [ [INFINI for i in range(3)] for a in range(width) ] for b in range(height) ] # [GAUCHE, HAUT, BAS]
minimum = INFINI


for i in range(height):
    for a in range(3):
        score[i][0][a] = grid[i][0]
        

for col in range(1, width):
    score[0][col][0] = grid[0][col] + min(score[0][col-1])
    
    for lig in range(1, height):
        valCase = grid[lig][col]
        score[lig][col][0] = valCase + min(score[lig][col-1])
        score[lig][col][1] = valCase + min(score[lig-1][col][0], score[lig-1][col][1])

    for lig in range(height-1):
        valCase = grid[lig][col]
        score[lig][col][2] = valCase + min(score[lig+1][col][0], score[lig+1][col][2])

        
for i in range(height):
    minimum = min(minimum, min(score[i][-1]) )

print(minimum)
