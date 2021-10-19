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
        print(temps[1],"jour",end=' ')
    else:
        print(temps[1],"jours",end=' ')
    if temps[2] == 0:
        print(end='')
    elif temps[2] == 1:
        print(temps[2],"jour",end=' ')
    else:
        print(temps[2],"jours",end=' ')
    if temps[3] == 0:
        print(end='')
    elif temps[3] == 1:
        print(temps[3],"jour",end=' ')
    else:
        print(temps[3],"jours",end=' ')
    pass

afficheTemps((1,0,14,23)) 





def demandeTemps():
    secondes = -1
    minutes = -1
    heures = -1
    jours = -1
    while secondes < 0 or secondes > 60:
        secondes = int(input("Combien de secondes voulez vous ajouter?"))
    while minutes < 0 or minutes > 60:
        minutes = int(input("Combien de minutes voulez vous ajouter?"))
    while heures < 0 or heures > 60:
        heures = int(input("Combien de heures voulez vous ajouter?"))
    while jours < 0 or jours > 60:
        jours = int(input("Combien de jours voulez vous ajouter?"))
    return((jours,heures,minutes,secondes))
    pass

afficheTemps(demandeTemps())