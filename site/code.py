choix = int(input("choisis un nombre\n"))#on choisis le nombre a convertir en hieroglyphe



def entier_vers_egypt(entier):#on défini une fonction pour effectuer la conversion
    chiffres = [(1000000, "☺"),#creation d'une liste pour stocker et utiliser les valeurs
            (100000, "♪"),
            (10000, "⌠"),
            (1000, "֍"),
            (100, "φ"),
            (10, "∩"),
            (1, "I")]



    list_egypt = []#nouvelle liste pour ajouter les signes a la fin de la conversion
    
    

    for number, symbol in chiffres:#boucle pour faire la conversion 
    
        while entier >= number:
            entier -= number #tant que l'entier mis par l'utilisateur est supéerieur ou egal au nombre de la liste, on soustrait le nombre a l'entier choisi pour afficher dans l'ordre decroissant les signes 
            
            
            
            list_egypt.append(symbol)#ajoute les symbole dans la liste


    return " ".join(list_egypt)#un espace entre chaque symbole


print(entier_vers_egypt(choix))#affiche le resultat par rapport au nombre entré
