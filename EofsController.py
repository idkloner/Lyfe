# End of Day Summary Controller
# Carlos Guerra Samaniego

from eofs import *

class EofsControllerClass:
    @staticmethod
    def input_mood(Moods):
        new_mood = setMood(Moods)
        new_mood.addMoodDatabase()

    def input_reason(Reasons):
        new_reason = setReason(Reasons)
        new_reason.addReasonDatabase()
    
