import copy

class Dish:
    def __init__(self, ingredients=None):
        if ingredients is None:
            ingredients = []
        self.__ingredients = ingredients

    def add_ingredient(self, ingredient):
        self.__ingredients.append(ingredient)

    def get_ingredients(self):
        return copy.deepcopy(self.__ingredients)

    def __eq__(self, other):
        if isinstance(other , Dish) and len(self.get_ingredients()) == len(other.get_ingredients()) and sorted(self.get_ingredients()) == sorted(other.get_ingredients()):
            return True
        else:
            return False

    def __repr__(self):
        ing_lst = ", ".join(self.get_ingredients())
        return  f"* {ing_lst} *"