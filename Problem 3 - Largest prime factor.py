def decompo(x):
    a = 2
    diviseur = 1
    while x != 1:
        if x%a == 0: #Si x est divisible par a
            x//= a #On divise
            diviseur += 1 #Il y a un diviseur de x en plus
            print(a)
        else:
            a+= a%2+1
            """
            Si a est pair (seulement au 1er tour de boucle, on ajoute 1)
            ensuite on ajoute 2
            """
                
    if diviseur == 2:
    #Si x a 2 diviseurs (1 [cas pas teste car toujours vrai] + lui-meme)
        print("Premier")

    else:
        print("Pas premier")
        

decompo(600851475143) #Réponse est le plus grand diviseur trouvé
