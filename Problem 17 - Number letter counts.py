
alphabet = [
{1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"},
{0 : "ten", 1 : "eleven", 2 : "twelve", 3 : "thirteen", 4 : "fourteen", 5 : "fifteen", 6 : "sixteen", 7 : "seventeen", 8 : "eighteen", 9 : "nineteen"},
{2 : "twenty", 3 : "thirty", 4 : "fourty", 5 : "fifty", 6 : "sixty", 7 : "seventy", 8 : "eighty", 9 : "ninety"}
]

def ecrire(nombre):
        chaine = ""
        if len(str(nombre)) == 1:
                chaine += alphabet[0][nombre]

        else:
                motAnd = False 

                if int(str(nombre)[-2]) == 1:
                        chaine += alphabet[1][int(str(nombre)[-1])]
                        motAnd = True

                elif int(str(nombre)[-2]):
                        chaine += alphabet[2][int(str(nombre)[-2])]
                        if int(str(nombre)[-1]):
                                chaine += alphabet[0][int(str(nombre)[-1])]
                        motAnd = True
                elif int(str(nombre)[-1]):
                        chaine += alphabet[0][int(str(nombre)[-1])]
                        motAnd = True

        

                if len(str(nombre)) > 2:
                        if motAnd: 
                                chaine = "and" + chaine

                        chaine = alphabet[0][int(str(nombre)[-3])] + "hundred" + chaine
        
        print(nombre, chaine, len(chaine))
        return len(chaine)
        


total = 0
for i in range(1, 1000):
        total += ecrire(i)

print(total + len("onethousand"))