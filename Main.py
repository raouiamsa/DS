while True:
    try:
        print("1- Sign_Up")
        print("2- Sign_In")
        print("3- Quitter")
        Choix=int(input("Merci d'introduire le numéro d'opération souhaité ")) 
        match Choix:
            case 1:
                from Signup import introduire_email
                from Signup import introduire_password
                email=''
                pwd=''
                with open("Enregistrement.txt",'a') as file:
                            file.write("")
                while pwd =='':
                    while email=='':    
                        email = introduire_email()
                        break
                    if email is not None:
                        pwd=introduire_password() 
                        with open("Enregistrement.txt",'a') as file:
                            file.write(f"{email}:{pwd}\n")
                        Choice=input("vous avez enregistré avec succés.Voulez vous connecter? Si oui tapez O/o! ")
                        if Choice.lower()=='o':
                            import signin
                            signin.authentification() 
                            
                        else:
                            from Main import *
                    else:
                        Choix=input("Ce adresse est déja enregistré, voulez vous connecter? Si Oui tapez O/o! ")
                        if Choix.lower()=='o':
                            from signin import *
                        else:
                            from Main import *
                break
            case 2:
                from signin import *
            case 3: 
                print("Au revoir")
                break
            case _:
                print("choisir 1, 2 ou 3 ")
    except ValueError:
        print("Choisir un valid choix")
