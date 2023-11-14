def Chiff_César_lettre(Message,Key):
    alphabet_Maj="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_Min="abcdefghijklmnopqrstuvwxyz"
    Message_chiffré=""
    for i in Message:
        if i in alphabet_Maj:
            Message_chiffré+=alphabet_Maj[(alphabet_Maj.index(i)+Key)%26]
        elif i in alphabet_Min:
            Message_chiffré+=alphabet_Min[(alphabet_Min.index(i)+Key)%26]
        else:
            Message_chiffré+=i
    return Message_chiffré
def Déchiff_César_lettre(Message,Key):
    alphabet_Maj="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_Min="abcdefghijklmnopqrstuvwxyz"
    Message_chiffré=""
    for i in Message:
        if i in alphabet_Maj:
            Message_chiffré+=alphabet_Maj[(alphabet_Maj.index(i)-Key)%26]
        elif i in alphabet_Min:
            Message_chiffré+=alphabet_Min[(alphabet_Min.index(i)-Key)%26]
        else:
            Message_chiffré+=i
    return Message_chiffré
def Chiff_César_Ascii(Message,Key):
    message_chiffré = ""
    for lettre in Message:
        # On va vérifier si la lettre est une lettre majuscule
        if lettre.isupper():
            # Décaler la lettre dans l'alphabet
            lettre_chiffree = chr((ord(lettre) + Key - 65) % 26 + 65)
        # On va vérifier si la lettre est une lettre minuscule
        elif lettre.islower():
            # Décaler la lettre dans l'alphabet
            lettre_chiffree = chr((ord(lettre) + Key - 97) % 26 + 97)
        else:
            # Si ce n'est pas une lettre, la laisser inchangée
            lettre_chiffree = lettre
        # Ajouter la lettre chiffrée au message chiffré
        message_chiffré += lettre_chiffree
    return message_chiffré
def Déchiff_César_Ascii(Message,Key):
    message_chiffré = ""
    for lettre in Message:
        # On va vérifier si la lettre est une lettre majuscule
        if lettre.isupper():
            # Décaler la lettre dans l'alphabet
            lettre_chiffree = chr((ord(lettre) - Key - 65) % 26 + 65)
        # On va vérifier si la lettre est une lettre minuscule
        elif lettre.islower():
            # Décaler la lettre dans l'alphabet
            lettre_chiffree = chr((ord(lettre) - Key - 97) % 26 + 97)
        else:
            # Si ce n'est pas une lettre, la laisser inchangée
            lettre_chiffree = lettre
        # Ajouter la lettre chiffrée au message chiffré
        message_chiffré += lettre_chiffree
    return message_chiffré
