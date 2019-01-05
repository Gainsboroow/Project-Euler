nbJours = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

jour = 1
mois = 1
annee = 1900

joursPasses = 0
dico = {0 : "Lundi", 1 : "mardi", 2 : "mercredi" , 3: "jeudi", 4 :"vendredi", 5 :"samedi", 6: "dimanche"}

total = [0]*7

while (jour, mois, annee) != (31, 12, 2000):
    #print(jour, mois, annee, total, dico[joursPasses] )
    
    if jour == 1 and annee != 1900:
        total[joursPasses] += 1
        #print(jour, mois, annee, total, dico[joursPasses] )
        
    jour += 1
    joursPasses = (joursPasses + 1)% 7
    
    if ( not(annee%4) and annee%100 ) or not(annee%400):
        nbJours[2] = 29
    else:
        nbJours[2] = 28
        
    if jour > nbJours[mois] :
        jour = 1
        mois += 1

    if mois > 12:
        mois = 1
        annee += 1

print(total)
