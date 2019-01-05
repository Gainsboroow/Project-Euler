"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

Reponse :
1389019170 1929374254627488900
"""

forme = "1_2_3_4_5_6_7_8_9_0"
#forme = "_6_7_8_96"

print(len(forme)//2)

for i in range(10**9, int(10**(len(forme)//2+1)), 10):
    if not i % 10**8: print(i)

    nombre = str(i**2)
    if len(nombre) != len(forme): continue

    valide = True
    
    for a, b in zip(forme, nombre):
        if a != "_" and a != b:
            valide = False

    if valide:
        print(i, nombre)
