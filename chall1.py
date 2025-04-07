"""def tri_bulle(liste):
    n= len(liste)
    for i in range(n):
        for j in range (0,n-i-1):
            if liste[j] > liste [j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste            
print(tri_bulle([3,5,7,8,14]))"""

def tri_bulle():
# Saisie des nombres séparés par des espaces
    Ma_liste = input("Entrez une liste de nombres entiers en utilisant l'espace comme séparateur : ")
# Affichage de Ma_liste en entier
    liste = [int(x) for x in Ma_liste.split()]
# Rangement de la liste
    x = len(liste)
    for i in range(x):
        for j in range(0, x - i - 1):
# Arrangement en ordre
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
# Afficher la liste triée
    print("La liste ordonnée est :", liste)
# Appel de la fonction
tri_bulle()