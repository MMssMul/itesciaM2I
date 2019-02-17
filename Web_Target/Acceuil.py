from tkinter import *
from Gestionnaire import Gestionnaire
from Fichier import Fichier
from Mail import Mail

class Acceuil(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.mail = Mail()
        self.source_var = StringVar()

        i=0
        while(i<4):
            j=0
            while(j<5):
                Label(self, text="  ").grid(row=i, column=j)
                j=j+1
            i=i+1

        label = Label(self, text="Nom Campagne").grid(row=1, column=2)
        #source = Label(self, text="fichier.csv").grid(row=2, column=2)
        self.source = Entry(self, textvariable=self.source_var).grid(row=2, column=2)
        action = Button(self, text="Fetch", command=lambda:self.actionListener_action()).grid(row=2, column=3)

    def actionListener_action(self):
        try:
            fichier = Fichier(self.source_var.get())
            #self.mail.setDesinataires(fichier.getMails())
            self.destroy()
            Gestionnaire(self.mail, fichier)
        except:
            pass

Acceuil().mainloop()