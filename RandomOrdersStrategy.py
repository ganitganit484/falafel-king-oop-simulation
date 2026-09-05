import random
from OrdersStrategy import OrdersStrategy
from Customer import Customer
from Mood import Mood
from Personality import Personality
from Dish import Dish

class RandomOrdersStrategy(OrdersStrategy):
    def __init__(self, max_dishes, max_ingredients, ingredients, n_orders=-1):
        super().__init__()
        self.max_dishes = max_dishes
        self.max_ingredients = max_ingredients
        self.ingredients = ingredients
        self.n_orders = n_orders
        self.current = 0 #We will initialize the field with 0 because initially no orders were created

    def __next__(self):
        if 0 < self.n_orders <= self.current:
            raise StopIteration
        number_of_dishes = random.choice(range(0,self.max_dishes+1))
        orders = []
        for _ in range(number_of_dishes+1):
            number_of_ing = random.choice(range(1,self.max_ingredients+1))
            customer = Customer(f"{self.current+1}",random.choice(Mood.__subclasses__())(strength=2),random.choice(Personality.__subclasses__())(),100,None)
            dish = Dish(random.choices(self.ingredients,k= number_of_ing))
            tuples = (customer , dish)
            orders.append(tuples)
            self.current += 1
        return orders
