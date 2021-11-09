#Exercice 2:

x_A = int(input("Combient vaudras x_A?"))
x_B = int(input("Combient vaudras x_B?"))
y_A = int(input("Combient vaudras y_A?"))
y_B = int(input("Combient vaudras y_B?"))

if x_A == x_B and y_A == y_B:
    print("Les points sont les mêmes.")
elif x_A != x_B and y_A != y_B:
    m = (y_B - y_A) / (x_B - x_A)
    p = (y_B * x_A - y_A * x_B) / (x_A - x_B)
    print("Le coefficient directeur est ",m,". L'ordonnée à l'origine est ",p,sep='')
elif x_A == x_B:
    print("Les points ont la même valeur de x!")
elif y_A == y_B:
    print("Les points ont la même valeur de y!")

#Exercice 3:

n = int(input("Combien vaudra n?"))
Produit = 1
for i in range (n):
    NouvelleValeur = int(input("Combien vaudra le prochain nombre?"))
    Produit = Produit * NouvelleValeur
print("La valeur du produit de tout ces nombres est de",Produit)
