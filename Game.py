import time
import copy
from FalafelStall import FalafelStall
from exceptions import NoSuchIngredientException, NotCustomerDishException, OrderOutOfBoundsException,NoSuchOrderException
from Dish import Dish


class Game:
    def __init__(self, orders_strategy, serving_strategy, ingredient_prices):
        self.__orders_strategy = orders_strategy
        self.__serving_strategy = serving_strategy
        self.__ingredient_prices = ingredient_prices
        self.__game_start = int(time.time())
        self.__lives = 3
        self.__ingredient_dictionary = {0:"green salad", 1:"falafel", 2:"french fries", 3:"coleslaw", 4:"fried eggplants", 5:"tachina", 6:"humus"}

    def get_lives(self):
        return copy.copy(self.__lives)

    def get_game_duration(self, current_time=None):
        if current_time is None:
            current_time = int(time.time())
        return current_time - self.__game_start

    def run(self):
        is_served = False
        falafel_stall = FalafelStall(self.__serving_strategy, self.__ingredient_prices)
        while self.get_lives() > 0: #As long as there is life the game goes on
            try:
                new_orders = next(self.__orders_strategy)
                for customer, dish in new_orders:#Generates orders
                    try:
                        falafel_stall.order(customer, dish)  # Trying to insert the orders into the order dictionary
                    except NoSuchIngredientException as e:
                        print(e)
            except StopIteration:
                if len(falafel_stall.get_orders()) == 0:
                    break
            try:
                next_order_id = falafel_stall.get_next_order_id() #Selects the next order to prepare from the dict
                customer,dish = falafel_stall.get_orders()[next_order_id]
            except OrderOutOfBoundsException as e:
                print(e)
            while is_served is False:
                print(f"Customer:\n{customer}\nDish: {dish}")
                print("Insert ingredients:")
                for key, ing in self.__ingredient_dictionary.items():
                    print(f"{key}: {ing}")
                dish_to_serve = input().split()
                for ing in range(len(dish_to_serve)):
                    try:
                        if int(dish_to_serve[ing]) not in self.__ingredient_dictionary.keys():
                            dish_to_serve[ing] = ""
                        if dish_to_serve[ing] != "":
                            dish_to_serve[ing] = self.__ingredient_dictionary[int(dish_to_serve[ing])]
                    except ValueError as e:
                        print(e)
                try:
                    falafel_stall.serve_dish(next_order_id, Dish(dish_to_serve))
                    falafel_stall.remove_order(next_order_id)
                    is_served = True
                    break

                except NoSuchIngredientException as e:
                    print(f"Failed to create a Dish\n{e}")
                    print("please retry.")

                except NotCustomerDishException as e:
                    print(f"Failed to serve a Dish to customer\n{e}")
                    break
                except NoSuchOrderException as e:
                    print(e)

            is_served = False
            dic =  falafel_stall.get_orders().copy()
            for key ,(customer,dish) in dic.items():
                customer.update()
                if customer.get_patience() <= 0:
                    falafel_stall.remove_order(key)
                    self.__lives -= 1

        print(f"Game Over")
        print(f"score: {falafel_stall.get_earning()}")
