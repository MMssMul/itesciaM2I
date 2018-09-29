# ECOLE         : ITESCIA
# FORMATION     : M2I L3
# ANNEE         : 2018/2019
# ETUDIANT      : Jeremy BEAUFORT
# ENVIRONNEMENT : python 3.6.2

import re  # bibliotheque pour expressions regulieres

# Verifie si la chaine passee en parametre est une date, voire une date gregorienne
# @param string
# @return 0 = pas une date, 1 = date gregorinne, 2 = date non gregorienne
def isDateGreg(str):
    if(re.sub('^(0?[1-9]|[12][0-9]|3[01])[\/](0?[1-9]|1[012])[\/][0-9]{4}$', "", str)):
        return 0  # n'est pas une date
    substr = str.split('/')
    if (int(substr[2]) > 1582 or (int(substr[2]) == 1582 and int(substr[1]) >= 11)):
        return 1  # est une date gregorienne
    return 2  # est une date

# Verifie si une l'annee passee en parametre est bissextile
# @param year
# @return vrai = True, faux = False
# @note :
# - la fonction est utilisee uniquement apres avoir verifier la date
# - l'annee correspond obligatoirement a l'annee d'une date valide
def isBissextile(year):
    year = int(year)  # enleve les zeros inutiles de debut de chaine
    if(year%400==0):
        return True
    elif(year%100==0):
        return False
    elif(year%4==0):
        return True
    return False

# Retourne le valeur associee a chaque mois, pour trouver le jour de la semaine d'une annee gregorienne
# @param month
# @return integer
# @note :
# - la fonction est utilisee uniquement apres avoir verifier la date
# - le mois correspond obligatoirement a un mois d'une date valide
def getMonthAssocValue(month):
    m = int(month)  # enleve les zeros inutiles de debut de chaine
    if (m == 1 or m == 10):
        return 0  # Janvier, Octobre
    elif (m == 2 or m == 3 or m == 11):
        return 3  # Fevrier, Mars, Novembre
    elif (m == 4 or m == 7):
        return 6  # Avril, Juillet
    elif (m == 5):
        return 1  # Mais
    elif (m == 6):
        return 4  # Juin
    elif (m == 8):
        return 2  # Aout
    elif (m == 9 or m == 12):
        return 5  # Septembre, Decembre

# Retourne le valeur associee au siecle, pour trouver le jour de la semaine d'une annee gregorienne
# @param century
# @return integer
# @note :
# - siecle minimum = 1600
def getCenturyAssocValue(century):
    c = int(century) - 1500
    if(c%400==0):
        return 0
    elif(c%300==0):
        return 2
    elif(c%200==0):
        return 4
    return 6

# Retourne le l'indice associe au jour de la semaine, pour trouver le jour de la semaine d'une annee gregorienne
# @param date
# @return integer
# @note :
# - la date est suposee valide et au format 'dd/mm/yyyy'
def getIndexOfDay(date):
    dateExploded = date.split('/')  # separation des informations de la date
    fragYearFin = int(dateExploded[2][2] + dateExploded[2][3])  # deux derniers digits de l'annee
    fragYearFinQuart = fragYearFin // 4
    day = int(dateExploded[0])  # jour
    month = int(dateExploded[1])  #mois
    valMonth = int(getMonthAssocValue(month))  # valeur associee au mois
    arroundYear = int(dateExploded[2][0] + dateExploded[2][1] + '0' + '0')  # annee arrondie a la centaine
    valCentury = int(getCenturyAssocValue(arroundYear))  # valeur associee a l'annee arrondie
    bissextile =  1 if (isBissextile(arroundYear) and (int(dateExploded[1]) == 1 or int(dateExploded[1]) == 2)) else 0  # test annee bissextile et mois = janvier ou fevrier

    return int(fragYearFin+fragYearFinQuart+day+valMonth-bissextile+valCentury)%7

# Corps du programme
def main():
    str_saisie = "Saisir une date gregorienne au format 'dd/mm/yyyy' >= [0]1/11/1582\n"

    # Saisie de la date par l'utilisateur
    date = input(str_saisie)

    # Boucle sur la saisie si la saisie est erronee
    while(isDateGreg(date)!=1):
        if(isDateGreg(date)==2):
            print('\nLa date saisie n\'est pas une date gregorienne !')
        else:
            print('\nLa saisie est incorrecte !')
        date = input(str_saisie)

    # Liste des jours de la semaine
    days = ['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi']

    # Affichage du jour de la semaine
    print('Jour => ',days[getIndexOfDay(date)])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

# AAPPEL DE LA FONCTION MAIN
main()