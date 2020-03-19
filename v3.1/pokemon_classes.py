from pip._vendor.distlib.compat import raw_input
from pokemon_decorators import battle_decorator, print_battle, change_poke_decorator, print_change_poke
import random

# Pokemon skills, type separated: [name, damage]
fire_skills = {'fireball': 12, 'flamethrower': 19, 'inferno fire': 28, 'tackle': 7}
water_skills = {'water gun': 11, 'hydropump': 23, 'bubble gun': 14, 'tackle': 7}
electric_skills = {'lightning strike': 10, 'thunder': 18, 'tackle': 7, }
grass_skills = {'vine whip': 12, 'gaia strike': 14, 'solarbeam': 27, 'tackle': 7}

#type-linked dict-- had trouble referencing above dicts in skill_types, so hard coded instead
skill_types = {'Fire': {'fireball': 12, 'flamethrower': 19, 'inferno fire': 28, 'tackle': 7}, 'Water': {'water gun': 11, 'hydropump': 23, 'bubble gun': 14, 'tackle': 7}, 'Electric': {'lightning strike': 10, 'thunder': 18, 'tackle': 7, }, 'Grass': {'vine whip': 12, 'gaia strike': 14, 'solarbeam': 27, 'tackle': 7}}

#all skills in 1 dictionary
skills = {'fireball': 12, 'flamethrower': 19, 'inferno fire': 28, 'tackle': 7,
           'water gun': 11, 'hydropump': 23, 'bubble gun': 14,
           'lightning strike': 10, 'thunder': 18,
           'vine whip': 12, 'gaia strike': 14, 'solarbeam': 27}

# heals-- try to link name key to list [quantity, heal amount]
default_potions = {'quick heal': 18, 'medium heal': 35, 'super heal': 60, 'quick heal': 18, 'quick heal': 18, 'revive': 1}

class Pokemon:
    def __init__(self, name, level, type, TKO=False):
        self.name = name
        self.level = level
        self.type = type
        self.max_hp = level * 4
        self.curr_hp = level * 4
        self.TKO = TKO

    def __repr__(self):
        # print("Summoning Pokemon: ")
        return 'Lv. ' + str(self.level) + " " + self.name + "(" + self.type + "), " + str(self.curr_hp) + '/' + str(
            self.max_hp) + ' HP'

    def lose_health(self, dmg):
        # print(self.name + ' takes ' + str(dmg) + ' damage: ')
        if self.curr_hp > 0 and self.TKO == False:
            self.curr_hp = round(self.curr_hp - dmg)
            if self.curr_hp <= 0:
                self.TKO = True
                print(('(' + str(self.curr_hp) + '/' + str(
                    self.max_hp) + ' HP), ' + self.name + ' takes ' + str(dmg) + ' damage and has been KOed!!') + '\n')
                return True
        print((self.name + ' takes ' + str(round(dmg)) + ' damage, and now has ' + str(round(self.curr_hp)) + '/' + str(
            self.max_hp) + ' HP.') + '\n')
        return True

    def gain_health(self, gain):
        print(self.name + ": recovering " + str(gain) + ' health..')
        if (self.TKO == True):
            return "But nothing happened! " + self.name + " is currently KOed and cannot regain health!!" + '\n'
        elif (self.curr_hp + gain > self.max_hp):
            return self.name + " is now at full HP (" + str(self.max_hp) + '/' + str(self.max_hp) + ').' + '\n'
        else:
            self.curr_hp += gain
            return self.name + " has recovered " + str(gain) + ' health points, and now has ' + str(
                self.curr_hp) + '/' + str(self.max_hp) + " HP." + '\n'

    def revive(self):
        print("Reviving " + self.name + ":")
        if self.TKO == True:
            self.TKO = False
            return self.name + " has been revived with " + str(round(self.max_hp * 0.35)) + '/' + str(
                self.max_hp) + ' HP.' + '\n'
        else:
            return self.name + " is not KOed.\n"

    def attack(self, other_pokemon, skill):  # fire, water, electric, grass; 1.35x vs 0.60x
        super_eff = round((self.level) / 2)
        normal = 1.0
        less_eff = 0.6
        damage = skills.get(skill)
        print(self.name + " uses " + skill + ' on ' + other_pokemon.name + '!')
        if(skill == 'tackle'):
            return other_pokemon.lose_health(damage * normal)
        elif ((self.type == 'Fire' and other_pokemon.type == 'Grass') or (
                self.type == 'Water' and other_pokemon.type == 'Fire') or (
                self.type == 'Grass' and other_pokemon.type == 'Water') or (
                self.type == 'Electric' and other_pokemon.type == 'Water')):
            print("It's super effective!!")
            return other_pokemon.lose_health(damage + super_eff)
        elif ((self.type == 'Grass' and other_pokemon.type == 'Fire') or (
                self.type == 'Fire' and other_pokemon.type == 'Water') or (
                      self.type == 'Water' and other_pokemon.type == 'Grass') or (
                      self.type == 'Water' and other_pokemon.type == 'Electric')):
            print("It's not very effective...")
            return other_pokemon.lose_health(damage * less_eff)
        else:
            return other_pokemon.lose_health(damage * normal)

# Pokemon objects = class(name, level, type)
charmander = Pokemon('Charmander', 16, 'Fire')
pikachu = Pokemon('Pikachu', 18, 'Electric')
bulbasaur = Pokemon('Bulbusaur', 14, 'Grass')
squirtle = Pokemon('Squirtle', 15, 'Water')
lapras = Pokemon('Lapras', 21, 'Water')
ninetails = Pokemon('Ninetails', 23, 'Fire')
bellsprout = Pokemon('Bellsprout', 20, 'Grass')
starmie = Pokemon('Starmie', 18, 'Water')
flareon = Pokemon('Flareon', 24, 'Fire')
jolteon = Pokemon('Jolteon', 23, 'Electric')
voltorb = Pokemon('Voltorb', 20, 'Electric')
magikarp = Pokemon('Magikarp', 14, 'Water')
#pokemon no. (randomize pokemon teams on initiation)
pokedex = [charmander, pikachu, bulbasaur, squirtle, lapras, ninetails, bellsprout, starmie, flareon, jolteon, voltorb, magikarp]
random.shuffle(pokedex)
print(pokedex)
temp_pat_team = []
temp_gary_team = []
for i in range(0,6):
    temp_pat_team.append(pokedex.pop())
pat_team = {'Pat': temp_pat_team}
for i in range(0,6):
    temp_gary_team.append(pokedex.pop())
gary_team = {'Gary': temp_gary_team}

#identifying player poke's
player_pokemon = {'Pat': [charmander], 'Gary': [bulbasaur]}
player_pokemon.update(pat_team)
player_pokemon.update(gary_team)

class Trainer:
    def __init__(self, name, pokemons=None, current_pokemon=None, potions=None, ):
        self.name = name
        if potions is None:
            self.potions = default_potions
        self.potions = potions
        if pokemons is None and self.name in player_pokemon:
            self.pokemons = player_pokemon.get(self.name)
            if(len(self.pokemons))>6:
                print(self.name + " exceeded max pokemon roster limit (6), removing " + str(self.pokemons[6]))
                self.pokemons.pop()
        if current_pokemon is None:
            self.current_pokemon = player_pokemon.get(self.name)[0]
    def __repr__(self):
        return ("Initializing trainer " + self.name + ":\n" + self.name + '\'s team: ' + str(
            self.pokemons) + '\nActive Pokemon: ' + str(self.current_pokemon)) + '\n'

    def attack_trainer(self, target_trainer, skill=None):
        print_battle(self.name, target_trainer.name)
        battle_instance_dmg = []
        battle_instance_skill = []
        temp = 0
        if skill is None:
            for key, values in skill_types.items():
                if(key == self.current_pokemon.type):
                   iter1 = 1
                   for key in skill_types.get(key):
                     print(str(iter1) + "). " + key + ' (' + str(values.get(key)) + " base dmg) ")
                     iter1 += 1
                     battle_instance_dmg.append(values.get(key))
                   for val in values:
                        battle_instance_skill.append(val)
        temp = input('Choose a skill # (1-4): ')
        temp = int(temp) - 1
        skill = battle_instance_skill[temp]
        battle = self.current_pokemon.attack(target_trainer.current_pokemon, skill)
        return battle

    def use_potion(self, potion_name=None):
        if potion_name == None:
            pass
        print(self.name + " used " + potion_name + " on " + self.current_pokemon.name + "--")
        heal = self.current_pokemon.gain_health(default_potions.get(potion_name))
        return heal

    def change_pokemon(self, poke_name=None):
      while(True):
        print_change_poke(self.name)
        change_poke_instance = []
        if poke_name == None:
          iter2 = 1
          for poke in self.pokemons:
            print(str(iter2) + '). ' + str(poke))
            change_poke_instance.append(poke.name)
            iter2 += 1
        temp = input('Choose a pokemon # (1-6): ')
        temp = int(temp) - 1
        poke_name = change_poke_instance[temp]
        print(self.name + " substitutes " + poke_name + " for " + str(self.current_pokemon.name) + "...")
        if(self.current_pokemon.name == poke_name):
            print(str(self.current_pokemon.name) + " is already active!\n")
            return True
   #     elif(self.current_pokemon.TKO == True):
   #         print("Can't, " + poke_name + " is currently KOed.")
        else:
            i = 0
            for i in range(len(self.pokemons)):
                if (self.pokemons[i].name == poke_name):
                    temp_poke=player_pokemon.get(self.name)[i]
                    if(temp_poke.TKO == True):
                        print("Can't, " + temp_poke.name+ " is currently KOed.\n")
                        return True
                    self.current_pokemon = player_pokemon.get(self.name)[i]
                    print(str(self.current_pokemon.name) + " is now active!\n")
                    return False
                i += 1
        print("Error, you do not own " + poke_name)
        return True
