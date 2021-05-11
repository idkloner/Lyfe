# End of Day Summary Controller
# Carlos Guerra Samaniego

from eofsDatabaseClass import *

class EofsControllerClass:
    @staticmethod
    def input_eofs(Date, Time, Mood, Reason, Notes):
        new_Eofs = Eofs(Date, Time, Mood, Reason, Notes)
        new_Eofs.AddEofsDatabase()
        new_Eofs.AddEofsList()
