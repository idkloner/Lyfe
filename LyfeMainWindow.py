from PyQt5 import QtCore, QtGui, QtWidgets

from eofs import *

class Ui_MainWindow(object):            #base layout/format: Carlos
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LyfeTitleLbl = QtWidgets.QLabel(self.centralwidget)
        self.LyfeTitleLbl.setGeometry(QtCore.QRect(190, 30, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.LyfeTitleLbl.setFont(font)
        self.LyfeTitleLbl.setObjectName("LyfeTitleLbl")
        self.MealTrackerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.MealTrackerBtn.setGeometry(QtCore.QRect(170, 160, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MealTrackerBtn.setFont(font)
        self.MealTrackerBtn.setObjectName("MealTrackerBtn")
        self.EndOfDayBtn = QtWidgets.QPushButton(self.centralwidget)
        self.MealTrackerBtn.clicked.connect(self.meal_page_flip)		#added by David to create page flip
        self.EndOfDayBtn.setGeometry(QtCore.QRect(170, 300, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EndOfDayBtn.setFont(font)
        self.EndOfDayBtn.setObjectName("EndOfDayBtn")
        #self.TaskTrackerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.EndOfDayBtn.clicked.connect(self.eofs_page_flip)
        #self.TaskTrackerBtn.setGeometry(QtCore.QRect(170, 230, 131, 51))
        #font = QtGui.QFont()
        #font.setPointSize(12)
        #self.TaskTrackerBtn.setFont(font)
        #self.TaskTrackerBtn.setObjectName("TaskTrackerBtn")
        #self.TaskTrackerBtn.clicked.connect(self.task_page_flip)
        self.SettingsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SettingsBtn.setGeometry(QtCore.QRect(170, 370, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SettingsBtn.setFont(font)
        self.SettingsBtn.setObjectName("SettingsBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LyfeTitleLbl.setText(_translate("MainWindow", "Lyfe"))
        self.MealTrackerBtn.setText(_translate("MainWindow", "Meal Tracker"))
        #self.EndOfDayBtn.setText(_translate("MainWindow", "End of Day"))
        #self.TaskTrackerBtn.setText(_translate("MainWindow", "Task Tracker"))
        self.SettingsBtn.setText(_translate("MainWindow", "Settings"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "0"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+F4"))

    def meal_page_flip(self, MainWindow): #made change to open main meal window instead. -agthomas95
        from MainMealWindow import Ui_MainMealWindow
        # Ben Witort helped get page flip to work
        self.mainMealWindow = QtWidgets.QMainWindow()
        self.MealUi = Ui_MainMealWindow()
        self.MealUi.MealWindowUI(self.mainMealWindow)
        self.mainMealWindow.show()
        MainWindow.close()

    def eofs_page_flip(self): #added by David
        self.EofsWindow = QtWidgets.QMainWindow()
        self.EofsUi = Ui_EofsWindow()
        self.EofsUi.setupUi(self.EofsWindow)
        self.EofsWindow.show()
        MainWindow.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
