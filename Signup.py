import colorama
from colorama import Fore
#print(Fore.RED + "Texte rouge " + Fore.GREEN + "Texte vert " + Fore.BLUE + "Texte bleu")
print(Fore.BLUE + "Phase d'enregistrement : \n ")
def introduire_email():
    global email
    import re
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    while True:
        email = input("Donnez votre email : ")
        with open("Enregistrement.txt", 'r') as file:
            for line in file:
                colon_index = line.find(':')
                stored_email = line[:colon_index].lower()
                if stored_email.lower() == email.lower():
                    return None
            if re.fullmatch(regex, email):
                return email
            else:
                print(Fore.RED+"Merci d'introduire un email valide, sous la forme 'aaaaa.bbbbb@ccccc.ddddd'")

def introduire_password():
    global pwd
    import maskpass
    import string
    import hashlib
    while True :
        pwd=maskpass.askpass()
        if len(pwd) ==8 :
            if any(t in string.digits for t in pwd) :
                if any(t in string.ascii_uppercase for t in pwd) :
                    if any(t in string.ascii_lowercase for t in pwd) :
                        if any(t in string.punctuation for t in pwd) :
                            pwd = hashlib.sha256(pwd.encode()).hexdigest()
                            return pwd
                        else :
                            print(Fore.RED + "Le mot de passe doit contenir au moins un caractere spécial! ")
                    else :
                        print(Fore.RED + "Le mot de passe doit contenir au moins un caractere miniscule! ")
                else :
                    print(Fore.RED + "Pwd doit contenir au moins un caractere majuscule! ")
            else :
                print(Fore.RED + "Pwd doit contenir au moins un chiffre! ")
        else :
            print(Fore.RED + "Le mot de passe doit etre de longueur 8 ")
