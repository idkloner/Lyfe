import xml.etree.ElementTree as ET          #used for reading and writing XML files

def AddMealDatabase(InfoList):              #appends new meal to database using food info give
    try:
        mdb = ET.parse("MealDatabase.xml")  #finds database in file; creates new database if XML name is not found
    except:
        root = ET.Element("Meals")          #element creates the main meal element that all meals will be contained in
        tree = ET.ElementTree(root)
        tree.write("MealDatabase.xml")
        
    mdb = ET.parse("MealDatabase.xml")
    MealsRoot = mdb.getroot()
    MealSubList = ET.Element("li", Name=InfoList[0], Date=InfoList[1], Calories=InfoList[2],                #creates new element within the meals element
                             Fat=InfoList[3], Sugars=InfoList[4], Cholesterol=InfoList[5],                  #called meal, containg separate info for each
                             Sodium=InfoList[6], Protein=InfoList[7], Time=InfoList[8], Notes=InfoList[9])  #meal added to the database
    MealsRoot.append(MealSubList)           #adds the meal into the database
    mdb.write("MealDatabase.xml")           #rewrites the xml file to contain the new meal
