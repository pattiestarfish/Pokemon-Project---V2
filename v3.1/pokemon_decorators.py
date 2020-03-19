def battle_decorator(print_battle):
    def wrapper(*args, **kwargs):
        print_battle(*args, **kwargs)
    return wrapper

@battle_decorator
def print_battle(self, target):
    print("___Trainer " + '*' + self + "* attacks " + "Trainer " + '*' + target + '*___')


def change_poke_decorator(print_battle):
    def wrapper(*args):
        print_battle(*args)
    return wrapper

@change_poke_decorator
def print_change_poke(self):
    print("___Trainer " + '*' + str(self) + "* changes Pokemon!!___")



#function ideas:
#max of 6 pokemon
#turn based battle (choose attack, use item, pass turn)
#add decorators for using items/changing pokemon/etc
#add randomization of pokemon teams upon instancing
