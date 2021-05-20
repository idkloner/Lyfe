#  Written By: Anthony Thomas
#  Tested by: Everyone
#  Debugged by: Anthony Thomas



# The UI for the user to add a meal into their database containing when the meal was consumed and nutritional info.

# all changed made by agthomas95 unless specified:
# 4/23/21:  Changed object names to be in line with other files
#           Changed window name to "Meal Window"
#           Added function to call add_the_meal function when button is pressed
#           Updated button to call the add_the_meal function

# 4/30/21:  Changed date entry to use the calendar to enter a consistent date rather than inconsistent date entries

# 5/3/21:   Updated date and time entry to be required to enter a consistent date and time before being added to database

# 5/5/21:   Added text under the required fields (time and date if entered incorrectly, name and calories if empty)
#           that's only shown when conditions are met. Changes field border to red to indicate wrong fields.
#           Added a function that checks that the inputs are correct before adding the information into the database.
#           Added a function to make a new window back to the main meal UI to be called in multiple areas.
#           Added a back button to go back to the main meal UI if the user doesn't want to enter a meal.

# Worked on making the text boxes for the notes and nutrition facts. - David T

from PyQt5 import QtCore, QtGui, QtWidgets
from MealControllerClass import *
from datetime import *

class Ui_MealWindow(object):
    def MealWindowSetup(self, MealForm):
        MealForm.setObjectName("Form")
        MealForm.resize(560, 720)
        MealForm.setMinimumSize(QtCore.QSize(400, 0))
        MealForm.setMouseTracking(True)
        self.FormTitle = QtWidgets.QLabel(MealForm)
        self.FormTitle.setGeometry(QtCore.QRect(130, -20, 301, 139))
        self.FormTitle.setMouseTracking(True)
        self.FormTitle.setLineWidth(1)
        self.FormTitle.setObjectName("FormTitle")
        # meal temp values hold user inputs entered through the UI
        self.MealTempDate = QtWidgets.QLineEdit(MealForm)
        self.MealTempDate.setGeometry(QtCore.QRect(180, 120, 261, 20))
        self.MealTempDate.setObjectName("MealDateLbl")
        self.MealTempDate.setPlaceholderText("MM/DD/YYYY")
        self.MealTempTime = QtWidgets.QLineEdit(MealForm)
        self.MealTempTime.setGeometry(QtCore.QRect(180, 160, 261, 20))
        self.MealTempTime.setObjectName("MealTimeLbl")
        self.MealTempTime.setPlaceholderText("HH:MM AM/PM")
        self.MealTempName = QtWidgets.QLineEdit(MealForm)
        self.MealTempName.setGeometry(QtCore.QRect(180, 200, 261, 20))
        self.MealTempName.setObjectName("MealNameLbl")
        self.MealTempCal = QtWidgets.QLineEdit(MealForm)
        self.MealTempCal.setGeometry(QtCore.QRect(180, 240, 261, 20))
        self.MealTempCal.setObjectName("MealCalLbl")
        self.MealTempFat = QtWidgets.QLineEdit(MealForm)
        self.MealTempFat.setGeometry(QtCore.QRect(180, 280, 261, 20))
        self.MealTempFat.setObjectName("MealFatLbl")
        self.MealTempSug = QtWidgets.QLineEdit(MealForm)
        self.MealTempSug.setGeometry(QtCore.QRect(180, 320, 261, 20))
        self.MealTempSug.setObjectName("MealSugLbl")
        self.MealTempChol = QtWidgets.QLineEdit(MealForm)
        self.MealTempChol.setGeometry(QtCore.QRect(180, 360, 261, 20))
        self.MealTempChol.setObjectName("MealCholLbl")
        self.MealTempSod = QtWidgets.QLineEdit(MealForm)
        self.MealTempSod.setGeometry(QtCore.QRect(180, 400, 261, 20))
        self.MealTempSod.setObjectName("MealSodLbl")
        self.MealTempProt = QtWidgets.QLineEdit(MealForm)
        self.MealTempProt.setGeometry(QtCore.QRect(180, 440, 261, 20))
        self.MealTempProt.setObjectName("MealProtLbl")
        self.MealNotes = QtWidgets.QTextEdit(MealForm)
        self.MealNotes.setGeometry(QtCore.QRect(180, 480, 261, 71))
        self.MealNotes.setObjectName("MealNotesLbl")
        # ignore form___, it's the text on the ui to the left of the text boxes
        self.FormDate = QtWidgets.QLabel(MealForm)
        self.FormDate.setGeometry(QtCore.QRect(90, 120, 51, 16))
        self.FormDate.setObjectName("FormDate")
        self.MealDateWrong = QtWidgets.QLabel(MealForm)
        self.MealDateWrong.setGeometry(QtCore.QRect(180, 140, 261, 20))
        self.MealDateWrong.setVisible(False)
        self.MealDateWrong.setObjectName("MealDateWrong")
        self.FormTime = QtWidgets.QLabel(MealForm)
        self.FormTime.setGeometry(QtCore.QRect(90, 160, 51, 16))
        self.FormTime.setObjectName("FormTime")
        self.MealTimeWrong = QtWidgets.QLabel(MealForm)
        self.MealTimeWrong.setGeometry(QtCore.QRect(180, 180, 261, 20))
        self.MealTimeWrong.setVisible(False)
        self.MealDateWrong.setObjectName("MealDateWrong")
        self.FormName = QtWidgets.QLabel(MealForm)
        self.FormName.setGeometry(QtCore.QRect(90, 200, 51, 16))
        self.FormName.setObjectName("FormName")
        self.NoMealName = QtWidgets.QLabel(MealForm)
        self.NoMealName.setGeometry(QtCore.QRect(180, 220, 261, 20))
        self.NoMealName.setVisible(False)
        self.NoMealName.setObjectName("NoMealName")
        self.FormCalories = QtWidgets.QLabel(MealForm)
        self.FormCalories.setGeometry(QtCore.QRect(90, 240, 81, 16))
        self.FormCalories.setObjectName("FormCalories")
        self.NoMealCalories = QtWidgets.QLabel(MealForm)
        self.NoMealCalories.setGeometry(QtCore.QRect(180, 260, 261, 20))
        self.NoMealCalories.setVisible(False)
        self.NoMealCalories.setObjectName("NoMealCalories")
        self.FormFats = QtWidgets.QLabel(MealForm)
        self.FormFats.setGeometry(QtCore.QRect(90, 280, 81, 16))
        self.FormFats.setObjectName("FormFats")
        self.FormSugars = QtWidgets.QLabel(MealForm)
        self.FormSugars.setGeometry(QtCore.QRect(90, 320, 81, 21))
        self.FormSugars.setObjectName("FormSugars")
        self.FormCholesterol = QtWidgets.QLabel(MealForm)
        self.FormCholesterol.setGeometry(QtCore.QRect(90, 360, 81, 21))
        self.FormCholesterol.setObjectName("FormCholesterol")
        self.FormSodium = QtWidgets.QLabel(MealForm)
        self.FormSodium.setGeometry(QtCore.QRect(90, 400, 81, 21))
        self.FormSodium.setObjectName("FormSodium")
        self.FormProtein = QtWidgets.QLabel(MealForm)
        self.FormProtein.setGeometry(QtCore.QRect(90, 440, 81, 21))
        self.FormProtein.setObjectName("FormProtein")
        self.FormNotes = QtWidgets.QLabel(MealForm)
        self.FormNotes.setGeometry(QtCore.QRect(90, 480, 81, 21))
        self.FormNotes.setObjectName("FormNotes")
        self.PushFinishButton = QtWidgets.QPushButton(MealForm)
        self.PushFinishButton.setGeometry(QtCore.QRect(210, 600, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.PushFinishButton.setFont(font)
        self.PushFinishButton.setMouseTracking(False)
        self.PushFinishButton.setCheckable(False)
        self.PushFinishButton.setObjectName("PushFinishButton")
        self.PushFinishButton.clicked.connect(lambda: self.addMealtoDatabase(MealForm))
        self.BackToMMW = QtWidgets.QPushButton(MealForm)
        self.BackToMMW.setGeometry(QtCore.QRect(60, 600, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BackToMMW.setFont(font)
        self.BackToMMW.setMouseTracking(False)
        self.BackToMMW.setCheckable(False)
        self.BackToMMW.setObjectName("BackToMMW")
        self.BackToMMW.clicked.connect(lambda: self.MealUIToMMW(MealForm))

        self.retranslateUi(MealForm)
        QtCore.QMetaObject.connectSlotsByName(MealForm)

    # adds meal information to the database
    #Worked on By David, Ben, Anthony
    def addMealtoDatabase(self, MealForm):
        Name = self.MealTempName.text()
        Date = self.MealTempDate.text()
        if Date == "":  Date = datetime.today().strftime("%m/%d/%Y")
        Cal = self.MealTempCal.text()
        Fat = self.MealTempFat.text()
        Sug = self.MealTempSug.text()
        Chol = self.MealTempChol.text()
        Sod = self.MealTempSod.text()
        Prot = self.MealTempProt.text()
        Time = self.MealTempTime.text()
        Notes = self.MealNotes.toPlainText()

        Date, Time, CorrectInput = self.checkInputs(Name, Date, Cal, Time)
        if CorrectInput:
            MealControllerClass.add_the_meal(Name, Date, Cal, Fat, Sug, Chol, Sod, Prot, Time, Notes)
            self.MealUIToMMW(MealForm)

    # checks that the name, date, calories, and date is inputted by the user and in the correct format
    def checkInputs(self, Name, Date, Cal, Time):
        _translate = QtCore.QCoreApplication.translate
        formatCounter = 0
        if Name == "":
            self.MealTempName.setStyleSheet("border: 1px solid red;")
            self.NoMealName.setVisible(True)
        else:
            self.MealTempName.setStyleSheet("border: 1px solid gray;")
            self.NoMealName.setVisible(False)
            formatCounter += 1

        try:
            Date = datetime.strptime(Date, "%m/%d/%Y").strftime("%m/%d/%Y")
            self.MealTempDate.setStyleSheet("border: 1px solid gray;")
            self.MealDateWrong.setVisible(False)
            formatCounter += 1
        except:
            self.MealTempDate.setStyleSheet("border: 1px solid red;")
            self.MealDateWrong.setVisible(True)

        try:
            calTest = int(Cal)
            self.MealTempCal.setStyleSheet("border: 1px solid gray;")
            self.NoMealCalories.setVisible(False)
            formatCounter += 1
        except:
            if Cal == "":
                self.MealTempCal.setStyleSheet("border: 1px solid red;")
                self.NoMealCalories.setText(_translate("MealForm","<html><head/><body><p style=\"color:red\"><span style=\" font-size:10pt;\">Calories are required</span></p></body></html>"))
            else:
                self.MealTempCal.setStyleSheet("border: 1px solid red;")
                self.NoMealCalories.setText(_translate("MealForm","<html><head/><body><p style=\"color:red\"><span style=\" font-size:10pt;\">Calories must be an integer</span></p></body></html>"))
            self.NoMealCalories.setVisible(True)

        try:
            Time = datetime.strptime(Time, "%H:%M %p").strftime("%H:%M %p")
            self.MealTempTime.setStyleSheet("border: 1px solid gray;")
            self.MealTimeWrong.setVisible(False)
            formatCounter += 1
        except:
            self.MealTempTime.setStyleSheet("border: 1px solid red;")
            self.MealTimeWrong.setVisible(True)

        if formatCounter == 4:
            return Date, Time, True
        return Date, Time, False

    # goes back to the main meal UI
    def MealUIToMMW(self, MealForm):
        from MainMealWindow import Ui_MainMealWindow
        self.toMainMealWindow = QtWidgets.QMainWindow()
        self.MealUi = Ui_MainMealWindow()
        self.MealUi.MealWindowUI(self.toMainMealWindow)
        self.toMainMealWindow.show()
        MealForm.close()

    # displays the text to the left of the respective input boxes and error messages when an input is done wrong
    def retranslateUi(self, MealForm):
        _translate = QtCore.QCoreApplication.translate
        MealForm.setWindowTitle(_translate("MealForm", "Meal Window"))
        self.FormTitle.setText(_translate("MealForm", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">New meal</span></p></body></html>"))
        self.FormDate.setText(_translate("MealForm", "<html><head/><body><p><span style=\" font-size:12pt;\">Date</span></p></body></html>"))
        self.MealDateWrong.setText(_translate("MealForm", "<html><head/><body><p style=\"color:red\"><span style=\" font-size:10pt;\">Wrong date format</span></p></body></html>"))
        self.FormTime.setText(_translate("MealForm", "<html><head/><body><p><span style=\" font-size:12pt;\">Time</span></p></body></html>"))
        self.MealTimeWrong.setText(_translate("MealForm","<html><head/><body><p style=\"color:red\"><span style=\" font-size:10pt;\">Wrong time format</span></p></body></html>"))
        self.FormName.setText(_translate("MealForm", "<html><head/><body><p><span style=\" font-size:12pt;\">Name</span></p></body></html>"))
        self.NoMealName.setText(_translate("MealForm","<html><head/><body><p style=\"color:red\"><span style=\" font-size:10pt;\">Name is required</span></p></body></html>"))
        self.FormCalories.setText(_translate("MealForm", "<html><head/><body><p><span style=\" font-size:12pt;\">Calories</span></p></body></html>"))
        self.FormFats.setText(_translate("MealForm", "<html><head/><body><p><span style=\" font-size:12pt;\">Fats</span></p></body></html>"))
        self.FormSugars.setText(_translate("MealForm", "<html><head/><body><p><span style=\" font-size:12pt;\">Sugars</span></p></body></html>"))
        self.FormCholesterol.setText(_translate("MealForm", "<html><head/><body><p><span style=\" font-size:12pt;\">Cholesterol</span></p></body></html>"))
        self.FormSodium.setText(_translate("MealForm", "<html><head/><body><p><span style=\" font-size:12pt;\">Sodium</span></p></body></html>"))
        self.FormProtein.setText(_translate("MealForm", "<html><head/><body><p><span style=\" font-size:12pt;\">Protein</span></p></body></html>"))
        self.FormNotes.setText(_translate("MealForm", "<html><head/><body><p><span style=\" font-size:12pt;\">Notes</span></p></body></html>"))
        self.PushFinishButton.setText(_translate("MealForm", "Add meal"))
        self.BackToMMW.setText(_translate("MealForm", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MealForm = QtWidgets.QMainWindow()
    ui = Ui_MealWindow()
    ui.MealWindowSetup(MealForm)
    MealForm.show()
    sys.exit(app.exec_())
