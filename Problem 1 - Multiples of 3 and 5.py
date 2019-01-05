a = 3
b = 5
z = 0
multiple = []
i = 0

while i <= 999:
    i = a*z
    z+=1
    multiple.append(i)
    
i = 0
z = 0
while i <= 999:
    i = b*z
    z+=1
    multiple.append(i)
#print(multiple)
    
multiple.remove(1000)
multiple.remove(1002)

mult_sans_doublon = set(multiple)
#print(mult_sans_doublon)

sommefinale = sum(mult_sans_doublon)
#print(sum(multiple))
#print(somme_multiple)

print(sommefinale)
