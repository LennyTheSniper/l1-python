# EXERCICE 1
listeNombres = [] ; valeurliste = 0
n = int(input("Quelle sera la valeur de 'n'?"))
for i in range (n):
    valeurliste += 2**i    # 2^0, puis 2^1, puis 2^2...
    listeNombres.append(valeurliste)
print(listeNombres)