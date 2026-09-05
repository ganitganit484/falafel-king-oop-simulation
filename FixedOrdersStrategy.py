from OrdersStrategy import OrdersStrategy


class FixedOrdersStrategy(OrdersStrategy):
    def __init__(self, lst_orders):
        super().__init__()
        self.lst_orders = lst_orders
        self.index = 0 #We defined a static variable that initializes the first index to be 0. In each iteration we will add 1 to it and return the lists that are in the current index in the nested list.

    def __iter__(self):
        super().__iter__()
        self.index=0
        return self

    def __next__(self):
        if self.index >= len(self.lst_orders):
            raise StopIteration
        order_to_return = self.lst_orders[self.index]
        self.index += 1
        return order_to_return
