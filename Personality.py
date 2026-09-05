from abc import ABC, abstractmethod
class Personality(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def adjust_mood(self, mood, waiting_time):
        pass

    def __repr__(self):
       return f"{self.__class__.__name__}"