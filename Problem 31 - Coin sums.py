pieces = [1,2,5,10,20,50,100,200]

possibilites = set()

def generer(total, facon, indice):
    if total > 200:
        return

    if total == 200:
        facon = "".join( map(str, sorted(facon)) )
        possibilites.add(facon)
        return

    for i in range(indice, len(pieces)):
        generer(pieces[i]+total, facon+[pieces[i]], i)

generer(0, [], 0)

print(len(possibilites))
