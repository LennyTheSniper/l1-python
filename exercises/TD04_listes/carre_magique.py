carre_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]]
carre_pas_mag=[[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,7,13]]
def testCollonesEgales(carre):
    for i in range(len(carre)):
        somme = 0
        for j in range(len(carre)):
            print("carré[j][i] =",carre[j][i])
            somme += carre[j][i]
        if "somme_two" not in locals():
            somme_two = somme
        print(somme,somme_two)
        if somme == somme_two:
            pass
        else:
            del somme_two
            return(-1)
    del somme_two
    return(True)

print(testCollonesEgales(carre_mag))
print(testCollonesEgales(carre_pas_mag))