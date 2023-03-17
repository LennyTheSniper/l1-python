#%matplotlib inline

from time import time
from matplotlib.pyplot import plot, show, legend, xlabel, ylabel

def mesure_insertion(n, nb_iter=50):
    """Mesure le temps d'insertion d'un élément suivant la taille du tableau.
    
    Retourne un tableau de taille n où la ième case indique le temps moyen en 
    millisecondes pour ajouter une case à la fin d'un tableau de taille i."""
    tps = []
    i = 0
    while i < n:
        tps.append(0.)
        i += 1

    j = 0
    while j < nb_iter:
        t = []
        i = 0
        while i < n:
            tic = time()
            t.append(1)
            tps[i] += time() - tic
            i += 1
        j += 1

    i = 0
    while i < n:
        tps[i] *= 100 / nb_iter
        i += 1
    return tps

n = 100000
tps = mesure_insertion(n)
plot(list(range(n)), tps, "b", label="Insertion")

xlabel("Taille du tableau sur laquelle se fait l'insertion")
ylabel("Tps d'exécution d'une insertion en millisecondes")
legend()
show()