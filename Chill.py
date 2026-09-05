from Mood import Mood

class Chill(Mood):
    def __init__(self, strength=2 , chill_modifier=0.5):
        if not (0 < chill_modifier < 1):
            raise ValueError("chill_modifier Must be a value between 0 and 1 of float type")
        self.chill_modifier = chill_modifier
        super().__init__(strength)

    def get_patience_factor(self, waiting_time):
        Factor = round(1.05 ** (waiting_time/5) * self.strength * self.chill_modifier , 2)
        return Factor

