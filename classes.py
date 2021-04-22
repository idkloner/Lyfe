import xml.etree.ElementTree as Xml


class Entry:
    Name = ""
    Date = ""


class Meal(Entry):
    Calories = 0.0
    Fat = 0.0
    Sugar = 0.0
    Cholesterol = 0.0
    Sodium = 0.0
    Protein = 0.0
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

    @staticmethod
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
        mealCalories.text = str(self.Calories)
        mealFat = Xml.SubElement(newMeal, "Fat")
        mealFat.text = str(self.Fat)
        mealSugar = Xml.SubElement(newMeal, "Sugar")
        mealSugar.text = str(self.Sugar)
        mealCholesterol = Xml.SubElement(newMeal, "Cholesterol")
        mealCholesterol.text = str(self.Cholesterol)
        mealSodium = Xml.SubElement(newMeal, "Sodium")
        mealSodium.text = str(self.Sodium)
        mealProtein = Xml.SubElement(newMeal, "Protein")
        mealProtein.text = str(self.Protein)
        mealTime = Xml.SubElement(newMeal, "Time")
        mealTime.text = self.Time
        mealNotes = Xml.SubElement(newMeal, "Notes")
        mealNotes.text = self.Notes
        file.write("databases/meals.xml")

    @staticmethod
    def AddMealList(self):
        MealList.append(self)

