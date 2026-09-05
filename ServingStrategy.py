from abc import ABC, abstractmethod
from exceptions import OrderOutOfBoundsException

class ServingStrategy(ABC):
    def __init__(self):
        pass

    def __iter__(self):
        return self

    @abstractmethod
    def select_next_order(self, orders):
        if not orders:
            raise OrderOutOfBoundsException(orders)
        pass
