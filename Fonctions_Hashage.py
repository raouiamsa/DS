import hashlib 
def hashed(Mot):
    Resultat=hashlib.sha256(Mot.encode()).hexdigest()
    return Resultat
def attack_Dict(Mot):
    with open("Dict.txt", 'r',encoding="utf-8") as file:
        for line in file:
            line=line.strip()
            if hashlib.sha256(line.encode()).hexdigest()==hashed(Mot):
                return True
    return False
    

