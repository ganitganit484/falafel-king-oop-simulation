import time
import copy

class Customer:
    def __init__(self, name, mood, personality, initial_patience=100, arrive_time=None):
        self.__name = name
        self.__mood = mood
        self.__personality = personality
        self.__initial_patience = initial_patience
        self.__patience = initial_patience
        if arrive_time is None:
            self.arrive_time = int(time.time()) #Because later on I want to access this field in another department I did not set it as private

    def get_mood(self):
        return copy.deepcopy(self.__mood)

    def get_waiting_time(self, current_time=None):
        if current_time is None:
            current_time = int(time.time())
        waiting_time = current_time - self.arrive_time
        return waiting_time

    def get_patience(self):
        return copy.deepcopy(round(self.__patience , 2))

    def update(self, waiting_time=None):
        if waiting_time is None:
            waiting_time = self.get_waiting_time()
        self.__patience = self.__initial_patience - self.get_mood().get_patience_factor(waiting_time) #Call the method from the appropriate class according to the mood type
        self.__mood = self.__personality.adjust_mood(self.get_mood(),waiting_time) #Call the method from the appropriate class according to the personality type

    def __repr__(self):
        number_of_asterisks = max(len("name: " + str(self.__name)), len("mood: " + str(self.__mood)), len("personality: " + str(self.__personality)), len("patience: " + str(self.__initial_patience)))
        asterisks_to_print = "*" * (number_of_asterisks+4)
        return (f"{asterisks_to_print}" "\n"
                f"* name: {self.__name}" + " " * (len(asterisks_to_print) - len(f"* name: {self.__name}") - 1) + "*" "\n"
                f"* mood: {self.__mood}" + " " * (len(asterisks_to_print) - len(f"* mood: {self.__mood}") - 1) + "*"  "\n"
                f"* personality: {self.__personality}" + " " * (len(asterisks_to_print) - len(f"* personality: {self.__personality}") - 1) + "*" "\n"
                f"* patience: {self.__patience}" + " " * (len(asterisks_to_print) - len(f"* patience: {self.__patience}") - 1) + "*" "\n"
                f"{asterisks_to_print}")
