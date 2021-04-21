# Meal Controller Class
from PyQt5.QtWidgets import *
import sys

MealTempDate = ""       # Date of meal to be put into file
MealTempTime = ""       # Time of meal //
MealTempName = ""       # What the user ate to be put into file
MealTempCal = ""        # Calories of meal to be put into file
MealTempFat = ""        # Fat of meal //
MealTempSug = ""        # Sugars //
MealTempChol = ""       # Cholesterol //
MealTempSod = ""        # Sodium //
MealTempProt = ""       # Protein //
MealNotes = ""          # Any notes that the user would like to make about the  						     meal
CalConsumedCount = ""   # The total sum of the days calories, resets at midnight
CalLeft = ""            # Calories Left for the day


@event(AddAMealBtn, Pressed)
def enter_a_meal(MealTempDate, MealTempTime, MealTempName, MealTempCal, MealTempFat,
    MealTempSug, MealTempChol, MealTempSod, MealTempProt, MealNotes):
    screen = MealInfo()
    screen.show()

    MealTempDate
    MealTempTime
    MealTempName
    MealTempCal
    MealTempFat
    MealTempSug
    MealTempChol
    MealTempSod
    MealTempProt
    MealNotes
    MealTempDate
    MealTempTime
    MealTempName
    MealTempCal
    MealTempFat
    MealTempSug
    MealTempChol
    MealTempSod
    MealTempProt
    MealNotes