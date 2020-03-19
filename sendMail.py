import smtplib  # smtplib modulunu projemize ekledik
import time
import db

def sendVerify(verify):
    # Hesap bilgilerimiz
    pathronus = "pathronusproject@gmail.com"
    password = 'pp1234pp.'
    userMail= db.fetch("1","uMail") # yetkili kullanıcının mail adresi
    print(userMail)
    subject = 'Verify Code' # konu
    message = str(verify) #doğrulama kodunu tutar
    seconds = time.time()
    localTime = time.ctime(seconds)# time bilgisi

    # bilgileri bir metinde derledik
    emailText = """
    From: {}
    To: {}
    Subject: {}
    Time: {}
    {}
    """.format(pathronus, userMail, subject, localTime,message)

    server = smtplib.SMTP('smtp.gmail.com:587')  # servere bağlanmak için gerekli host ve portu belirttik
    server.starttls()  # serveri TLS(bütün bağlantı şifreli olucak bilgiler korunucak) bağlantısı ile başlattık
    server.login(pathronus, password)  # Gmail SMTP server'ına giriş yaptık
    server.sendmail(pathronus, userMail, emailText)  # Mail'imizi gönderdik
    server.close()  # SMTP serverimizi kapattık


#sendVerify(123456)
