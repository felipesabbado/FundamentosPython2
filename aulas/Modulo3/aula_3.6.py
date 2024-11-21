# 3.6 Section 6 – Exceptions once again
class PizzaError(Exception):
    def __init__(self, pizza='unknown', message=''):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uknown', cheese='>100', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, 'no such pizza')
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, 'too much cheese')
    print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.pizza, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
