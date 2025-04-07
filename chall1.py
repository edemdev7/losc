def tri_bulle(liste):
    n= len(liste)
    for i in range(n):
        for j in range (0,n-i-1):
            if liste[j] > liste [j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste            
print(tri_bulle([3,5,7,8,14]))

