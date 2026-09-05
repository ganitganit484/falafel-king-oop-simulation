from collections import OrderedDict
from ServingStrategy import ServingStrategy
from Customer import Customer
from Dish import Dish
class ArrivalTimeServingStrategy(ServingStrategy):
    def __init__(self):
        super().__init__()

    def select_next_order(self, orders : dict[int,tuple[Customer,Dish]]):
        orders = OrderedDict(orders)
        first_arrived_key = min(orders, key = lambda k: orders[k][0].arrive_time)
        orders.pop(first_arrived_key)
        return first_arrived_key
