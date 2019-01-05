grid = []

with open("Problem 11 - Largest Product in a Grid.txt", "r") as file :
    for i in file :
        grid.append( list( map(int, i.split() ) ) )

depl = [ (0,1), (1,0), (1,1), (1,-1) ]

maxi = 0

def fonction(lig, col, dlig, dcol):

    try:
        total = 1
        for i in range(4):
            total *= grid[lig+i*dlig][col+i*dcol]

        return total
    except:
        return 0

for lig in range( len(grid) ):
    for col in range( len(grid[0]) ):
        for dlig, dcol in depl:
            maxi = max(maxi, fonction(lig, col, dlig, dcol) )

print(maxi)
