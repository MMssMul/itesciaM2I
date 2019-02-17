from tkinter import *
from TestMail import TestMail
from Import_CSV import Import_CSV
from Import_URL import Import_URL
from Importer import Importer
from Fichier import Fichier
from Mail import Mail
from Mailer import Mailer

class Gestionnaire(Tk):
    def __init__(self,mail,fichier):
        Tk.__init__(self)
        self.mail = mail
        self.fichier = fichier
        self.geometry("350x400")

        #self.liste_mails= ['mail1', 'mail2']
        #self.fichier.addListeMails(self.liste_mails)

        ## TOP ##
        top = PanedWindow(self)
        top_top = PanedWindow(top, orient=HORIZONTAL)
        top_bot = PanedWindow(top, orient=HORIZONTAL)

        dedoublonner = Button(top_top, text="Dédoublonner", command=self.actionListener_dedoublonner).pack(side=LEFT)
        valider = Button(top_top, text="Valider", command=self.actionListener_valider).pack(side=RIGHT)
        importer = Button(top_top, text="Importer", command=lambda: Importer(self.fichier)).pack(side=LEFT)
        #import_csv = Button(top_bot, text="Import CSV", command=lambda: Import_CSV(self.fichier)).pack(side=LEFT)
        #import_url = Button(top_bot, text="Import URL", command=lambda: Import_URL(self.fichier)).pack(side=RIGHT)

        top_top.pack(side=TOP)
        top_bot.pack(side=BOTTOM)
        top.pack(side=TOP)


        ## BOT ##
        self.bot = PanedWindow(self)
        self.bottom = self.paint(self.bot, 0)
        self.bottom.pack(side=TOP)
        """
        for mail in mail.getDestinataires():
            panel = PanedWindow(bot, orient=HORIZONTAL)
            adresse_mail = Label(panel, text=mail).pack(side=LEFT)
            adresse_valide = Label(panel, text="        OK" if TestMail.isMail(mail) else "PAS OK").pack(side=LEFT)
            supprimer = Button(panel, text="X").pack(side=RIGHT)
            panel.pack(anchor="e")

        """
        self.bot.pack(side=TOP)
        suite = Button(self, text="Suite", command=self.actionListener_suite).pack(side=BOTTOM)

    def paint(self, pan, mode):
        bot = PanedWindow(pan)
        self.mail.setDesinataires(self.fichier.getMails(self.fichier.chemin))
        for mail in self.mail.getDestinataires():
            panel = PanedWindow(bot, orient=HORIZONTAL)
            adresse_mail = Label(panel, text=mail).pack(side=LEFT)
            if(mode==1):
                etat = "OK" if (mode == 1 and TestMail.isMail(mail)) else "PAS OK"
            else:
                etat = "???"
            adresse_valide = Label(panel, text=etat).pack(side=LEFT)
            supprimer = Button(panel, text="X", command=lambda email=mail: self.actionListener_supprimer(email)).pack(side=RIGHT)
            panel.pack(anchor="e")

        return bot

    def repaint(self):
        self.bottom.destroy()
        self.bottom = self.paint(self.bot, 1)
        self.bottom.pack(side=TOP)

    def actionListener_dedoublonner(self):
        Fichier.dedoublonneMails(self.fichier)
        self.repaint()

    def actionListener_valider(self):
        self.repaint()

    def actionListener_supprimer(self, mail):
        Fichier.supprimeMail(self.fichier,mail)
        self.repaint()

    def actionListener_suite(self):
        if(self.mail.getDestinataires().__len__()>0):
            self.destroy()
            Mailer(self.mail)