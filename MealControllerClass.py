# Meal Controller Class
class MealControllerClass:
    from PyQt5.QtWidgets import *
    import sys
    from bs4 import BeautifulSoup

    MealTempDate = ""  # Date of meal to be put into file
    MealTempTime = ""  # Time of meal //
    MealTempName = ""  # What the user ate to be put into file
    MealTempCal = ""  # Calories of meal to be put into file
    MealTempFat = ""  # Fat of meal //
    MealTempSug = ""  # Sugars //
    MealTempChol = ""  # Cholesterol //
    MealTempSod = ""  # Sodium //
    MealTempProt = ""  # Protein //
    MealNotes = ""  # Any notes that the user would like to make about the  						     meal
    CalConsumedCount = ""  # The total sum of the days calories, resets at midnight
    CalLeft = ""  # Calories Left for the day

    # When Add a meal is pressed

    def add_the_meal(MealTempDate, MealTempTime, MealTempName, MealTempCal, MealTempFat,
                     MealTempSug, MealTempChol, MealTempSod, MealTempProt, MealNotes):
        screen = MealInfo()  # Page where user can add a meal
        screen.show()

        MealTempDate = MealDateLbl.text()   # These lines take the users input into the variable
        MealTempTime = MealTimeLbl.text()
        MealTempName = MealNameLbl.text()
        MealTempCal = MealCalLbl.text()
        MealTempFat = MealFatLbl.text()
        MealTempSug = MealSugLbl.text()
        MealTempChol = MealCholLbl.text()
        MealTempSod = MealSodLbl.text()
        MealTempProt = MealProtLbl.text()
        MealNotes = MealNotesLbl.text()
