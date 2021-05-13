# David Toepfer, Used Ben's Meal class as a base reference


# Library that handles creating and interacting with XML files
import xml.etree.ElementTree as Xml
# Library needed for creating database directory
import os

# Used to hold all summaries in database while user is in summary window
Eofslist = []

# Loads in all of the summaries from the database into EofsList
def LoadEofs():
    file = Xml.parse("databases/eofs.xml")
    eofs = file.getroot()

    if(Eofslist):
        Eofslist.clear()

    for summary in eofs:
        Eofslist.append(Eofs(eofs.find("Date").text, eofs.find("Time").text, eofs.find("Name").text, eofs.find("Protein").text,
                             eofs.find("Notes").text))

def FindInsertIndex(Date, Time, DatabaseRoot):
    EofsMonth = Date.split("/")[0]
    EofsDay = Date.split("/")[1]
    EofsYear = Date.split("/")[2]
    EofsHour = Time.split(":")[0]
    EofsMinute = Time[Time.find(":")+1 : Time.find(" ")]
    EofsTimeFrame = Time.split(" ")[1]
    if EofsTimeFrame == "PM": EofsHour = str(int(EofsHour) + 12)
    DateInfo = {"Timeframe": EofsTimeFrame, "Minute": EofsMinute, "Hour": EofsHour, "Day": EofsDay, "Month": EofsMonth, "Year": EofsYear}

    counter = 0
    for eofs in DatabaseRoot:
        CurrentEofsDate = eofs[0].text
        CurrentEofsTime = eofs[1].text
        CurrentEofsMonth = CurrentEofsDate.split("/")[0]
        CurrentEofsDay = CurrentEofsDate.split("/")[1]
        CurrentEofsYear = CurrentEofsDate.split("/")[2]
        CurrentEofsHour = CurrentEofsTime.split(":")[0]
        CurrentEofsMinute = CurrentEofsTime[CurrentEofsTime.find(":")+1 : CurrentEofsTime.find(" ")]
        CurrentEofsTimeFrame = CurrentEofsTime.split(" ")[1]
        if CurrentEofsTimeFrame == "PM": CurrentEofsHour = str(int(EofsHour) + 12)  #Used for comparing time by converting to 24-hour time

        if(int(CurrentEofsYear) > int(DateInfo["Year"])):
            counter += 1
            continue
        if(int(CurrentEofsMonth) > int(DateInfo["Month"])):
            counter += 1
            continue
        if(int(CurrentEofsDay) > int(DateInfo["Day"])):
            counter += 1
            continue
        if(int(CurrentEofsDay) == int(DateInfo["Day"])):
            if(int(CurrentEofsHour) > int(DateInfo["Hour"])):
                counter += 1
                continue
            if(int(CurrentEofsMinute) > int(DateInfo["Minute"])):
                counter += 1
                continue
        break
    return counter


# Class for end of day summary entries
class Eofs:
    # Initiates summary object, assigning given data to their respective properties
    def __init__(self, EofsDate, EofsTime, EofsMood,  EofsReason, EofsNotes):
        self.Date = EofsDate
        self.Time = EofsTime
        self.Mood = EofsMood
        self.Reason = EofsReason
        self.Notes = EofsNotes

    # Puts the summary into the database
    def AddEofsDatabase(self):
        # If the Eofs database doesn't exist, create it
        try:
            file = Xml.parse("databases/eofs.xml")
        except:
            database = Xml.ElementTree(Xml.Element("Eofs"))
            if(not os.path.isdir("databases")):
                os.makedirs("databases")
            with open("databases/eofs.xml", "wb") as NewDatabase:
                database.write(NewDatabase)
            file = Xml.parse("databases/eofs.xml")
        eofs = file.getroot()
        newEofs = Xml.Element("Eofs")
        index = FindInsertIndex(self.Date, self.Time, eofs)
        eofsDate = Xml.SubElement(newEofs, "Date")
        eofsDate.text = self.Date
        eofsTime = Xml.SubElement(newEofs, "Time")
        eofsTime.text = self.Time
        eofs.insert(index, newEofs)
        eofsMood = Xml.SubElement(newEofs, "Mood")
        eofsMood.text = self.Mood
        eofsReason = Xml.SubElement(newEofs, "Reason")
        eofsReason.text = self.Reason
        eofsNotes = Xml.SubElement(newEofs, "Notes")
        eofsNotes.text = self.Notes
        file.write("databases/eofs.xml")

    # Puts the sumary into a list
    def AddEofsList(self):
        Eofslist.append(self)
