# Meal Controller Class
# David Toepfer

from MealClass import *


class MealControllerClass:
    # Temporary variables to hold changing variables
    CalConsumedCount = ""  # The total sum of the days calories, resets at midnight
    CalLeft = ""  # Calories Left for the day

    # When Add a meal is pressed

    def add_the_meal(self, CalConsumedCount, CalLeft):
        new_meal = Meal(MealNameLbl.text(), MealDateLbl.text(), MealCalLbl.text(), MealFatLbl.text(),
                       MealSugLbl.text(), MealCholLbl.text(), MealSodLbl.text(), MealProtLbl.text(), MealTimeLbl.text(),
                       MealNotesLbl.text())

        new_meal.AddMealDatabase()  # temps to file.

        CalConsumedCount = CalConsumedCount + MealCalLbl.text    # Calculates the total calories consumed for the day
        CalLeft = TargetCal - CalConsumedCount              # Calculates the amount of calories left for the day


        screen = MealWindow()  # returns to meals page
        screen.show()
