print("Dans cette partie nous allons travailler sur Iris Data ")
print("\t a- Affichez le Dataset sous forme de dictionnaire.\n")  
print("\t b- Afficher des courbes de votre choix.\n")
print("\t c- Revenir au menu principal.\n")
Choix=input("donnez votre chiox: ")
match Choix:
    case 'a':
        import csv
        csv_file_path = '../DS/Iris.csv'
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            dataset_as_dict = [row for row in csv_reader]
        print(dataset_as_dict)
        ch=input("voulez vous voir les courbes ? Si oui Tapez O/o: ")
        if ch.lower()=='o':
            import Courbes
    case 'b':
        import Courbes
    case 'c':
        from Menu import *
    case _:
        print("vous devez choisir a,b ou c")
        from Datascience import *