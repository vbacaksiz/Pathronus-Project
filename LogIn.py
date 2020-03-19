from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QErrorMessage
from Pathronus import *
import db
import sendMail
import random


# First Log in gerçekleştirildikten ve ilk kullanıcı eklendikten sonra program çalıştırıldığında açılacak ekran
class Ui_LogIn(object):

    def LogInUi(self, LogIn):

        db.updateInfo("1", "verifyCode", None)
        LogIn.setObjectName("LogIn")
        LogIn.resize(470, 333)
        self.centralwidget = QtWidgets.QWidget(LogIn)
        self.centralwidget.setObjectName("centralwidget")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(110, 10, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 310, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # Oluşturulan tab widget ile Log In ve Forgot Password tabları oluşturuldu
        self.LogIn_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.LogIn_tabWidget.setGeometry(QtCore.QRect(0, 40, 470, 261))
        self.LogIn_tabWidget.setObjectName("LogIn_tabWidget")

        # Kullanıcının bilglerini girip Log In yaptığı tab
        self.LogIn_Tab = QtWidgets.QWidget()
        self.LogIn_Tab.setObjectName("LogIn_Tab")

        self.label_3 = QtWidgets.QLabel(self.LogIn_Tab)
        self.label_3.setGeometry(QtCore.QRect(100, 40, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.LogIn_Tab)
        self.label_4.setGeometry(QtCore.QRect(90, 80, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.LogIn_Tab)
        self.label_5.setGeometry(QtCore.QRect(100, 120, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        # User Name yazılacak Line Edit
        self.email = QtWidgets.QLineEdit(self.LogIn_Tab)
        self.email.setGeometry(QtCore.QRect(180, 80, 113, 25))
        self.email.setObjectName("username")

        # Password yazılacak Line Edit
        self.password = QtWidgets.QLineEdit(self.LogIn_Tab)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setGeometry(QtCore.QRect(180, 120, 113, 25))
        self.password.setObjectName("password")

        # Kullanıcı bilgileri doğruysa Pathronus olarak isimlendirilen programın ana ekranına geçiş yapan Log In butonu
        self.LogIn_LogIn_Button = QtWidgets.QPushButton(self.LogIn_Tab)
        self.LogIn_LogIn_Button.setGeometry(QtCore.QRect(190, 160, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.LogIn_LogIn_Button.setFont(font)
        self.LogIn_LogIn_Button.setObjectName("LogIn_LogIn_Button")
        self.LogIn_LogIn_Button.clicked.connect(self.logInToProgram)

        self.LogIn_tabWidget.addTab(self.LogIn_Tab, "")

        # Kullanıcın parolasını unutması halinde gitmesi gereken Forgot Password tabı
        self.ForgotPassword_Tab = QtWidgets.QWidget()
        self.ForgotPassword_Tab.setObjectName("ForgotPassword_Tab")

        self.label_6 = QtWidgets.QLabel(self.ForgotPassword_Tab)
        self.label_6.setGeometry(QtCore.QRect(130, 50, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.ForgotPassword_Tab)
        self.label_7.setGeometry(QtCore.QRect(110, 80, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.ForgotPassword_Tab)
        self.label_8.setGeometry(QtCore.QRect(60, 120, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.ForgotPassword_Tab)
        self.label_9.setGeometry(QtCore.QRect(50, 150, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_29")

        # Kullanıcının doğrulanması için e-postasına kod göndermeyi sağlayan buton
        self.ForgotPassword_SendCode_Button = QtWidgets.QPushButton(self.ForgotPassword_Tab)
        self.ForgotPassword_SendCode_Button.setGeometry(QtCore.QRect(190, 10, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.ForgotPassword_SendCode_Button.setFont(font)
        self.ForgotPassword_SendCode_Button.setObjectName("ForgotPassword_SendCode_Button_1")
        self.ForgotPassword_SendCode_Button.clicked.connect(self.sendCode)

        # Kullanıcın e-posta yolu ile gönderilen kodu yazacağı Line Edit
        self.verifyCode = QtWidgets.QLineEdit(self.ForgotPassword_Tab)
        self.verifyCode.setGeometry(QtCore.QRect(180, 50, 113, 25))
        self.verifyCode.setObjectName("verifyCode")

        # Kullanıcı kod gönderildikten sonra yeni bir parola girmelidir
        self.newUserPassword = QtWidgets.QLineEdit(self.ForgotPassword_Tab)
        self.newUserPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newUserPassword.setGeometry(QtCore.QRect(180, 120, 113, 25))
        self.newUserPassword.setObjectName("newUserPassword")

        # Yeni parolanın doğrulanması için parola tekrar girilmelidir
        self.newUserPasswordConfirm = QtWidgets.QLineEdit(self.ForgotPassword_Tab)
        self.newUserPasswordConfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newUserPasswordConfirm.setGeometry(QtCore.QRect(180, 150, 113, 25))
        self.newUserPasswordConfirm.setObjectName("newUserPasswordConfirm")

        # Girilen kodun doğruluğunu ve iki kere girilen yeni parolanın uyuşup uyuşmadığının kontrol edilmesini sağlayan ve uyuyorsa parolayı yenileyen buton(.
        # Sadece yetkili kullanıcı(İlk kayıt olan) parola değişebilir.)
        self.ForgotPassword_Enter_Button = QtWidgets.QPushButton(self.ForgotPassword_Tab)
        self.ForgotPassword_Enter_Button.setGeometry(QtCore.QRect(190, 190, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.ForgotPassword_Enter_Button.setFont(font)
        self.ForgotPassword_Enter_Button.setObjectName("ForgotPassword_SendCode_Button_2")
        self.ForgotPassword_Enter_Button.clicked.connect(self.changePassword)

        self.LogIn_tabWidget.addTab(self.ForgotPassword_Tab, "")

        LogIn.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogIn)
        self.LogIn_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LogIn)

    # Log In butonuna basıldığında veri tabanından doğruluk kontrolü yapan ve bilgiler doğruysa Pathronus ekranına geçiş sağlayan fonksiyon
    def logInToProgram(self):
        email = self.email.text()

        password = self.password.text()

        if email == db.fetch("1", "uMail"):
            if password == db.fetch("1", "uPassword"):
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_Pathronus()
                self.ui.PathronusUi(self.window)
                self.window.show()
                LogIn.close()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Parolalar Eşleşmedi")
                msg.setInformativeText('Lütfen Uyuşan Parolalar giriniz')
                msg.setWindowTitle("Parolalar Eşleşmedi")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Böyle Bir Email Bulunamadı")
            msg.setInformativeText('Lütfen Kayıt Olduğunuz Emaili giriniz')
            msg.setWindowTitle("Email Hatası")
            msg.exec_()

    # sendCode fonksiyonu yazılacak
    def sendCode(self):
        rand = random.randrange(int("1" + "0" * 5), int("1" + "0" * 6))
        db.updateInfo("1", "verifyCode", str(rand))
        sendMail.sendVerify(rand)

    # Parolayı değiştirme tabında bulunan formun doğruluğunun kontrolü yapılır.
    def changePassword(self):
        verifyCode = int(self.verifyCode.text())
        newUserPassword = self.newUserPassword.text()
        newUserPasswordConfirm = self.newUserPasswordConfirm.text()

        if verifyCode == db.fetch("1", "verifyCode"):
            if newUserPassword == newUserPasswordConfirm:
                if newUserPassword == db.fetch("1", "uPassword"):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Parola Eski Parola İle Aynı")
                    msg.setInformativeText('Lütfen Yeni Bir Parola Giriniz.')
                    msg.setWindowTitle("Aynı Parola")
                    msg.exec_()
                else:
                    db.updateInfo("1", "uPassword", newUserPassword)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Parolanız Başarı İle Değiştirildi.")
                    msg.setWindowTitle("Başarılı İşlem")
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Parolalar Eşleşmedi")
                msg.setInformativeText('Lütfen Uyuşan Parolalar Giriniz.')
                msg.setWindowTitle("Parolalar Eşleşmedi!")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Doğrulama Kodu Hatalı")
            msg.setInformativeText('Doğrulama Kodu Uyuşmadı')
            msg.setWindowTitle("Kod Hatalı")
            msg.exec_()

    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "Pathronus"))
        self.label_1.setText(_translate("LogIn", "Welcome To Pathronus Project"))
        self.label_2.setText(_translate("LogIn", "A University Project Created By Pathronus"))
        self.label_3.setText(_translate("LogIn", "Please Enter Your User Informations"))
        self.label_4.setText(_translate("LogIn", "   E-mail:"))
        self.label_5.setText(_translate("LogIn", "Password:"))
        self.LogIn_LogIn_Button.setText(_translate("LogIn", "Log In"))
        self.LogIn_tabWidget.setTabText(self.LogIn_tabWidget.indexOf(self.LogIn_Tab), _translate("LogIn", "Log In"))
        self.label_6.setText(_translate("LogIn", "Code:"))
        self.label_7.setText(_translate("LogIn", "You Have To Change Your Password"))
        self.label_8.setText(_translate("LogIn", "New Password:"))
        self.label_9.setText(_translate("LogIn", "Password Again:"))
        self.ForgotPassword_SendCode_Button.setText(_translate("LogIn", "Send Code"))
        self.ForgotPassword_Enter_Button.setText(_translate("LogIn", "Enter"))
        self.LogIn_tabWidget.setTabText(self.LogIn_tabWidget.indexOf(self.ForgotPassword_Tab),_translate("LogIn", "Forgot Password"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QMainWindow()
    ui = Ui_LogIn()
    ui.LogInUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())
