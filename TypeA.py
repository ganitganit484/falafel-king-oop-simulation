from Explosive import Explosive
from Personality import Personality
from Furious import Furious
from Angry import Angry
class TypeA(Personality):
    def __init__(self):
        super().__init__()

    def adjust_mood(self, mood, waiting_time):
        if waiting_time > 40:
            return Explosive(mood.strength)
        elif waiting_time > 30 and not isinstance(mood,Explosive):
            return Furious(mood.strength)
        elif waiting_time > 20 and not isinstance(mood,Explosive) and not isinstance(mood,Furious):
            return Angry(mood.strength)
        return mood
