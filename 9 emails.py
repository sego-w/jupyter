import email
import imaplib
import smtplib
import getpass
'''
Setting up the server I think?
'''
smtpl = smtplib.SMTP('smtp.gmail.com',587)
smtpl.ehlo()
smtpl.starttls()

mail = input("What email are we using today? ")
password = input("Please enter the application password: ")
smtpl.login(mail,password)

#Test mail
frommail = mail
tomail = mail
subj = input("What is the subject of the email? ")
body = input("What are the contents of the email? ")
message = "Subject: "+subj+'\n'+body

smtpl.sendmail(frommail,tomail,message)