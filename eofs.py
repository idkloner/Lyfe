#  Written By: 
#  Tested by:Everyone
#  Debugged by:



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EOFS.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#5-12-21 Added .connect to each object name -erika
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import *
from LyfeMainWindow import *
from EofsController import *


class Ui_EofsWindow(object):

    currentMood = ""
    currentReason = ""

    def setupUi(self, EofsForm):
        EofsForm.setObjectName("EofsForm")
        EofsForm.resize(574, 476)
        self.HappyButton = QtWidgets.QPushButton(EofsForm)
        self.HappyButton.setGeometry(QtCore.QRect(30, 80, 75, 23))
        self.HappyButton.clicked.connect(lambda: self.setMood("Happy"))
        self.HappyButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);    \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.HappyButton.setObjectName("HappyButton")
        self.SadButton = QtWidgets.QPushButton(EofsForm)
        self.SadButton.setGeometry(QtCore.QRect(100, 80, 75, 23))
        self.SadButton.clicked.connect(lambda: self.setMood("Sad"))
        self.SadButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.SadButton.setObjectName("SadButton")
        self.MadButton = QtWidgets.QPushButton(EofsForm)
        self.MadButton.setGeometry(QtCore.QRect(170, 80, 75, 23))
        self.MadButton.clicked.connect(lambda: self.setMood("Mad"))
        self.MadButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.MadButton.setObjectName("MadButton")
        self.DepressedButton = QtWidgets.QPushButton(EofsForm)
        self.DepressedButton.setGeometry(QtCore.QRect(240, 80, 75, 23))
        self.DepressedButton.clicked.connect(lambda: self.setMood("Depressed"))
        self.DepressedButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.DepressedButton.setObjectName("DepressedButton")
        self.TiredButton = QtWidgets.QPushButton(EofsForm)
        self.TiredButton.setGeometry(QtCore.QRect(310, 80, 75, 23))
        self.TiredButton.clicked.connect(lambda: self.setMood("Tired"))
        self.TiredButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.TiredButton.setObjectName("TiredButton")
        self.ChallengingButton = QtWidgets.QPushButton(EofsForm)
        self.ChallengingButton.setGeometry(QtCore.QRect(380, 80, 75, 23))
        self.ChallengingButton.clicked.connect(lambda: self.setMood("Challenging"))
        self.ChallengingButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.ChallengingButton.setObjectName("ChallengingButton")
        self.OtherButton = QtWidgets.QPushButton(EofsForm)
        self.OtherButton.setGeometry(QtCore.QRect(450, 80, 75, 23))
        self.OtherButton.clicked.connect(lambda: self.setMood("Other"))
        self.OtherButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.OtherButton.setObjectName("OtherButton")
        self.WorkButton = QtWidgets.QPushButton(EofsForm)
        self.WorkButton.setGeometry(QtCore.QRect(30, 180, 75, 23))
        self.WorkButton.clicked.connect(lambda: self.setReason("Work"))
        self.WorkButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.WorkButton.setObjectName("WorkButton")
        self.SchoolButton = QtWidgets.QPushButton(EofsForm)
        self.SchoolButton.setGeometry(QtCore.QRect(100, 180, 75, 23))
        self.SchoolButton.clicked.connect(lambda: self.setReason("School"))
        self.SchoolButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.SchoolButton.setObjectName("SchoolButton")
        self.ParentsButton = QtWidgets.QPushButton(EofsForm)
        self.ParentsButton.setGeometry(QtCore.QRect(170, 180, 75, 23))
        self.ParentsButton.clicked.connect(lambda: self.setReason("Parents"))
        self.ParentsButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.ParentsButton.setObjectName("ParentsButton")
        self.FriendsButton = QtWidgets.QPushButton(EofsForm)
        self.FriendsButton.setGeometry(QtCore.QRect(240, 180, 75, 23))
        self.FriendsButton.clicked.connect(lambda: self.setReason("Friends"))
        self.FriendsButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.FriendsButton.setObjectName("FriendsButton")
        self.ResponsibilitiesButton = QtWidgets.QPushButton(EofsForm)
        self.ResponsibilitiesButton.setGeometry(QtCore.QRect(310, 180, 101, 23))
        self.ResponsibilitiesButton.clicked.connect(lambda: self.setReason("Responsibilities"))
        self.ResponsibilitiesButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.ResponsibilitiesButton.setObjectName("ResponsibilitiesButton")
        self.SoButton = QtWidgets.QPushButton(EofsForm)
        self.SoButton.setGeometry(QtCore.QRect(400, 180, 75, 23))
        self.SoButton.clicked.connect(lambda: self.setReason("S/O"))
        self.SoButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.SoButton.setObjectName("SoButton")
        self.OtherButton2 = QtWidgets.QPushButton(EofsForm)
        self.OtherButton2.setGeometry(QtCore.QRect(470, 180, 75, 23))
        self.OtherButton2.clicked.connect(lambda: self.setReason("Other"))
        self.OtherButton2.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(58, 134, 255);\n"
"    color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(253, 255, 103);\n"
"    color: rgb(65, 65, 65);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(78, 134, 255);\n"
"    \n"
"}")
        self.OtherButton2.setObjectName("OtherButton2")
        self.label2 = QtWidgets.QLabel(EofsForm)
        self.label2.setGeometry(QtCore.QRect(190, 130, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label1 = QtWidgets.QLabel(EofsForm)
        self.label1.setGeometry(QtCore.QRect(160, 40, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(EofsForm)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 250, 511, 131))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label3 = QtWidgets.QLabel(EofsForm)
        self.label3.setGeometry(QtCore.QRect(220, 220, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.BackButton = QtWidgets.QPushButton(EofsForm)
        self.BackButton.setGeometry(QtCore.QRect(30, 420, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.BackButton.setFont(font)
        self.BackButton.clicked.connect(lambda: self.main_page_flip(EofsForm))
        self.BackButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 120, 120);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 0, 0);\n"
"    \n"
"}")
        self.BackButton.setObjectName("BackButton")
        self.DoneButton = QtWidgets.QPushButton(EofsForm)
        self.DoneButton.setGeometry(QtCore.QRect(470, 420, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.DoneButton.setFont(font)
        self.DoneButton.clicked.connect(lambda: self.addSummaryToDatabase(EofsForm))
        self.DoneButton.setStyleSheet("QPushButton{\n"
"    border-radius: 8pt;\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(120, 120, 120);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 0, 0);\n"
"    \n"
"}")
        self.DoneButton.setObjectName("DoneButton")

        self.retranslateUi(EofsForm)
        QtCore.QMetaObject.connectSlotsByName(EofsForm)

    def main_page_flip(self, EofsForm): #added by David
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainUi = Ui_MainWindow()
        self.MainUi.setupUi(self.MainWindow)
        self.MainWindow.show()
        EofsForm.close()

    def setMood(self, Mood):
        self.currentMood = Mood


    def setReason(self, Reason):
        self.currentReason = Reason

    def addSummaryToDatabase(self, EofsForm):
        Notes = self.plainTextEdit.toPlainText()
        Date = datetime.today().strftime("%m/%d/%Y")
        Time = datetime.today().strftime("%H:%M %p")    # changed format since I gave Ben the wrong time format -agthomas95
        EofsControllerClass.input_eofs(Date, Time, self.currentMood, self.currentReason, Notes)
        self.main_page_flip(EofsForm)

    def retranslateUi(self, EofsForm):
        _translate = QtCore.QCoreApplication.translate
        EofsForm.setWindowTitle(_translate("EofsForm", "EofsForm"))
        self.HappyButton.setText(_translate("EofsForm", "Happy"))
        self.SadButton.setText(_translate("EofsForm", "Sad"))
        self.MadButton.setText(_translate("EofsForm", "Mad"))
        self.DepressedButton.setText(_translate("EofsForm", "Depressed"))
        self.TiredButton.setText(_translate("EofsForm", "Tired"))
        self.ChallengingButton.setText(_translate("EofsForm", "Challenging"))
        self.OtherButton.setText(_translate("EofsForm", "Other"))
        self.WorkButton.setText(_translate("EofsForm", "Work"))
        self.SchoolButton.setText(_translate("EofsForm", "School"))
        self.ParentsButton.setText(_translate("EofsForm", "Parents"))
        self.FriendsButton.setText(_translate("EofsForm", "Friends"))
        self.ResponsibilitiesButton.setText(_translate("EofsForm", "Responsibilities"))
        self.SoButton.setText(_translate("EofsForm", "S/O"))
        self.OtherButton2.setText(_translate("EofsForm", "Other"))
        self.label2.setText(_translate("EofsForm", "What might be the cause?"))
        self.label1.setText(_translate("EofsForm", "How was your overall mood today?"))
        self.label3.setText(_translate("EofsForm", "Care to elaborate?"))
        self.BackButton.setText(_translate("EofsForm", "Back"))
        self.DoneButton.setText(_translate("EofsForm", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EofsForm = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(EofsForm)
    EofsForm.show()
    sys.exit(app.exec_())
