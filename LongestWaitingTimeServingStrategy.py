from collections import OrderedDict
from ServingStrategy import ServingStrategy
from Customer import Customer
from Dish import Dish

class LongestWaitingTimeServingStrategy(ServingStrategy):
    def __init__(self):
        super().__init__()

    def select_next_order(self, orders : dict[int,tuple[Customer,Dish]]):
        orders = OrderedDict(orders)
        max_key = max(orders, key = lambda k: (orders[k][0].get_waiting_time())) #Since we converted the dictionary to OrderedDict, if the "max" function finds several values whose waiting time is equal, it will automatically return the first one inserted into the dictionary
        orders.pop(max_key)
        return max_key
