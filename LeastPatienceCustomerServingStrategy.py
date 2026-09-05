from collections import OrderedDict
from ServingStrategy import ServingStrategy
class LeastPatienceCustomerServingStrategy(ServingStrategy):
    def __init__(self):
        super().__init__()

    def select_next_order(self, orders):
        orders = OrderedDict(orders)
        least_patience_key = min(orders , key = lambda k: (orders[k][0].get_patience()))
        orders.pop(least_patience_key)
        return least_patience_key
