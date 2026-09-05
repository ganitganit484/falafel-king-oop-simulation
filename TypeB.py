from Angry import Angry
from Furious import Furious
from Personality import Personality
from Explosive import Explosive
from Calm import Calm
from Chill import Chill

class TypeB(Personality):
    def __init__(self):
        super().__init__()

    def adjust_mood(self, mood, waiting_time):
        if waiting_time > 120 and isinstance(mood,Furious):
            mood = Explosive(mood.strength)
        if waiting_time > 90 and isinstance(mood,Angry):
            mood = Furious(mood.strength)
        if waiting_time > 60 and isinstance(mood,Calm):
            mood = Angry(mood.strength)
        if waiting_time > 40 and isinstance(mood,Chill):
            mood = Calm(mood.strength)
        return mood
