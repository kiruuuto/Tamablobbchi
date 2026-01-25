import random
import tkinter as tk


'''
comment marche un aglo fourmi
Un algorithme de type "fourmi" (Ant Colony Optimization, ACO) est une méthode d'optimisation inspirée du comportement des fourmis dans la nature. Voici comment cela fonctionne généralement :
1. **Inspiration biologique** : Les fourmis dans la nature trouvent des chemins optimaux entre leur nid et les sources de nourriture en déposant des phéromones sur le sol. Plus un chemin est utilisé, plus il y a de phéromones, ce qui attire davantage de fourmis.
2. **Représentation du problème** : Le problème à résoudre est représenté sous forme de graphe, où les nœuds représentent les états ou les solutions possibles, et les arêtes représentent les transitions entre ces états avec des coûts associés.
3. **Initialisation** : Un certain nombre de fourmis artificielles sont placées sur le graphe. Chaque fourmi construit une solution en se déplaçant de nœud en nœud selon certaines règles probabilistes basées sur les phéromones et les coûts des arêtes.
4. **Construction de solutions** : Chaque fourmi construit une solution complète en choisissant les
    prochaines étapes en fonction de la quantité de phéromones présentes sur les arêtes et des coûts associés. Les fourmis ont tendance à choisir des chemins avec plus de phéromones et des coûts plus faibles.
5. **Mise à jour des phéromones** : Une fois que toutes les fourmis ont construit leurs solutions, les phéromones sur les arêtes sont mises à jour. Les chemins utilisés par les fourmis qui ont trouvé de bonnes solutions reçoivent une augmentation de phéromones, tandis que les phéromones sur les autres chemins s'évaporent avec le temps.
6. **Itération** : Le processus de construction de solutions et de mise à jour des
phéromones est répété pendant un certain nombre d'itérations ou jusqu'à ce qu'une condition d'arrêt soit atteinte (par exemple, un nombre maximum d'itérations ou une solution satisfaisante).
7. **Résultat final** : Après plusieurs itérations, les chemins avec les plus fortes concentrations de phéromones représentent les solutions optimales ou quasi-optimales au problème initial.
Voici un exemple simple d'implémentation d'un algorithme de type fourmi en Python pour résoudre le problème du voyageur de commerce (TSP) :
'''
'''
je suis en train d'etudier le code de test.py c'est euh un modele de simulation de blob 
qui a été creer et que jai trouvé sur github donc le code est open source bah nn pcq dcp t'as le droit de l'utiliser et l'etudier
et moi je vais l'etudier pour comprendre comment marche un aglo de type fourmi et apres je vais essayer de l'adapter a mon projet
'''


# Temps
temps = 200              # nombre d'itérations de la simulation

# Paramètres biologiques (modèle)
alpha = 0.1              # renforcement des veines
beta = 0.02              # évaporation (atrophie)
seuil = 0.05             # seuil de suppression d'une veine

# Environnement
taille_grille = 20       # si tu utilises une grille 2D
rows = 10
cols = 10
cell_size = 50



width = 500
height = 500
hauteur = 10
largeur = 10
#blob = [[0.0 for _ in range(largeur)] for _ in range(hauteur)]

blob = [[0 for _ in range(largeur)] for _ in range(hauteur)]  # grid of blob IDs


pheromone = [[0.0 for _ in range(largeur)] for _ in range(hauteur)]

root = tk.Tk()
root.title("jpp")
canvas = tk.Canvas(root, width=cols*cell_size, height=rows*cell_size, bg="white")
canvas.pack()

for y in range(rows):
    for x in range(cols):
        canvas.create_rectangle(x*cell_size, y*cell_size, (x+1)*cell_size, (y+1)*cell_size, fill="lightgrey", outline="black")

obstacles = []

if (x,y) in obstacles:
    color = "black"

#blob[y][x] = canvas.create_rectangle(50, 50, 100, 100, outline="black", fill='red')

blob[0][0] = canvas.create_rectangle(0, 0, cell_size, cell_size, fill='red', outline='black')


def border_check(x, y):
    x1, x2, y1, y2 = canvas.coords(blob[y][x])
    if x1 + x < 0 or y1 + y < 0:
        return False
    if x2 + x > width or y2 + y > height:
        return False
    return True

def move_blob():
    dx = random.randint(-cell_size, cell_size)
    dy = random.randint(-cell_size, cell_size)
    if border_check(0, 0, dx, dy):
        canvas.move(blob[0][0], dx, dy)
    root.after(1000, move_blob)

move_blob()


for y in range(hauteur):
    for x in range(largeur):
        pheromone[y][x] = 1.0
        obstacles = [(2,3), (4,1), (6,2)]
        for (ox, oy) in obstacles:
            pheromone[oy][ox] = 0.0

def evaporation():
    for y in range(hauteur):
        for x in range(largeur):
            pheromone[y][x] *= (1 - beta)
            if pheromone[y][x] < seuil:
                pheromone[y][x] = 0.0

def reinforce_path(path):
    for (x, y) in path:
        pheromone[y][x] += alpha

def afficher_grille():
    pass

root.mainloop()

