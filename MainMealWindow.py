#  Written By: Anthony Thomas
#  Tested by: Everyone
#  Debugged by: Anthony

# Anthony Thomas

# Generates the UI that shows the list of meals added, a pie graph to show calories consumed for the day and remaining
# calories before exceeding the user's target calories, and a button to add a new meal.

# All changes made by agthomas95 (Anthony Thomas) unless specified:
# 5/2/21:       Added function for "add a meal" button to pop up a new window


# 5/5/21:       Replaced the placeholder list text with function addMealsToList() that will take all meal information from
#               the database and show the meal's name, calories, and time under its corresponding date. Function will also
#               add the calories of each meal from today's date to be displayed in the pie chart.

#               Updated the pie chart to show the updated calories consumed and how much left before exceeding the user's
#               daily target calories, followed by the previous information.

#               Back button now switches to the Lyfe main menu UI.

#               Moved the Lyfe main window import to the function that'll switch to the Lyfe main menu UI to avoid an ImportError.


# 5/13/21:      Added a button to change the user's target calories and a text box to enter it. Entering a non-integer
#               will prompt an error until a valid integer is entered.

#               Added functions to check that the text box and error is not shown until prompted, and to change the
#               calorie goal stored in the database that'll be called in this class to change the calorie text shown
#               around the pie graph.

# 5/18/21:      Fixed pie chart only showing half of each color when any amount of meals are added

from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtCore import Qt
from datetime import date

from MealControllerClass import MealControllerClass
from MealUI import Ui_MealWindow
from MealClass import *
import sys

class Ui_MainMealWindow(object):
    def MealWindowUI(self, MainMealWindow):
        MainMealWindow.setObjectName("MainMealWindow")
        MainMealWindow.resize(800, 675)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainMealWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainMealWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 120, 271, 331))
        self.listWidget.setObjectName("listWidget")
        self.addMealButton = QtWidgets.QPushButton(self.centralwidget)
        self.addMealButton.setGeometry(QtCore.QRect(640, 10, 141, 51))
        self.addMealButton.setAutoFillBackground(False)
        self.addMealButton.setObjectName("addMealButton")
        self.addMealButton.clicked.connect(lambda: self.toAddMeal(MainMealWindow))
        self.MainMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.MainMenuButton.setGeometry(QtCore.QRect(90, 510, 131, 51))
        self.MainMenuButton.setObjectName("MainMenuButton")
        self.MainMenuButton.clicked.connect(lambda: self.toLyfeMainWindow(MainMealWindow))
        self.ChangeCalTargetButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeCalTargetButton.setGeometry(QtCore.QRect(400, 10, 180, 31))
        self.ChangeCalTargetButton.setObjectName("ChangeTargetCalButton")
        self.CalTargetTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.CalTargetTextBox.setGeometry(QtCore.QRect(440, 50, 100, 21))
        self.CalTargetTextBox.setObjectName("CalTargetTextBox")
        self.CalTargetTextBox.setPlaceholderText("Daily calories")
        self.CalTargetTextBox.setVisible(False)
        self.CalTargetTextBox.returnPressed.connect(lambda: self.checkForCalTargetInt(self.CalTargetTextBox.text(), MainMealWindow))
        self.ChangeCalTargetButton.clicked.connect(lambda: self.calTargetVisible())
        self.CalTargetError = QtWidgets.QLabel(self.centralwidget)
        self.CalTargetError.setGeometry(QtCore.QRect(435, 75, 140, 21))
        self.CalTargetError.setObjectName("CalTargetError")
        self.CalTargetError.setVisible(False)
        self.CurrentDateDisplay = QtWidgets.QLabel(self.centralwidget)
        self.CurrentDateDisplay.setGeometry(QtCore.QRect(20, 10, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.CurrentDateDisplay.setFont(font)
        self.CurrentDateDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentDateDisplay.setObjectName("CurrentDateDisplay")
        MainMealWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainMealWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainMealWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMealWindow)
        self.statusbar.setObjectName("statusbar")
        MainMealWindow.setStatusBar(self.statusbar)

        try:  # skips adding meals to a list if database doesn't exist yet -agthomas95
            self.addMealsToList()
        except:
            CheckForDatabase()

        # pie chart creation
        self.pieChartWidget = QtWidgets.QWidget(self.centralwidget)
        self.pieChartWidget.setGeometry(300, 130, 400, 400)

        self.calorieSeries = QPieSeries()   # class for creating pie chart
        self.calorieSeries.append("Calories consumed", MealControllerClass.CalConsumedCount)
        self.calorieSeries.append("Calories left", int(Xml.parse("databases/meals.xml").getroot().find("CalorieGoal/Goal").text)
                                  - MealControllerClass.CalConsumedCount)

        self.calorieSlice = self.calorieSeries.slices()[0]  # slice for calories consumed
        self.calorieSlice.setPen(QPen(Qt.darkGray, 1))
        self.calorieSlice.setBrush(Qt.yellow)
        self.calorieSlice = self.calorieSeries.slices()[1]  # slice for calories left
        self.calorieSlice.setPen(QPen(Qt.darkGray, 1))
        self.calorieSlice.setBrush(Qt.blue)

        self.calorieChart = QChart()
        self.calorieChart.addSeries(self.calorieSeries)
        self.calorieChart.legend().hide()
        self.calorieChart.setBackgroundVisible(False)

        self.chartView = QChartView(self.calorieChart)
        self.vbox = QVBoxLayout()                       # above 3 classes used to show pie chart in UI
        self.vbox.addWidget(self.chartView)
        self.pieChartWidget.setLayout(self.vbox)

        self.caloriesText = QtWidgets.QLabel(self.centralwidget)
        self.caloriesText.setGeometry(360, 150, 400, 40)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.caloriesText.setFont(font)
        self.caloriesText.setObjectName("caloriesConsumedText")

        self.dailyGoalText = QtWidgets.QLabel(self.centralwidget)
        self.dailyGoalText.setGeometry(630, 240, 150, 40)
        self.dailyGoalText.setFont(font)
        self.dailyGoalText.setObjectName("dailyGoalText")

        self.retranslateUi(MainMealWindow)
        QtCore.QMetaObject.connectSlotsByName(MainMealWindow)

    # used to display the meals from the database as a list in the meal UI
    def addMealsToList(self):
        MealControllerClass.CalConsumedCount = 0
        _translate = QtCore.QCoreApplication.translate
        LoadMeals()
        # checks if a date is already added in the list and adds meals of the same date under it
        for meal in MealList:
            if self.listWidget.count() == 0 or len(self.listWidget.findItems(meal.Date, QtCore.Qt.MatchExactly)) == 0:
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignLeft)
                font = QtGui.QFont()
                font.setPointSize(14)
                item.setFont(font)
                brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
                brush.setStyle(QtCore.Qt.Dense5Pattern)
                item.setBackground(brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
                brush.setStyle(QtCore.Qt.NoBrush)
                item.setForeground(brush)
                self.listWidget.addItem(item)
                item.setText(_translate("MainMealWindow", meal.Date))

            if len(self.listWidget.findItems(meal.Date, QtCore.Qt.MatchExactly)) > 0:
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignLeft)
                font = QtGui.QFont()
                font.setPointSize(12)
                item.setFont(font)
                self.listWidget.addItem(item)
                item.setText(_translate("MainMealWindow", "{}{}{}".format(meal.Name.ljust(25), (meal.Calories + " Cal.").ljust(10), meal.Time)))
                if meal.Date == datetime.today().strftime("%m/%d/%Y"):
                    MealControllerClass.CalConsumedCount += int(meal.Calories)

        self.retranslateUi(MainMealWindow)

    def calTargetVisible(self):
        if self.CalTargetTextBox.isVisible():
            self.CalTargetTextBox.setVisible(False)
            self.CalTargetError.setVisible(False)
        else:
            self.CalTargetTextBox.setVisible(True)

    def checkForCalTargetInt(self, value, MainMealWindow):
        try:
            intTest = int(value)
            ChangeCalorieGoal(value)
            self.CalTargetTextBox.setVisible(False)
            self.CalTargetError.setVisible(False)
            self.retranslateUi(MainMealWindow)
        except:
            self.CalTargetError.setVisible(True)

    # goes to the UI for adding a meal
    def toAddMeal(self, MainMealWindow):
        self.addMealWindow = QtWidgets.QMainWindow()
        self.mealUi = Ui_MealWindow()
        self.mealUi.MealWindowSetup(self.addMealWindow)
        self.addMealWindow.show()
        MainMealWindow.close()

    # goes back to the main menu
    def toLyfeMainWindow(self, MainMealWindow):
        from LyfeMainWindow import Ui_MainWindow    # moved import to the function call to prevent an import error -agthomas95
        self.toMainWindow = QtWidgets.QMainWindow()
        self.mainMenu = Ui_MainWindow()
        self.mainMenu.setupUi(self.toMainWindow)
        self.toMainWindow.show()
        MainMealWindow.close()

    # displays today's date, button info, and user calorie information
    def retranslateUi(self, MainMealWindow):
        _translate = QtCore.QCoreApplication.translate
        MainMealWindow.setWindowTitle(_translate("MainMealWindow", "Meals"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.addMealButton.setText(_translate("MainMealWindow", "Add a meal"))
        self.MainMenuButton.setText(_translate("MainMealWindow", "Back"))
        self.ChangeCalTargetButton.setText(_translate("MainMealWindow", "Change daily calories"))
        self.CalTargetError.setText(_translate("MainMealWindow", "<html><head/><body><p style=\"color:red\"><span style=\" font-size:10pt;\">Enter a valid integer</span></p></body></html>"))
        currentDate = date.today()
        self.CurrentDateDisplay.setText(_translate("MainMealWindow", currentDate.strftime("%A, %B %d")))
        self.caloriesText.setText(_translate("MainMealWindow", "Calories consumed: " +
                                             str(MealControllerClass.CalConsumedCount) +
                                             " calories\nCalories left: " +
                                             str(int(Xml.parse("databases/meals.xml").getroot().find("CalorieGoal/Goal").text) -
                                                 MealControllerClass.CalConsumedCount) + " calories"))
        self.dailyGoalText.setText(_translate("MainMealWindow", "Daily goal:\n" +
                                              Xml.parse("databases/meals.xml").getroot().find("CalorieGoal/Goal").text +
                                              " calories"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainMealWindow = QtWidgets.QMainWindow()
    ui = Ui_MainMealWindow()
    ui.MealWindowUI(MainMealWindow)
    MainMealWindow.show()
    sys.exit(app.exec_())
