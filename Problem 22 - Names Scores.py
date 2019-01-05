noms = []

with open("Problem 22 - Names Scores.txt", "r") as file:
    for i in file:
        noms = list( eval(i) )

noms.sort()

total = 0

for i in range( len(noms) ):
    pts = 0
    
    for a in noms[i]:
        pts += ord(a) - ord("A") + 1

    total += (pts * (i+1) )
    
print(total)
