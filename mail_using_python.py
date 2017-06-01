import smtplib
import getpass

#doesnot work with iitb lan and wifi why ? must know
#and for this to work you have to enable the access gmail using less secure apps on

smtpobj=smtplib.SMTP('smtp.gmail.com',587)  #if this doenot work use SMTP_ssl and port 465
smtpobj.ehlo() #make connection with server

smtpobj.starttls()  #start a TLS encryption
my_email=raw_input("Please Enter Your email address: ")
password=getpass.getpass("Please Enter Your password: ") #password is not echoed using getpass
smtpobj.login(my_email,password)
to_email=raw_input("Please Enter the mail address of receiver: ")
subject=raw_input("please Enter the Subject: ")
mail=raw_input("Please Enter the mail: ")

smtpobj.sendmail(my_email,to_email,"Subject:"+subject+"\n"+mail)

smtpobj.quit()

print "mail was sent successfully"
