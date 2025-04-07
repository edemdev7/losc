from collections import deque

def trouver_chemin(grille, depart, arrivee):
    lignes=len(grille)
    cols=len(grille[0])
    file=deque()
    file.append((depart,[depart])) #position,chemin_actu
    visites=set()
    visites.add(depart)

    #haut,bas,gauche,droite
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while file:
        (x,y),chemin=file.popleft()
        if (x,y) == arrivee:
            return chemin
        
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if(0<=nx<lignes and 0 <=ny<cols and grille[nx][ny]==0 and (nx,ny) not in visites):
                visites.add((nx,ny))
                file.append(((nx,ny),chemin+[(nx,ny)]))
    return None #aucun chemin trouvé

grille = [
  [0, 1, 0, 0],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [1, 1, 0, 0]
]
depart = (0, 0) 
arrivee = (3, 3)

chemin = trouver_chemin(grille,depart,arrivee)
print(chemin)