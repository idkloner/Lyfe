# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EOFS.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(574, 476)
        self.HappyButton = QtWidgets.QPushButton(Form)
        self.HappyButton.setGeometry(QtCore.QRect(30, 80, 75, 23))
        self.HappyButton.setObjectName("HappyButton")
        self.SadButton = QtWidgets.QPushButton(Form)
        self.SadButton.setGeometry(QtCore.QRect(100, 80, 75, 23))
        self.SadButton.setObjectName("SadButton")
        self.MadButton = QtWidgets.QPushButton(Form)
        self.MadButton.setGeometry(QtCore.QRect(170, 80, 75, 23))
        self.MadButton.setObjectName("MadButton")
        self.DepressedButton = QtWidgets.QPushButton(Form)
        self.DepressedButton.setGeometry(QtCore.QRect(240, 80, 75, 23))
        self.DepressedButton.setObjectName("DepressedButton")
        self.TiredButton = QtWidgets.QPushButton(Form)
        self.TiredButton.setGeometry(QtCore.QRect(310, 80, 75, 23))
        self.TiredButton.setObjectName("TiredButton")
        self.ChallengingButton = QtWidgets.QPushButton(Form)
        self.ChallengingButton.setGeometry(QtCore.QRect(380, 80, 75, 23))
        self.ChallengingButton.setObjectName("ChallengingButton")
        self.OtherButton = QtWidgets.QPushButton(Form)
        self.OtherButton.setGeometry(QtCore.QRect(450, 80, 75, 23))
        self.OtherButton.setObjectName("OtherButton")
        self.WorkButton = QtWidgets.QPushButton(Form)
        self.WorkButton.setGeometry(QtCore.QRect(30, 180, 75, 23))
        self.WorkButton.setObjectName("WorkButton")
        self.SchoolButton = QtWidgets.QPushButton(Form)
        self.SchoolButton.setGeometry(QtCore.QRect(100, 180, 75, 23))
        self.SchoolButton.setObjectName("SchoolButton")
        self.ParentsButton = QtWidgets.QPushButton(Form)
        self.ParentsButton.setGeometry(QtCore.QRect(170, 180, 75, 23))
        self.ParentsButton.setObjectName("ParentsButton")
        self.FriendsButton = QtWidgets.QPushButton(Form)
        self.FriendsButton.setGeometry(QtCore.QRect(240, 180, 75, 23))
        self.FriendsButton.setObjectName("FriendsButton")
        self.ResponsibilitiesButton = QtWidgets.QPushButton(Form)
        self.ResponsibilitiesButton.setGeometry(QtCore.QRect(310, 180, 101, 23))
        self.ResponsibilitiesButton.setObjectName("ResponsibilitiesButton")
        self.SoButton = QtWidgets.QPushButton(Form)
        self.SoButton.setGeometry(QtCore.QRect(400, 180, 75, 23))
        self.SoButton.setObjectName("SoButton")
        self.OtherButton2 = QtWidgets.QPushButton(Form)
        self.OtherButton2.setGeometry(QtCore.QRect(470, 180, 75, 23))
        self.OtherButton2.setObjectName("OtherButton2")
        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(190, 130, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(160, 40, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 250, 511, 131))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label3 = QtWidgets.QLabel(Form)
        self.label3.setGeometry(QtCore.QRect(220, 220, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.BackButton = QtWidgets.QPushButton(Form)
        self.BackButton.setGeometry(QtCore.QRect(30, 420, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.DoneButton = QtWidgets.QPushButton(Form)
        self.DoneButton.setGeometry(QtCore.QRect(470, 420, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.DoneButton.setFont(font)
        self.DoneButton.setObjectName("DoneButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.HappyButton.setText(_translate("Form", "Happy"))
        self.SadButton.setText(_translate("Form", "Sad"))
        self.MadButton.setText(_translate("Form", "Mad"))
        self.DepressedButton.setText(_translate("Form", "Depressed"))
        self.TiredButton.setText(_translate("Form", "Tired"))
        self.ChallengingButton.setText(_translate("Form", "Challenging"))
        self.OtherButton.setText(_translate("Form", "Other"))
        self.WorkButton.setText(_translate("Form", "Work"))
        self.SchoolButton.setText(_translate("Form", "School"))
        self.ParentsButton.setText(_translate("Form", "Parents"))
        self.FriendsButton.setText(_translate("Form", "Friends"))
        self.ResponsibilitiesButton.setText(_translate("Form", "Responsibilities"))
        self.SoButton.setText(_translate("Form", "S/O"))
        self.OtherButton2.setText(_translate("Form", "Other"))
        self.label2.setText(_translate("Form", "What might be the cause?"))
        self.label1.setText(_translate("Form", "How was your overall mood today?"))
        self.label3.setText(_translate("Form", "Care to elaborate?"))
        self.BackButton.setText(_translate("Form", "Back"))
        self.DoneButton.setText(_translate("Form", "Done"))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
