print("\t \t 1- Cesar avec code ASCII.\n")
print("\t \t 2- Cesar dans les 26 lettres.\n")
print("\t \t 3-Revenir au menu principal")

while True:
    try:
        Choix = int(input("Donner l'opération que vous souhaitez faire: "))
        
        if Choix == 1 or Choix == 2:
            print("Vous avez choisi le code ASCII pour le décalage!" if Choix == 1 else "Vous avez choisi le code ASCII pour le décalage!")
            
            Message = input("Donner le message à chiffrer: ")
            Clé = int(input("Donnez le clé de décalage: "))
            
            print("\t a- Chiffrer le message\n")
            print("\t b- Déchiffrer le message\n")
            print("\t c- Revenir au menu principal.\n")
            
            Choice = input("Donner l'opération souhaitée: ")
            
            if Choice == 'a' or Choice == 'b':
                from Chiffrement import Chiff_César_Ascii, Déchiff_César_Ascii, Chiff_César_lettre, Déchiff_César_lettre
                Quitter = False
                
                while not Quitter:
                    if Choix == 1:
                        Resultat = Chiff_César_Ascii(Message, Clé) if Choice == 'a' else Déchiff_César_Ascii(Message, Clé)
                    else:
                        Resultat = Chiff_César_lettre(Message, Clé) if Choice == 'a' else Déchiff_César_lettre(Message, Clé)
                    
                    print(Resultat)
                    
                    choix = input("Voulez-vous entrer un autre mot ? Si oui, tapez O/o! ")
                    if choix.lower() == 'o':
                        Message = input("Entrez un autre mot: ")
                    else:
                        Quitter = True
            elif Choice == 'c':
                break  # Exit the loop to return to the main menu
            else:
                print("Vous devez choisir a, b ou c!")
        elif Choix==3:
            import Menu
        else:
            print("vous devez choisi 1,2 ou 3 !")
    except ValueError:
        print("donnez un choix valid")