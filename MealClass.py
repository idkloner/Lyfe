# Ben Witort, Anthony Thomas

# Library that handles creating and interacting with XML files
import xml.etree.ElementTree as Xml
# Library needed for creating database directory
import os

# 5/13/21:      Moved CheckForDatabase() outside of Meal class so that MainMealWindow can call it without having to put
#               in meal values not yet initialized and check that the database is created.

#               Added ChangeCalorieGoal() that will take the new calorie value from the user input in MainMealWindow
#               and change the value stored in the database. If element hasn't been created yet within the database, it
#               will create one instead.
#               -agthomas95

# Used to hold all meals in database while user is in Meal window
MealList = []

# Loads in all of the meals from the meals database into MealList
def LoadMeals():
    file = Xml.parse("databases/meals.xml")
    meals = file.getroot()

    # If MealList has already been loaded, clear it before loading again
    if(MealList):
        MealList.clear()

    for meal in meals:
        try:
            MealList.append(Meal(meal.find("Name").text, meal.find("Date").text, meal.find("Calories").text,
                                 meal.find("Fat").text, meal.find("Sugar").text, meal.find("Cholesterol").text,
                                 meal.find("Sodium").text, meal.find("Protein").text, meal.find("Time").text,
                                 meal.find("Notes").text))
        except:
            continue

# Finds the proper index for the new meal to be added to database based on Date and Time
def FindInsertIndex(Date, Time, DatabaseRoot):  #changed values to use split to get the numbers between each symbol.
    MealMonth = Date.split("/")[0]              #Before, MealMonth would get a number + / and cause a base 10 error when
    MealDay = Date.split("/")[1]                #comparing the two days together.
    MealYear = Date.split("/")[2]
    MealHour = Time.split(":")[0]
    MealMinute = Time[Time.find(":")+1 : Time.find(" ")]
    MealTimeFrame = Time.split(" ")[1]
    if MealTimeFrame == "PM": MealHour = str(int(MealHour) + 12)
    DateInfo = {"Timeframe": MealTimeFrame, "Minute": MealMinute, "Hour": MealHour, "Day": MealDay, "Month": MealMonth, "Year": MealYear}

    counter = 0
    for meal in DatabaseRoot:
        try:
            CurrentMealDate = meal[0].text
            CurrentMealTime = meal[1].text
            CurrentMealMonth = CurrentMealDate.split("/")[0]
            CurrentMealDay = CurrentMealDate.split("/")[1]
            CurrentMealYear = CurrentMealDate.split("/")[2]
            CurrentMealHour = CurrentMealTime.split(":")[0]
            CurrentMealMinute = CurrentMealTime[CurrentMealTime.find(":")+1 : CurrentMealTime.find(" ")]
            CurrentMealTimeFrame = CurrentMealTime.split(" ")[1]
            if CurrentMealTimeFrame == "PM": CurrentMealHour = str(int(MealHour) + 12)  # Used for comparing time by converting to 24-hour time

            if(int(CurrentMealYear) > int(DateInfo["Year"])):
                counter += 1
                continue
            if(int(CurrentMealMonth) > int(DateInfo["Month"])):
                counter += 1
                continue
            if(int(CurrentMealDay) > int(DateInfo["Day"])):
                counter += 1
                continue
            if(int(CurrentMealDay) == int(DateInfo["Day"])):
                if(int(CurrentMealHour) > int(DateInfo["Hour"])):
                    counter += 1
                    continue
                if(int(CurrentMealMinute) > int(DateInfo["Minute"])):
                    counter += 1
                    continue
        except:
            continue
        break
    return counter

def CheckForDatabase():
    # If the meal database doesn't exist, create it
    try:
        file = Xml.parse("databases/meals.xml")
    except:
        database = Xml.ElementTree(Xml.Element("Meals"))
        if (not os.path.isdir("databases")):
            os.makedirs("databases")
        with open("databases/meals.xml", "wb") as NewDatabase:
            database.write(NewDatabase)
        ChangeCalorieGoal(0)

def ChangeCalorieGoal(calories):
    try:
        file = Xml.parse("databases/meals.xml")
        file.getroot().find("CalorieGoal/Goal").text = str(calories)
        file.write("databases/meals.xml")
    except:
        root = file.getroot()
        calorieElement = Xml.Element("CalorieGoal")
        calorieSubElement = Xml.SubElement(calorieElement, "Goal")
        calorieSubElement.text = str(calories)
        root.insert(0, calorieElement)
        file.write("databases/meals.xml")


# Class for meal entries
class Meal:
    # Initiates Meal object, assigning given data to their respective meal properties
    def __init__(self, MealName, MealDate, MealCalories, MealFat, MealSugar,
                 MealCholesterol, MealSodium, MealProtein, MealTime, MealNotes):
        self.Name = MealName
        self.Date = MealDate
        self.Calories = MealCalories
        self.Fat = MealFat
        self.Sugar = MealSugar
        self.Cholesterol = MealCholesterol
        self.Sodium = MealSodium
        self.Protein = MealProtein
        self.Time = MealTime
        self.Notes = MealNotes

    # Puts the meal into the meal database
    def AddMealDatabase(self):
        CheckForDatabase()
        file = Xml.parse("databases/meals.xml")
        meals = file.getroot()
        newMeal = Xml.Element("Meal")
        index = FindInsertIndex(self.Date, self.Time, meals)
        mealDate = Xml.SubElement(newMeal, "Date")
        mealDate.text = self.Date
        mealTime = Xml.SubElement(newMeal, "Time")
        mealTime.text = self.Time
        meals.insert(index, newMeal)
        mealName = Xml.SubElement(newMeal, "Name")
        mealName.text = self.Name
        mealCalories = Xml.SubElement(newMeal, "Calories")
        mealCalories.text = self.Calories
        mealFat = Xml.SubElement(newMeal, "Fat")
        mealFat.text = self.Fat
        mealSugar = Xml.SubElement(newMeal, "Sugar")
        mealSugar.text = self.Sugar
        mealCholesterol = Xml.SubElement(newMeal, "Cholesterol")
        mealCholesterol.text = self.Cholesterol
        mealSodium = Xml.SubElement(newMeal, "Sodium")
        mealSodium.text = self.Sodium
        mealProtein = Xml.SubElement(newMeal, "Protein")
        mealProtein.text = self.Protein
        mealNotes = Xml.SubElement(newMeal, "Notes")
        mealNotes.text = self.Notes
        file.write("databases/meals.xml")

    # Puts the meal into MealList
    def AddMealList(self):
        MealList.append(self)
