import time

#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes
def tempsEnSeconde(temps):
    return(int(temps[0]) * 86400 + int(temps[1]) * 3600 + int(temps[2]) * 60 + int(temps[3]))
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    pass

temps = (3,23,1,34)

def secondeEnTemps(seconde):
    return((seconde//86400,(seconde//3600) % 24,(seconde//60) % 60,(seconde % 60)))
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    pass





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
    return secondeEnTemps(int(tempsEnSeconde(temps))*proportion)

afficheTemps(proportionTemps((2,0,36,0),0.2))
#appeler la fonction en échangeant l'ordre des arguments

"""


#---------------------------------------------------------------------------------------

def testBisextile(Annee):
    if Annee % 4 == 0 and (not Annee % 100 == 0 or Annee % 400 == 0):
        return(True)
    else:
        return(False)

def LongueurMois(Mois,Annee):
    if Mois == 2 and testBisextile(Annee):
        return(29)
    else:
        list_len_day = [31,28,31,30,31,30,31,31,30,31,30,31]
        return(list_len_day[Mois-1])

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
    return(Date)
    pass

def afficheDate(date):
    date = list(date)
    liste_nom_mois = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
    date[1] = liste_nom_mois[date[1]-1]
    for i in range (4,6):
        if date[i] == 0:
            date[i] = "00"
            print(date[i],i)
    print(date[2]," ",date[1]," ",date[0]," ",date[3],":",date[4],":",date[5],sep='')
    pass

afficheDate(tempsEnDate(secondeEnTemps(1665964800)))


def bisextile(jours):
    Annee = 2020
    jours_a_tester = 0
    while jours > jours_a_tester :
        if testBisextile(Annee):
            print(Annee,"est bisextile!")
            jours_a_tester += 366
        else:
            jours_a_tester += 365
        Annee += 1
    print("Terminé")
    pass

bisextile(20000)


def verifie(liste_temps):
    for i in range (len(liste_temps)):
        sumHoursMonth = 0
        for j in range (len(liste_temps[i])):
            sumHoursMonth = sumHoursMonth + (liste_temps[i])[j]
            if (liste_temps[i])[j] >= 48:
                print("Warning! Overtime detected in month",i+1,"week",j+1,"! Amount detected :",(liste_temps[i])[j])
        if sumHoursMonth >= 140:
            print("Warning! Overtime detected in month",i+1,"! Amount detected :",sumHoursMonth)
    pass



liste_temps = [[1, 2, 39, 34], [0, 1, 9, 4], [0, 29, 39, 51], [0, 31, 13, 46]]
verifie(liste_temps)
