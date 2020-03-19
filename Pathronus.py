from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import db
import faceDataSet
import faceTraining
import faceRecognition


class Ui_Pathronus(object):

    #Arayüz tablar kullanılarak yeniden düzenlendi bazı geçiş sorunaları giderildi
    def PathronusUi(self, Pathronus):

        Pathronus.setObjectName("Pathronus")
        Pathronus.resize(532, 424)
        self.centralwidget = QtWidgets.QWidget(Pathronus)
        self.centralwidget.setObjectName("centralwidget")
        self.Pathronus_TabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.Pathronus_TabWidget.setGeometry(QtCore.QRect(0, 50, 532, 311))
        self.Pathronus_TabWidget.setObjectName("Pathronus_TabWidget")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(130, 10, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 400, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        #Pathronus ana ekran tabı
        self.Pathronus_Tab = QtWidgets.QWidget()
        self.Pathronus_Tab.setObjectName("Pathronus_Tab")

        self.PathronusMainText = QtWidgets.QLabel(self.Pathronus_Tab)
        self.PathronusMainText.setGeometry(QtCore.QRect(0, 0, 531, 281))
        self.PathronusMainText.setToolTipDuration(-1)
        self.PathronusMainText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PathronusMainText.setTextFormat(QtCore.Qt.RichText)
        self.PathronusMainText.setObjectName("PathronusMainText")
        self.Pathronus_TabWidget.addTab(self.Pathronus_Tab, "")

        #Kullanıcı ekleme tabı
        self.AddUser_Tab = QtWidgets.QWidget()
        self.AddUser_Tab.setObjectName("AddUser_Tab")

        self.label_3 = QtWidgets.QLabel(self.AddUser_Tab)
        self.label_3.setGeometry(QtCore.QRect(130, 40, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.AddUser_Tab)
        self.label_4.setGeometry(QtCore.QRect(110, 90, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.AddUser_Tab)
        self.label_5.setGeometry(QtCore.QRect(120, 130, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.AddUser_Tab)
        self.label_6.setGeometry(QtCore.QRect(70, 170, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.username = QtWidgets.QLineEdit(self.AddUser_Tab)
        self.username.setGeometry(QtCore.QRect(200, 90, 113, 25))
        self.username.setObjectName("username")

        self.password = QtWidgets.QLineEdit(self.AddUser_Tab)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setGeometry(QtCore.QRect(200, 130, 113, 25))
        self.password.setObjectName("password")

        self.passwordConfirm = QtWidgets.QLineEdit(self.AddUser_Tab)
        self.passwordConfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordConfirm.setGeometry(QtCore.QRect(200, 170, 113, 25))
        self.passwordConfirm.setObjectName("passwordConfirm")

        self.AddUser_Button = QtWidgets.QPushButton(self.AddUser_Tab)
        self.AddUser_Button.setGeometry(QtCore.QRect(210, 210, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.AddUser_Button.setFont(font)
        self.AddUser_Button.setObjectName("AddUser_Button")
        self.AddUser_Button.clicked.connect(self.addUser)

        self.Pathronus_TabWidget.addTab(self.AddUser_Tab, "")

        #Kullanıcı silme tabı
        self.RemoveUser_Tab = QtWidgets.QWidget()
        self.RemoveUser_Tab.setObjectName("RemoveUser_Tab")

        #Kullanıcı listesinin görüneceği tablo widget
        self.RemoveUser_Table = QtWidgets.QTableWidget(self.RemoveUser_Tab)
        self.RemoveUser_Table.setGeometry(QtCore.QRect(180, 50, 121, 181))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.RemoveUser_Table.setFont(font)
        self.RemoveUser_Table.setRowCount(5)
        self.RemoveUser_Table.setColumnCount(1)
        self.RemoveUser_Table.setObjectName("RemoveUser_Table")



        self.label_7 = QtWidgets.QLabel(self.RemoveUser_Tab)
        self.label_7.setGeometry(QtCore.QRect(160, 20, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        #Mevcut kullanıcıları yenilemek için oluşturulan buton
        self.RemoveUser_Refresh_Button = QtWidgets.QPushButton(self.RemoveUser_Tab)
        self.RemoveUser_Refresh_Button.setGeometry(QtCore.QRect(150, 240, 89, 25))
        self.RemoveUser_Refresh_Button.setObjectName("RemoveUser_Refresh_Button")
        self.RemoveUser_Refresh_Button.clicked.connect(self.refreshTable)

        #Tablodan seçilen kullanıcıları silmek için kullanılan buton
        self.RemoveUser_Remove_Button = QtWidgets.QPushButton(self.RemoveUser_Tab)
        self.RemoveUser_Remove_Button.setGeometry(QtCore.QRect(260, 240, 89, 25))
        self.RemoveUser_Remove_Button.setObjectName("RemoveUser_Remove_Button")
        self.RemoveUser_Remove_Button.clicked.connect(self.removeUser)

        self.Pathronus_TabWidget.addTab(self.RemoveUser_Tab, "")

        #Parola değiştirmek için oluşturulan tab
        self.ChangePassword_Tab = QtWidgets.QWidget()
        self.ChangePassword_Tab.setObjectName("ChangePassword_Tab")

        self.label_8 = QtWidgets.QLabel(self.ChangePassword_Tab)
        self.label_8.setGeometry(QtCore.QRect(140, 50, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.ChangePassword_Tab)
        self.label_9.setGeometry(QtCore.QRect(90, 100, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.ChangePassword_Tab)
        self.label_10.setGeometry(QtCore.QRect(80, 140, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        #Belirlenen yeni parolanın girildiği metin yazma yeri
        self.newPassword = QtWidgets.QLineEdit(self.ChangePassword_Tab)
        self.newPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPassword.setGeometry(QtCore.QRect(200, 100, 113, 25))
        self.newPassword.setObjectName("newPassword")

        #Yeni parolanın tekrar girilmesi
        self.newPasswordConfirm = QtWidgets.QLineEdit(self.ChangePassword_Tab)
        self.newPasswordConfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPasswordConfirm.setGeometry(QtCore.QRect(200, 140, 113, 25))
        self.newPasswordConfirm.setObjectName("newPasswordConfirm")

        #Yeni parolanın veri tabanına kaydedilmesi için kullanılan buton
        self.ChangePassword_Enter_Button = QtWidgets.QPushButton(self.ChangePassword_Tab)
        self.ChangePassword_Enter_Button.setGeometry(QtCore.QRect(210, 180, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.ChangePassword_Enter_Button.setFont(font)
        self.ChangePassword_Enter_Button.setObjectName("ChangePassword_Enter_Button")
        self.ChangePassword_Enter_Button.clicked.connect(self.changePassword)

        self.Pathronus_TabWidget.addTab(self.ChangePassword_Tab, "")

        #Hali hazırda giriş yapmış kullanıcıya fotoğraf eklemek için kullanılan buton
        self.AddPicture_Button = QtWidgets.QPushButton(self.centralwidget)
        self.AddPicture_Button.setGeometry(QtCore.QRect(440, 360, 91, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.AddPicture_Button.setFont(font)
        self.AddPicture_Button.setObjectName("AddPicture_Button")

        #Programın başlatılması için kullanılan buton
        self.EnableProgram_Button = QtWidgets.QPushButton(self.centralwidget)
        self.EnableProgram_Button.setGeometry(QtCore.QRect(0, 360, 151, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.EnableProgram_Button.setFont(font)
        self.EnableProgram_Button.setObjectName("EnableProgram_Button")
        self.EnableProgram_Button.clicked.connect(self.programEnable)

        Pathronus.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pathronus)
        self.Pathronus_TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Pathronus)

    def retranslateUi(self, Pathronus):

        _translate = QtCore.QCoreApplication.translate
        Pathronus.setWindowTitle(_translate("Pathronus", "Pathronus"))
        self.label_1.setText(_translate("Pathronus", "Welcome To Pathronus Project"))
        self.label_2.setText(_translate("Pathronus", "A University Project Created By Pathronus"))
        self.PathronusMainText.setText(_translate("Pathronus", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Welcome to Pathronus Project. This project is created for a univercity</span></p><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">project by Pathronus group.</span></p><p><span style=\" font-weight:600; text-decoration: underline;\">Lesson:</span><span style=\" font-style:italic;\">Software Engineering</span></p><p><span style=\" font-weight:600; text-decoration: underline;\">Teacher: </span><span style=\" font-style:italic;\">Sedat Görmüş</span></p><p><span style=\" font-weight:600; text-decoration: underline;\">Group Members:</span></p><p><span style=\" font-style:italic;\">Ahmet Uğur Arıkan</span></p><p><span style=\" font-style:italic;\">Volkan Can Bacaksız</span></p><p><span style=\" font-style:italic;\">Kürşat Ercan</span></p><p><span style=\" font-style:italic;\">Burak Altuntaş</span></p><p><span style=\" font-weight:600; text-decoration: underline;\">IBAN For Donate: TR28 0011 1000 0000 **** **** **</span></p><p><span style=\" font-weight:600; text-decoration: underline;\">Connect: PathronusProject@gmail.com</span><br/></p></body></html>"))
        self.Pathronus_TabWidget.setTabText(self.Pathronus_TabWidget.indexOf(self.Pathronus_Tab), _translate("Pathronus", "Pathronus"))
        self.label_3.setText(_translate("Pathronus", "Please Enter New User Informations"))
        self.label_4.setText(_translate("Pathronus", "User Name:"))
        self.label_5.setText(_translate("Pathronus", "Password:"))
        self.label_6.setText(_translate("Pathronus", "Password Again:"))
        self.AddUser_Button.setText(_translate("Pathronus", "Add User"))
        self.Pathronus_TabWidget.setTabText(self.Pathronus_TabWidget.indexOf(self.AddUser_Tab), _translate("Pathronus", "Add User"))
        self.label_7.setText(_translate("Pathronus", "Select User For Remove"))
        self.RemoveUser_Refresh_Button.setText(_translate("Pathronus", "Refresh"))
        self.RemoveUser_Remove_Button.setText(_translate("Pathronus", "Remove"))
        self.Pathronus_TabWidget.setTabText(self.Pathronus_TabWidget.indexOf(self.RemoveUser_Tab), _translate("Pathronus", "Remove User"))
        self.label_8.setText(_translate("Pathronus", "Please Enter Your New Password"))
        self.label_9.setText(_translate("Pathronus", "New Password:"))
        self.label_10.setText(_translate("Pathronus", "Password Again:"))
        self.ChangePassword_Enter_Button.setText(_translate("Pathronus", "Enter"))
        self.Pathronus_TabWidget.setTabText(self.Pathronus_TabWidget.indexOf(self.ChangePassword_Tab), _translate("Pathronus", "Change Password"))
        self.AddPicture_Button.setText(_translate("Pathronus", "Add Picture"))
        self.EnableProgram_Button.setText(_translate("Pathronus", "Enable The Program"))


    def addUser(self):
        newUserUsername = self.username.text()
        newUserPassword = self.password.text()
        newUserPasswordConfirm = self.passwordConfirm.text()

        if db.totalUserInTable() <= 4:
            if newUserUsername != None and newUserPassword != None:
                if newUserPassword == newUserPasswordConfirm:

                    db.createUser(db.genereteID(), newUserUsername, "", newUserPassword, False, "")
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Cheese :)")
                    msg.setWindowTitle("Cheese :)")
                    msg.exec_()
                    if msg.exec_() == 1024:
                        faceDataSet.saveFaceFrame(db.totalUserInTable())
                        faceTraining.training()

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
                msg.setText("Herhangi Bir Alan Boş Bırakılamaz")
                msg.setWindowTitle("Kritik Hata")
                msg.exec_()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Kullanıcı Sayısı Aşıldı")
            msg.setInformativeText('Kullanıcı Eklemek için Kullanıcı Silmeniz Gerekli')
            msg.setWindowTitle("Sınır Aşıldı")
            msg.exec_()

    def removeUser(self):
        if self.RemoveUser_Table.currentRow() == -1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Kullanıcı Seçimi Yapmalısınız")
            msg.setInformativeText('Lütfen Kullanıcı Seçin')
            msg.setWindowTitle("Kullanıcı Seçimi Yapınız")
            msg.exec_()

        if self.RemoveUser_Table.currentRow() == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Yetkili Kullanıcı Silinemez")
            msg.setWindowTitle("Hata")
            msg.exec_()
        else:
            row = self.RemoveUser_Table.currentRow()
            db.deleteUser(str(row + 1))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Kullanıcı Silindi")
            msg.setWindowTitle("Başarılı İşlem")
            msg.exec_()

    def refreshTable(self):
        totalRow = 1
        totalUserInTable = db.totalUserInTable() + 1
        while totalRow != totalUserInTable:
            self.RemoveUser_Table.setItem(totalRow - 1, 0, QTableWidgetItem(db.fetch(str(totalRow), "uName")))
            totalRow += 1

    def changePassword(self):
        newPassword = self.newPassword.text()

        newPasswordConfirm = self.newPasswordConfirm.text()

        if newPassword == newPasswordConfirm:
            if newPassword == db.fetch("1", "uPassword"):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Parola Eski Parola İle Aynı")
                msg.setInformativeText('Lütfen Yeni Bir Parola Giriniz')
                msg.setWindowTitle("Aynı Parola")
                msg.exec_()
            else:
                db.updateInfo("1", "uPassword", newPassword)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Parolanız Değiştirildi")
                msg.setWindowTitle("Başarılı İşlem")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Parolalar Eşleşmedi")
            msg.setInformativeText('Lütfen Uyuşan Parolalar giriniz')
            msg.setWindowTitle("Parolalar Eşleşmedi")
            msg.exec_()

    def programEnable(self):
        faceTraining.training()
        faceRecognition.recognition()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pathronus = QtWidgets.QMainWindow()
    ui = Ui_Pathronus()
    ui.PathronusUi(Pathronus)
    Pathronus.show()
    sys.exit(app.exec_())
