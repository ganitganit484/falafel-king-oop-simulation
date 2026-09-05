import copy
from exceptions import NoSuchIngredientException, NotCustomerDishException, NoSuchOrderException, OrderOutOfBoundsException

class FalafelStall:
    def __init__(self, strategy, ingredient_prices):
        self.strategy = strategy
        self.__ingredient_prices = ingredient_prices
        self.__orders = {}
        self.__money = 0.00
        self.__order_counter = 0

    def order(self, customer, dish):
        for ing in dish.get_ingredients():
            if ing not in self.__ingredient_prices.keys():
                raise NoSuchIngredientException(ing)
        self.__order_counter += 1
        order_id = self.__order_counter
        self.__orders[order_id] = (customer , dish)
        return order_id

    def get_next_order_id(self):
        if not self.__orders:
            raise OrderOutOfBoundsException(self.get_orders())
        return self.strategy.select_next_order(self.__orders)

    def serve_dish(self, order_id, dish):
        if type(order_id) != int:
            raise TypeError("Order ID must be of type int")
        if order_id not in self.__orders.keys():
            raise NoSuchOrderException(order_id)
        if dish == self.__orders[order_id][1]:
            self.__money += self.calculate_cost(dish)
        else:
            raise NotCustomerDishException(dish,self.__orders[order_id][1])

    def remove_order(self, order_id):
        if not isinstance(order_id,int):
            raise TypeError("Order ID must be of type int")
        if order_id not in self.__orders.keys():
            raise NoSuchOrderException(order_id)
        del self.__orders[order_id]

    def get_order(self, order_id):
        if order_id not in self.__orders.keys():
            raise NoSuchOrderException(order_id)
        orders_copy = copy.deepcopy(self.__orders)
        return orders_copy[order_id]

    def calculate_cost(self, dish):
        total_cost = 0
        for ing in dish.get_ingredients():
            if ing not in self.__ingredient_prices.keys():
                raise NoSuchIngredientException(ing)
            total_cost += self.__ingredient_prices[str(ing)]
        return total_cost

    def get_orders(self):
        return self.__orders

    def get_earning(self):
        return copy.copy(self.__money)



