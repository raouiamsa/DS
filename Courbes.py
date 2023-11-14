from colorama import Fore
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import train_test_split
from colorama import Fore
import csv
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("..\DS\Iris.csv", header=0, names=['sepal_l', 'sepal_w', 'petal_l', 'petal_w', 'class'])
print("A-Compréhension du jeu de données: \n")
print("B-Les Courbes :\n")
print("C-Apprentissage automatique:\n")
Choix=input("Donnez votre choix: ")
match Choix:
    case 'A':
        print(Fore.CYAN+"5 premieres lignes du jeu de données : \n"+Fore.WHITE)
        print(data.head())
        print(Fore.CYAN+"\n Shape:\n"+Fore.WHITE)
        print(data.shape)
        print(Fore.CYAN+"\n Infos générales:"+Fore.WHITE)
        print(data.info())
        print(Fore.CYAN+"\n Infos détaillés: \n"+Fore.WHITE)
        print(data.describe())
        print(Fore.CYAN+"\n Nombre des cases vides: \n"+Fore.WHITE)
        print(data.isnull().sum())
        print(Fore.CYAN+"\n Nombres des lignes dupliquées \n"+Fore.WHITE)
        print(data.duplicated().sum())
        Choix =input ("voulez vous reafficher le menu pour choisir un autre opération ? si oui taper O/o! ")
        if Choix.lower()=='o':
            from Courbes import *
    case 'B':
        print(Fore.MAGENTA+"a- Piechart\nb- Histogram\nc- Tout les histogrammes \nd- Points "+Fore.WHITE)
        Choix1=input("donnez votre choix du courbe :")
        match Choix1:
            case 'a':
                class_counts = data['class'].value_counts()
                plt.figure(figsize=(8, 8))
                plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', startangle=140)
                plt.title('Distribution of Iris Classes')
                plt.show()
            case 'b':
                column_for_histogram = 'sepal_l'
                plt.figure(figsize=(8, 6))
                plt.hist(data[column_for_histogram], bins=20, color='skyblue', edgecolor='black')
                plt.xlabel(column_for_histogram)
                plt.ylabel('Frequency')
                plt.title(f'Histogram of {column_for_histogram}')
                plt.show()

            case 'c':
                grid = sns.FacetGrid(data, col='class', height=4, aspect=1.2)
                grid.map(plt.hist, 'sepal_l', bins=15, color='skyblue', edgecolor='black')
                grid.set_axis_labels('Sepal Length', 'Frequency')
                grid.set_titles('Histogram of Sepal Length for {col_name}')
                plt.tight_layout()
                plt.show()

            case 'd':
                
                plt.figure(figsize=(8, 6))
                sns.scatterplot(data=data, x='sepal_l', y='sepal_w', hue='class', palette='viridis', s=80, alpha=0.8)
                plt.title('Scatter Plot of Sepal Length vs Sepal Width')
                plt.xlabel('Sepal Length')
                plt.ylabel('Sepal Width')
                plt.legend()
                plt.show()
            case _:
                print("donner un choix valid")
    case 'C':
        X = data.drop('class', axis=1)  # Features
        y = data['class']  # Target variable
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        #Pour l'arbre de décision
        dt_classifier = DecisionTreeClassifier(random_state=42)
        dt_classifier.fit(X_train, y_train)
        dt_predictions = dt_classifier.predict(X_test)
        #pour Randrom Forest
        rf_classifier = RandomForestClassifier(random_state=42)
        rf_classifier.fit(X_train, y_train)
        rf_predictions = rf_classifier.predict(X_test)
        #Support Vector Machine (SVM)
        svm_classifier = SVC(random_state=42)
        svm_classifier.fit(X_train, y_train)
        svm_predictions = svm_classifier.predict(X_test)
        #evaluation
        print("Decision Tree Accuracy:", accuracy_score(y_test, dt_predictions))
        print("Random Forest Accuracy:", accuracy_score(y_test, rf_predictions))
        print("SVM Accuracy:", accuracy_score(y_test, svm_predictions))
        # Rapports
        print("\nDecision Tree Classification Report:\n", classification_report(y_test, dt_predictions))
        print("\nRandom Forest Classification Report:\n", classification_report(y_test, rf_predictions))
        print("\nSVM Classification Report:\n", classification_report(y_test, svm_predictions))
    case _:
        print(Fore.RED+"Donner un choix valid \n"+Fore.WHITE)
        from Courbes import *

