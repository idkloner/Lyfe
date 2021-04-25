# Meal Controller Class
# David Toepfer

from MealClass import *


class MealControllerClass:
    CalConsumedCount = 0  # The total sum of the days calories, resets at midnight
    CalLeft = 0  # Calories Left for the day
    TargetCal = 2000  # calorie goal for the day

    # When Add a meal is pressed

    @staticmethod
    def add_the_meal(Name, Date, Cal, Fat, Sug, Chol, Sod, Prot, Time, Notes):
        new_meal = Meal(Name, Date, Cal, Fat, Sug, Chol, Sod, Prot, Time, Notes)

        new_meal.AddMealDatabase()  # adds meal to the data base#.

        new_meal.AddMealList()  # adds meal to list for on page.

        # CalConsumedCount = CalConsumedCount + int(Cal)    	# Calculates the total calories consumed for the day
        # CalLeft = TargetCal - CalConsumedCount              	# Calculates the amount of calories left for the day

