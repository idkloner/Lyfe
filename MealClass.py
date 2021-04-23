# Ben Witort

import xml.etree.ElementTree as Xml

# Used to hold all meals in database while user is in Meal window
MealList = []

# Loads in all of the meals from the meals database into MealList
def LoadMeals():
    file = Xml.parse("databases/meals.xml")
    meals = file.getroot()
    for meal in meals:
        MealList.append(Meal(meal.find("Name").text, meal.find("Date").text, meal.find("Calories").text,
                             meal.find("Fat").text, meal.find("Sugar").text, meal.find("Cholesterol").text,
                             meal.find("Sodium").text, meal.find("Protein").text, meal.find("Time").text,
                             meal.find("Notes").text))

  
# Class for meal entries
class Meal():
    Name = ""
    Date = ""
    Calories = ""
    Fat = ""
    Sugar = ""
    Cholesterol = ""
    Sodium = ""
    Protein = ""
    Time = ""
    Notes = ""

    def __init__(self, MealName, MealDate, MealCalories, MealFat, MealSugar, MealCholesterol, MealSodium, MealProtein, MealTime, MealNotes):
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
        file = Xml.parse("databases/meals.xml")
        meals = file.getroot()
        newMeal = Xml.Element("Meal")
        meals.append(newMeal)
        mealName = Xml.SubElement(newMeal, "Name")
        mealName.text = self.Name
        mealDate = Xml.SubElement(newMeal, "Date")
        mealDate.text = self.Date
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
        mealTime = Xml.SubElement(newMeal, "Time")
        mealTime.text = self.Time
        mealNotes = Xml.SubElement(newMeal, "Notes")
        mealNotes.text = self.Notes
        file.write("databases/meals.xml")

    # Puts the meal into MealList
    def AddMealList(self):
        MealList.append(self)
