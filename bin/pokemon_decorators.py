def battle_decorator(print_battle):
    def wrapper(*args, **kwargs):
        print_battle(*args, **kwargs)
    return wrapper

@battle_decorator
def print_battle(self, target):
    print("--===--" + self + " attacks " + target + "--===--")


#function ideas:
#max of 6 pokemon
#turn based battle (choose attack, use item, pass turn)
#add decorators for using items/changing pokemon/etc
#
3