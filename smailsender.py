import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#gonderim bilgilerini ayarla
sender="DEGIS!"
reciever ="DEGIS!"
password ="DEGIS!"

#mail icerigini ayarla
message="Merhaba Sergen Bey"
message1="<html><h1>SERGEN</h1></html>"

#MIME yapisi olustur(Email template olustur)
newmultipart=MIMEMultipart()
newmultipart['To']=reciever #kime
newmultipart['From']= sender #kimden
newmultipart['Subject']='COKOMELLI' #mail basligi


#Gonderecegin mesajlarin yapisini belirt ve olusturdugun template'e ekle
remessage=MIMEText(message,"plain")
remessage1=MIMEText(message1,"html")
newmultipart.attach(remessage)
newmultipart.attach(remessage1)

#mail gonder
newclient=smtplib.SMTP("smtp-mail.outlook.com",587)
newclient.starttls()
newclient.login(sender,password)
newclient.sendmail(sender,reciever,newmultipart.as_string())
