# EXERCICE 2
N = int(input("Quelle sera la valeur de 'N'?"))
listeNombresPremiers = []
for nombreATesterSiPremier in range (2,N+1):
    DetecteNonPremier = 0
    for i in range (2,nombreATesterSiPremier):
        if nombreATesterSiPremier % i == 0:
            DetecteNonPremier = 1
    if DetecteNonPremier == 0:
        listeNombresPremiers.append(nombreATesterSiPremier)
print(listeNombresPremiers)