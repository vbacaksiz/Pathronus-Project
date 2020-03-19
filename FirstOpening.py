from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from Pathronus import *
import faceDataSet
import faceTraining
from LogIn import *
import db


#Kullanıcı programı ilk açtığında karşılaşacağı ekran. Bu ekran en az bir kullanıcı varsa bir daha gösterilmez
class Ui_FirstOpeninWindow(object):

    def FirstOpeningUi(self, FirstOpeningWindow):

        FirstOpeningWindow.setObjectName("FirstOpeningWindow")
        FirstOpeningWindow.resize(417, 330)
        self.centralwidget = QtWidgets.QWidget(FirstOpeningWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(70, 20, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 100, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 140, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 180, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 220, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        #E-mail yazılacak Line Edit
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(160, 100, 113, 25))
        self.username.setObjectName("FirstOpening_lineEdit_1")

        #User Name yazılacak Line Edit
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(160, 140, 113, 25))
        self.email.setObjectName("FirstOpening_lineEdit_2")

        #Password yazılacak Line Edit
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setGeometry(QtCore.QRect(160, 180, 113, 25))
        self.password.setObjectName("FirstOpening_lineEdit_3")

        #Password Again yazılacak Line Edit
        self.passwordConfirm = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordConfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordConfirm.setGeometry(QtCore.QRect(160, 220, 113, 25))
        self.passwordConfirm.setObjectName("FirstOpening_lineEdit_4")

        #İlk kullanıcının bilgileri girildikten sonra bu bilgilere sahip kullanıcının yaratılması için kullanılan buton
        self.FirstOpening_AddUser_Button = QtWidgets.QPushButton(self.centralwidget)
        self.FirstOpening_AddUser_Button.setGeometry(QtCore.QRect(170, 260, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setItalic(True)
        self.FirstOpening_AddUser_Button.setFont(font)
        self.FirstOpening_AddUser_Button.setObjectName("FirstOpening_AddUser_Button")
        self.FirstOpening_AddUser_Button.clicked.connect(self.firstUserAddOpenTheProgram)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 300, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        FirstOpeninWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FirstOpeninWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstOpeninWindow)

    #Kullanıcı ekleme butonuna basıldıktan sonra gerçekleşecek işlemler için fonksiyon
    def firstUserAddOpenTheProgram(self):
        userUsername = self.email.text()

        userEmail = self.username.text()

        userPassword = self.password.text()

        userPasswordConfirm = self.passwordConfirm.text()
        if userEmail != None and userUsername != None and userPassword != None:
            if userPassword == userPasswordConfirm:
                db.createTable()
                db.createUser(db.genereteID(), userUsername, userEmail, userPassword, True, "")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Cheese :)")
                msg.setWindowTitle("Cheese :)")
                msg.exec_()
                if msg.exec_() == 1024:
                    faceDataSet.saveFaceFrame(1)
                    faceTraining.training()

                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_Pathronus()
                self.ui.PathronusUi(self.window)
                self.window.show()
                FirstOpeninWindow.close()

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
            msg.setText("Hiç Bir Alan Boş Bırakılamaz")
            msg.setWindowTitle("Kritik Hata")
            msg.exec_()




    def retranslateUi(self, FirstOpeningWindow):

        _translate = QtCore.QCoreApplication.translate
        FirstOpeningWindow.setWindowTitle(_translate("FirstOpeningWindow", "Pathronus"))
        self.label_1.setText(_translate("FirstOpeningWindow", "Welcome To Pathronus Project"))
        self.label_2.setText(_translate("FirstOpeningWindow", "This Is The First User Registration Page"))
        self.label_3.setText(_translate("FirstOpeningWindow", "E-Mail:"))
        self.label_4.setText(_translate("FirstOpeningWindow", "User Name:"))
        self.label_5.setText(_translate("FirstOpeningWindow", "Password:"))
        self.label_6.setText(_translate("FirstOpeningWindow", "Password Again:"))
        self.FirstOpening_AddUser_Button.setText(_translate("FirstOpeningWindow", "Add User"))
        self.label_7.setText(_translate("FirstOpeningWindow", "A University Project Created By Pathronus"))


if __name__ == "__main__":
    import sys
    #Eğer veritabanında zaten bir kullanıcı var ise login arayüzünün açılmasını sağlar.
    if db.isUserInTable() == True:
        app = QtWidgets.QApplication(sys.argv)
        LogIn = QtWidgets.QMainWindow()
        ui = Ui_LogIn()
        ui.LogInUi(LogIn)
        LogIn.show()
        sys.exit(app.exec_())
    else:
        app = QtWidgets.QApplication(sys.argv)
        FirstOpeninWindow = QtWidgets.QMainWindow()
        ui = Ui_FirstOpeninWindow()
        ui.FirstOpeningUi(FirstOpeninWindow)
        FirstOpeninWindow.show()
        sys.exit(app.exec_())
