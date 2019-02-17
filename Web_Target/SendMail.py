from tkinter import *
from TestMail import TestMail
from Mail import Mail

class SendMail(Tk):
    def __init__(self, mail):
        Tk.__init__(self)
        self.geometry("700x520")
        self.mail = mail
        self.source_var = StringVar()

        top = PanedWindow(self)
        Button(top, text='Tester', command=self.actionListener_tester).pack(side=LEFT)
        self.dest_test = Entry(top, textvariable=self.source_var).pack(side=RIGHT)
        top.pack(side=TOP)


        bot = PanedWindow(self)
        self.message = Text(bot, wrap=WORD)
        self.message.insert('1.0', self.mail.getMessage())
        self.message.pack(side=TOP)
        Button(bot, text='Envoyer', command=self.actionListener_valider).pack(side=BOTTOM)
        bot.pack(side=BOTTOM)

    def actionListener_tester(self):
        try:
            TestMail().sendMail(self.mail.getExpediteur(), self.source_var.get(),  self.mail.getObjet(), self.mail.getMessage())
        except:
            print('except: échec envoie de mail')

    def actionListener_valider(self):
        try:
            TestMail().sendMail(self.mail.getExpediteur(), self.mail.getDestinataires(),  self.mail.getObjet(), self.mail.getMessage())
        except:
            print('except')
"""
m = Mail()
m.setMessage("message test")
SendMail(m).mainloop()
"""