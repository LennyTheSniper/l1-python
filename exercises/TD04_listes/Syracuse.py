ListeSyracuse = [1]
def syracuse(n):
    ListeSyracuse = []
    ListeSyracuse.append(n)
    while n != 1:
        if n % 2 == 0:
            n //= 2
            ListeSyracuse.append(n)
        elif n % 2 == 1:
            n *= 3
            n += 1
            ListeSyracuse.append(n)
    return ListeSyracuse

def testeConjecture(n_max):
    n = 1
    while ListeSyracuse[-1] == 1 and n <= n_max:
        print(ListeSyracuse[-1] == 1,"at",n)
        n += 1
    if n > n_max:
        return True
    else:
        return False
#print(testeConjecture(1000))

def tempsVol(n):
    return(len(syracuse(n)))-1
abc = 15
print(syracuse(abc))
print(tempsVol(abc))

def tempsVolListe(n_max):
    tempsVolListe = []
    for i in range (1,n_max+1):
        tempsVolListe.append(tempsVol(i))
    return (tempsVolListe)

print(tempsVolListe(10))
"""
def OrdreCroissantListe(Liste):
    PlaceholerList = []
    for i in range (len(Liste)):
        PlaceholerList.append("")
    for i in range (len(Liste)):
        j = 0
        while j < len(Liste):
            if Liste[i] < Liste[j]:
                PlaceholerList[j] = Liste[j]
                Liste[j] = Liste[i]
                Liste[i] = PlaceholerList[j]
            j += 1
    return Liste

def SyracuseListe(n_max):
    SyracuseListe = []
    for i in range (1,n_max+1):
        SyracuseListe.append(OrdreCroissantListe(syracuse(i))[len(syracuse(i))-1])
    return (SyracuseListe)

a = tempsVolListe(1000)
b = SyracuseListe(1000)

print("tempsVolListe",a)
print("SyracuseListe",b)

OrdoneeA=OrdreCroissantListe(a)
OrdoneeB=OrdreCroissantListe(b)

print("tempsVolListe",OrdoneeA)
print("SyracuseListe",OrdoneeB)

print("Le temps de vol le plus grand atteint est",OrdoneeA[len(OrdoneeA)-1])
print("L'altitude la plus grande atteint est",OrdoneeB[len(OrdoneeB)-1])

print("Le temps de vol de", 3, "est", tempsVol(3))

#print(testeConjecture(10000))
"""