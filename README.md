# Falafel King: OOP Management Simulation (Python)

A modular, turn-based restaurant management simulation modeled in Python, inspired by the arcade game "Falafel King". The architecture applies rigorous Object-Oriented Design (inheritance, abstraction, composition, and polymorphism), behavioral Strategy patterns for order and serving prioritization, and dynamic mathematical customer decay modeling.

## System Architecture & OOP Principles
- Abstract Base Classes (`ABC`): Standardizes extensible behavior across four core hierarchies (`Mood`, `Personality`, `OrdersStrategy`, and `ServingStrategy`).
- Dynamic Mood & Patience Mechanics: Customer patience degrades dynamically based on waiting duration and active mood, while customer personality dictating mood transitions over waiting thresholds.
- Strategy Pattern Implementations:
  - Orders Strategies: Produces customer orders either via an infinite pseudo-random generator (`RandomOrdersStrategy`) or pre-configured batch feeds (`FixedOrdersStrategy`).
  - Serving Strategies: Dynamically selects the next order by earliest arrival (`ArrivalTimeServingStrategy`), maximum wait time (`LongestWaitingTimeServingStrategy`), or critical patience (`LeastPatienceCustomerServingStrategy`).
- Fail-Safe Exception Framework: Dedicated domain-specific exception types (`NoSuchIngredientException`, `NotCustomerDishException`, `NoSuchOrderException`, `OrderOutOfBoundsException`) enforcing strict runtime state assertions.
- Test-Driven Validation: Unit test suites implemented via `unittest` verifying domain model contracts.

## Class & Module Hierarchy
- Game Driver: `Game.py`, `FalafelStall.py`, `Dish.py`, `Customer.py`
- Abstract Bases: `Mood.py`, `Personality.py`, `OrdersStrategy.py`, `ServingStrategy.py`
- Concrete Moods: `Chill.py`, `Calm.py`, `Angry.py`, `Furious.py`, `Explosive.py`
- Personalities: `TypeA.py`, `TypeB.py`
- Serving Strategies: `ArrivalTimeServingStrategy.py`, `LongestWaitingTimeServingStrategy.py`, `LeastPatienceCustomerServingStrategy.py`
- Order Generators: `RandomOrdersStrategy.py`, `FixedOrdersStrategy.py`
- Error Handling: `exceptions.py`
- Unit Testing: `test_Calm.py`, `test_Dish.py`, `test_TypeA.py`, `test_Game.py`

## Requirements
- Python 3.8 or higher.
- Standard libraries: `math`, `time`, `random`, `unittest`, `abc`.

## Build & Execution

Run interactive game loop:
python main.py

Run unit test verification:
python -m unittest discover -s . -p "test_*.py"
