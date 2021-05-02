# Ben Witort

# Library that handles creating and interacting with XML files
import xml.etree.ElementTree as Xml
# Library needed for creating database directory
import os

# Used to hold all meals in database while user is in Meal window
MealList = []

# Loads in all of the meals from the meals database into MealList
def LoadMeals():
    file = Xml.parse("databases/meals.xml")
    meals = file.getroot()

    if(MealList):
        MealList.clear()

    for meal in meals:
        MealList.append(Meal(meal.find("Name").text, meal.find("Date").text, meal.find("Calories").text,
                             meal.find("Fat").text, meal.find("Sugar").text, meal.find("Cholesterol").text,
                             meal.find("Sodium").text, meal.find("Protein").text, meal.find("Time").text,
                             meal.find("Notes").text))

def FindInsertIndex(Date, Time, DatabaseRoot):
    MealMonth = Date[4:7]
    DaySpaceIndex = Date.find(" ", 8)
    MealDay = Date[8:DaySpaceIndex]
    MealYear = Date[DaySpaceIndex + 1:]
    MealTimeColonIndex = Time.find(":")
    MealHour = Time[0:MealTimeColonIndex]
    MealMinute = Time[MealTimeColonIndex + 1:]
    DateInfo = {"Minute": MealMinute, "Hour": MealHour, "Day": MealDay, "Month": MealMonth, "Year": MealYear}

    counter = 0
    MonthDict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
                 "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    for meal in DatabaseRoot:
        CurrentMealDate = meal[0].text
        CurrentMealTime = meal[1].text
        CurrentMealMonth = CurrentMealDate[4:7]
        DayIndex = CurrentMealDate.find(" ", 8)
        CurrentMealDay = CurrentMealDate[8:DayIndex]
        CurrentMealYear = CurrentMealDate[DayIndex + 1:]
        CurrentMealTimeColonIndex = CurrentMealTime.find(":")
        CurrentMealHour = CurrentMealTime[0:CurrentMealTimeColonIndex]
        CurrentMealMinute = CurrentMealTime[CurrentMealTimeColonIndex + 1:]

        if(int(CurrentMealYear) > int(DateInfo["Year"])):
            counter += 1
            continue
        if(MonthDict[CurrentMealMonth] > MonthDict[DateInfo["Month"]]):
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
        break
    return counter


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
        # If the meal database doesn't exist, create it
        try:
            file = Xml.parse("databases/meals.xml")
        except:
            database = Xml.ElementTree(Xml.Element("Meals"))
            os.makedirs("databases")
            with open("databases/meals.xml", "wb") as NewDatabase:
                database.write(NewDatabase)
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
