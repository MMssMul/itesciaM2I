import os
import re
import requests
from bs4 import BeautifulSoup
from TestMail import TestMail

class Fichier:
    def __init__(self,chemin): #constructeur
        self.extension = chemin.split(".")[-1]  #extension du fichier à lire
        self.chemin = chemin #chemin du fichier
        self.separateur = ' '
        if (self.extension == "csv"):
            self.separateur = ";"

    def fichierLocal(self, path, liste_mails):
        if(os.path.exists(path)):
            fichier = open(path, "r")
            lines = fichier.readlines()
            for line in lines:
                tokens = line.split(self.separateur)
                for token in tokens:
                    #if (TestMail.isMail(token)):
                    if (token!='' and token!='\n' and token!='\r\n'):
                        liste_mails.append(token)
        elif(path == self.chemin):
            fichier = open(path, "w")
        fichier.close()


    def fichierWeb(self, path, liste_mails):
        code = requests.get(path)
        plain = code.text
        soup = BeautifulSoup(plain,"html.parser")
        for s in soup.find_all('a'):
            href = str(s.get('href'))
            if(href.startswith('mailto')):
                mail = href.split('mailto:')[1]
                #if(TestMail.isMail(mail)):
                liste_mails.append(mail)

    # retourne une liste de mails valides contenus dans le fichier
    def getMails(self, path):
        liste_mails = []
        regex = re.compile('^https?://')
        if(regex.match(path)):
            self.fichierWeb(path, liste_mails)
        else:
            self.fichierLocal(path, liste_mails)

        return list(set(liste_mails))  # retire les doublons

    # ajoute une liste de mails au fichier
    def addListeMails(self, liste_mails):
        if (os.path.exists(self.chemin)):
            fichier = open(self.chemin, "a+")
            fichier.seek(0)
            for mail in liste_mails:
                fichier.write(mail+self.separateur+'\n')
            fichier.close()

    # supprime une adresse mail du fichier
    def supprimeMail(self, str):
        if (os.path.exists(self.chemin)):
            fichier = open(self.chemin, "r+")
            text = fichier.read()
            text = re.sub(str+self.separateur, '', text)
            fichier.seek(0)
            fichier.write(text)
            fichier.truncate()
            fichier.close()

    # dedoublonne les adresses mails du fichier
    def dedoublonneMails(self):
        if (os.path.exists(self.chemin)):
            liste_mails = []
            fichier = open(self.chemin, "r+")
            lines = fichier.readlines()
            for line in lines:
                tokens = line.split(self.separateur)
                for token in tokens:
                    if (token != '' and token != '\n' and token != '\r\n'):
                        liste_mails.append(token)
            fichier.close()

            liste_mails = list(set(liste_mails))

            fichier = open(self.chemin, "w")
            for mail in liste_mails:
                fichier.write(mail+self.separateur+'\n')
            fichier.close()