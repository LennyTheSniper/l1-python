#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes
def tempsEnSeconde(temps):
    return(int(temps[0]) * 86400 + int(temps[1]) * 3600 + int(temps[2]) * 60 + int(temps[3]))
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    pass

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))

def secondeEnTemps(seconde):
    return((seconde//86400,(seconde//3600) % 24,(seconde//60) % 60,(seconde % 60)))
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    pass
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")




def afficheTemps(temps):
    if temps[0] == 0:
        print(end='')
    elif temps[0] == 1:
        print(temps[0],"jour",end=' ')
    else:
        print(temps[0],"jours",end=' ')
    if temps[1] == 0:
        print(end='')
    elif temps[1] == 1:
        print(temps[1],"heure",end=' ')
    else:
        print(temps[1],"heures",end=' ')
    if temps[2] == 0:
        print(end='')
    elif temps[2] == 1:
        print(temps[2],"minute",end=' ')
    else:
        print(temps[2],"minutes",end=' ')
    if temps[3] == 0:
        print(end='\n')
    elif temps[3] == 1:
        print(temps[3],"seconde",end='\n')
    else:
        print(temps[3],"secondes",end='\n')
    pass

afficheTemps((1,0,14,23)) 




"""
def demandeTemps():
    secondes = -1
    minutes = -1
    heures = -1
    jours = -1
    while secondes < 0 or secondes > 59:
        secondes = int(input("Combien de secondes voulez vous ajouter?"))
    while minutes < 0 or minutes > 59:
        minutes = int(input("Combien de minutes voulez vous ajouter?"))
    while heures < 0 or heures > 23:
        heures = int(input("Combien de heures voulez vous ajouter?"))
    while jours < 0:
        jours = int(input("Combien de jours voulez vous ajouter?"))
    return((jours,heures,minutes,secondes))
    pass

afficheTemps(demandeTemps())
"""





def sommeTemps(temps1,temps2):
    tempsa = temps1[3] + temps2[3]
    tempsb = temps1[2] + temps2[2]
    tempsc = temps1[1] + temps2[1]
    tempsd = temps1[0] + temps2[0]
    while tempsa>=60:
        tempsa -= 60
        tempsb += 1
    while tempsb>=60:
        tempsb -= 60
        tempsc += 1
    while tempsc>=24:
        tempsc -= 24
        tempsd += 1
    return((tempsd,tempsc,tempsb,tempsa))
    pass

afficheTemps(sommeTemps((2,3,4,25),(5,22,57,1)))






def proportionTemps(temps,proportion):
    return(secondeEnTemps(int((tempsEnSeconde(temps))*proportion)))
    pass
afficheTemps(proportionTemps((2,0,36,0),0.2))
#appeler la fonction en échangeant l'ordre des arguments





def testBisextile(Annee):
    if Annee % 4 == 0 and (not Annee % 100 == 0 or Annee % 400 == 0):
        return(True)
    else:
        return(False)

def LongueurMois(Mois,Annee):
    if Mois % 2 == 1 :
        return(31)
    elif Mois == 2 and testBisextile(Annee) == True:
        return(29)
    elif Mois == 2 and testBisextile(Annee) == False:
        return(28)
    elif Mois % 2 == 0:
        return(30)

def tempsEnDate(temps):
    Date = list((1970,1,1,0,0,0))
    Date[5] += temps[3]
    Date[4] += temps[2]
    Date[3] += temps[1]
    Date[2] += temps[0]
    while Date[2] > LongueurMois(Date[1],Date[0]):
        Date[2] -= LongueurMois(Date[1],Date[0])
        Date[1] += 1
        while Date[1] > 12:
            Date[1] -= 12
            Date[0] += 1
    Date = tuple((Date[0],Date[1],Date[2],Date[3],Date[4],Date[5]))
    print(Date)
    pass

def afficheDate(date2):
    if date2[1] == 1:
        date2[1] = 'Janvier'
    elif date2[1] == 2:
        date2[1] = 'Fevrier'
    elif date2[1] == 3:
        date2[1] = 'Mars'
    elif date2[1] == 4:
        date2[1] = 'Avril'
    elif date2[1] == 5:
        date2[1] = 'Mai'
    elif date2[1] == 6:
        date2[1] = 'Juin'
    elif date2[1] == 7:
        date2[1] = 'Juillet'
    elif date2[1] == 8:
        date2[1] = 'Aôut'
    elif date2[1] == 9:
        date2[1] = 'Septembre'
    elif date2[1] == 10:
        date2[1] = 'Octobre'
    elif date2[1] == 11:
        date2[1] = 'Novembre'
    else:
        date2[1] = 'Décembre'
    print(date2[2]," ",date2[1]," ",date2[0],date2[3],":",date2[4],":",date2[5],sep='')
    pass
    
temps = secondeEnTemps(1000000000)
tempsEnDate(temps)
print(afficheDate(tempsEnDate(temps)))