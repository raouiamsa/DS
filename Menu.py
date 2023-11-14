print("A- Hachage de mot \n")
print("\t a- Hacher le mot par sha256. \n") 
print("\t b- Attaquer par dictionnaire le mot inséré.\n") 
print("\t c- Revenir au menu principal\n")
print("B- Décalage par CESAR.\n")
print("\t a- Donnez un mot à chiffrer.\n")  
print("\t \t 1- Cesar avec code ASCII.\n")
print("\t \t 2- Cesar dans les 26 lettres.\n")
print("\t b- Chiffrer le message\n")
print("\t c- Déchiffrer le message\n")
print("\t d- Revenir au menu principal.\n")  
print("C- Data science.\n")
print("\ta- Affichez le Dataset sous forme de dictionnaire.\n")  
print("\tb- Afficher des courbes de votre choix.\n")
print("\tc- Revenir au menu principal.\n")
Choix=input("Donnez le lettre correspond à votre choix :A,B ou C ")
match Choix:
    case 'A':
        print("Vous etes dans la partie de Hachage du mot et attaque par dictionnaire! ")
        from Hachage import *
    case 'B':
        print("Vous etes dans la partie de Décalge César : ")
        from César import *
    case 'C':
        print("Vous etes dans la partie Data Science")
        from Datascience import *
    case _:
        print("vous devez entre un choix valide")
        import Menu
        
