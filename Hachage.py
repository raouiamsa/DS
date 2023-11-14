print("\t a- Hacher le mot par sha256. \n") 
print("\t b- Attaquer par dictionnaire le mot inséré.\n")
print("\t c- Revenir au menu principal\n")
Choix = input("Donner l'opération que vous souhaitez faire: ")
if Choix=='c':#il faut vérifier tout d'abord si l'utilisateur a choisit de revenir au menu principal donc il sert à rien de produire le mot à utiliser 
    from Menu import *
elif Choix=='a' or Choix =='b':
    word = input("Donner le mot à utiliser : ")
    import Fonctions_Hashage
    match Choix:
        case 'a':
            Quitter=False
            while Quitter==False:
                Resultat = Fonctions_Hashage.hashed(word)
                print(Resultat)
                choix = input("Voulez-vous entrer un autre mot ? Si oui, tapez O/o! ")
                if choix.lower() != 'o':
                    Quitter==True
                    import Hachage
                    break
                else:
                    word = input("Entrez un autre mot: ")
                continue
        case 'b':
            Quitter=False
            while Quitter ==False:
                print(Fonctions_Hashage.attack_Dict(word))
                choix = input("Voulez-vous entrer un autre mot ? Si oui, tapez O/o! ")
                if choix.lower() != 'o':
                    Quitter==True
                    from Hachage import *
                    break
                else:
                    word = input("Entrez un autre mot: ")
else: 
    print("vous devez choisir a,b ou c! ")
    import Hachage
