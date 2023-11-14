import colorama
from colorama import Fore
import hashlib
import hashlib
import pyautogui
def authentification():
    email = input("Entrez votre email : ")
    email_found=False
    with open("Enregistrement.txt", 'r') as file:
        for line in file:
            # Trouver l'indice de la première occurrence de ':'
            colon_index = line.find(':')
            stored_email = line[:colon_index]  # Extraire l'email
            stored_pwd = line[colon_index + 1:].strip()  # Extraire le mot de passe
            if email.lower() == stored_email.lower() :
                email_found = True  # Marquer que l'email a été trouvé
                pwd= pyautogui.password("tapez le mot de passe: ")
                password=hashlib.sha256(pwd.encode()).hexdigest()
                if password == stored_pwd:
                    return True  # Authentification réussie
                else:
                    print(Fore.RED+"Mot de passe incorrect"+Fore.WHITE)
                    return False  # Authentification échoué
    if not email_found:
        choice = input(Fore.RED+"Cet email n'est pas enregistré. Voulez-vous vous enregistrer ? Tapez O/o pour s'enregistrer: ")
        if (choice== 'o' or choice=='O'):
            import Signup
            email = Signup.introduire_email()
            pwd = Signup.introduire_password()
            with open("Enregistrement.txt", 'a') as file:
                file.write(f"{email}:{pwd}")
            print(Fore.GREEN+"Enregistrement réussi."+Fore.WHITE)
        else:
            choice1 = input(Fore.YELLOW+"Voulez-vous revenir au menu principal ou vous reconnecter ? Tapez O/o pour vous reconnecter: "+Fore.WHITE)
            if choice1.lower() == "o":
                return authentification()

    return False  # Authentification échouée
if authentification():
    import Menu
else :
    print(Fore.RED+"Accés non autorisé. Veuillez saisir les cordonnées correctes"+Fore.WHITE)
    from signin import *
