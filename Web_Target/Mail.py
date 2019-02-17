class Mail():
    def __init__(self):
        self.expediteur = ""
        self.destinataires = []
        self.objet = ""
        self.message = ""

    ## MUTATEURS ##
    def setExpediteur(self, new):
        self.expediteur = new

    def setDesinataires(self, new):
        self.destinataires = new

    def setObjet(self, new):
        self.objet = new

    def setMessage(self, new):
        self.message = new

    ## ACCESSEURS ##
    def getExpediteur(self):
        return self.expediteur

    def getDestinataires(self):
        return self.destinataires

    def getObjet(self):
        return self.objet

    def getMessage(self):
        return self.message