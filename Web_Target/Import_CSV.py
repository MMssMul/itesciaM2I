from tkinter import *
from Fichier import Fichier

class Import_CSV(Toplevel):
    def __init__(self, fichier):
        Toplevel.__init__(self)
        self.fichier = fichier
        self.source_var = StringVar()

        i=0
        while(i<4):
            j=0
            while(j<5):
                Label(self, text="  ").grid(row=i, column=j)
                j=j+1
            i=i+1

        label = Label(self, text="Import URL").grid(row=1, column=2)
        self.source = Entry(self, textvariable=self.source_var).grid(row=2, column=2)
        action = Button(self, text="Import", command=lambda: self.importer()).grid(row=2, column=3)

    def importer(self):
        path = self.source_var.get()
        try:
            Fichier.addListeMails(self.fichier, Fichier.getMails(self.fichier, path))
        except:
            pass