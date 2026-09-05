from abc import ABC, abstractmethod

class OrdersStrategy(ABC):
    def __init__(self):
        pass

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass