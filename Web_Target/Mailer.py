from tkinter import *
import tkinter.ttk as ttk
import Pmw
from Mail import Mail
from SendMail import SendMail

class Mailer(Tk):
    def __init__(self, mail):
        Tk.__init__(self)
        self.geometry("700x520")
        self.mail = mail
        self.liste_couleurs = [
            "Noir",
            "Rouge",
            "Vert",
            "Bleu"
        ]
        self.liste_couleurs_resolve = [
            "black",
            "red",
            "green",
            "blue"
        ]
        self.couleur = self.liste_couleurs_resolve[0]

        ## TOP = entêtes ##
        fTop = Frame(self)
        top = PanedWindow(fTop)
        Label(top, text="Expéditeur").grid(row=0, column=0)
        self.expediteur = Entry(top)
        self.expediteur.insert(INSERT, self.mail.getExpediteur())
        self.expediteur.grid(row=0, column=1)
        Label(top, text="Objet").grid(row=1, column=0)
        self.objet = Entry(top)
        self.objet.insert(INSERT, self.mail.getObjet())
        self.objet.grid(row=1, column=1)
        top.pack(side=TOP)
        fTop.pack(side=TOP)

        ## BOTTOM = corps ##
        fBot = PanedWindow(self)

        Label(fBot, text="Message").pack()
        self.message = Text(fBot, wrap=WORD, undo=TRUE)
        self.message.insert(INSERT, self.mail.getMessage())
        self.message.pack(side=BOTTOM)

        bot = PanedWindow(fBot)
        Button(bot, text="Gras", command=lambda: self.actionListener_widget('gras')).pack(side=LEFT)
        Button(bot, text="Italique", command=lambda: self.actionListener_widget('italique')).pack(side=LEFT)
        Button(bot, text="Souligner", command=lambda: self.actionListener_widget('souligner')).pack(side=LEFT)
        Button(bot, text="Couleur", command=lambda: self.actionListener_widget('couleur')).pack(side=LEFT)
        cb = ttk.Combobox(bot, values=(self.liste_couleurs[0], self.liste_couleurs[1], self.liste_couleurs[2], self.liste_couleurs[3]), state='readonly', width=8)
        cb.set(self.liste_couleurs[0])
        cb.pack(side=LEFT)
        cb.bind('<<ComboboxSelected>>', self.actionListener_couleur)
        Button(bot, text="Redo", command=self.message.edit_redo).pack(side=RIGHT)
        Button(bot, text="Undo", command=self.message.edit_undo).pack(side=RIGHT)
        bot.pack(side=TOP, fill=BOTH)

        fBot.pack(side=TOP)

        ## BOUTON continuer ##
        fFooter = Frame(self)
        Button(fFooter, text="Continuer", command=self.actionListener_continuer).pack()
        fFooter.pack(side=BOTTOM)

    def actionListener_couleur(self, event=None):
        if event:  # <-- this works only with bind because `command=` doesn't send event
            self.couleur = self.liste_couleurs_resolve[self.liste_couleurs.index(event.widget.get())]
            #self.actionListener_widget('couleur')

    def actionListener_widget(self, context):
        index = self.getIndex()
        if(context=='gras'):
            self.message.insert(index[1],'</b>')
            self.message.insert(index[0],'<b>')
        elif(context=='italique'):
            self.message.insert(index[1], '</i>')
            self.message.insert(index[0], '<i>')
        elif(context=='souligner'):
            self.message.insert(index[1], '</u>')
            self.message.insert(index[0], '<u>')
        elif(context=='couleur'):
            self.message.insert(index[1], '</font>')
            self.message.insert(index[0], '<font color="'+self.couleur+'">')

    # retourne True si du texte a été sélectionné, False sinon
    def isSelection(self):
        try:
            print(self.message.selection_own())
            return self.message.selection_get()!=''
        except:
            return False

    # retourne les coordonnées de la sélection
    def getSelectionIndexs(self):
        return [self.message.index(SEL_FIRST), self.message.index(SEL_LAST)]

    # retourne les coordonnées de la sélection, ou bien du curseur s'il n'y a pas de sélection
    def getIndex(self):
        if(self.isSelection()):
            return self.getSelectionIndexs()
        else:
            return [self.message.index(INSERT), self.message.index(INSERT)]

    def actionListener_continuer(self):
        self.mail.setExpediteur(self.expediteur.get())
        self.mail.setObjet(self.objet.get())
        self.mail.setMessage(self.message.get('1.0',END))
        self.destroy()
        SendMail(self.mail)

#Mailer(Mail()).mainloop()