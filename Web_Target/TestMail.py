import os
import re
import requests
from bs4 import BeautifulSoup
import requests
from html.parser import HTMLParser
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

class TestMail():
    # envoie un mail
    def sendMail(self, exp, dest, obj, msg):
        mail = []
        host = 'smtp.gmail.com'
        server = smtplib.SMTP(host, 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("snexonnoreply@gmail.com", "snexon123")
        for d in dest:
            message = MIMEMultipart()
            message['From'] = exp
            message['To'] = d
            message['Subject'] = obj
            message.attach(MIMEText(msg, 'html'))
            server.send_message(message)
        server.quit()

    # vérifie si le webmail existe
    def isWebmailValide(str):
        if(os.system('ping '+str+' -a -n 1')):
            return False
        return True

    # vérifie si le mail est valide
    def isMail(str):
        substr = str.split("@")
        if(substr[0]=='' or len(substr)==1):
            return False
        webmail = substr[-1]
        domaine = webmail.split(".")[-1]
        if(domaine=="fr" or domaine=="com"):
            return TestMail.isWebmailValide(webmail)
        return False
