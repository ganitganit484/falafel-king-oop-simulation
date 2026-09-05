from abc import ABC, abstractmethod
class Mood(ABC):
    def __init__(self,strength):
        if strength<=0:
            raise ValueError("Strength must be greater than 0")
        self.strength = strength

    @abstractmethod
    def get_patience_factor(self, waiting_time):
        if waiting_time < 0:
            raise ValueError("waiting_time must be a value greater than or equal to 0")
        pass

    def __repr__(self):
       return f"{self.__class__.__name__}"