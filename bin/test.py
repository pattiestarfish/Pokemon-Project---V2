import pokemon_classes
#creating Trainers: class(name, potions, active pokemon)
pat = pokemon_classes.Trainer('Pat', None, None, None)
gary = pokemon_classes.Trainer('Gary', None, None, None)

#player instances
print(pat)
print(gary)
#testing trainer battles
#                    |----------------------------------------------|
#trainer commands:   |   Trainer.attack_trainer(Trainer, 'skill')   |
#                    |   Trainer.use_potion('potion name')          |
#                    |   Trainer.change_pokemon('Pokemon name')     |
#                    |----------------------------------------------|
#default_potions = {'quick heal': 18, 'medium heal': 35, 'super heal': 60}
#skills = {'fireball': 12, 'flamethrower': 19, 'inferno fire': 28, 'tackle': 7,
#           'water gun': 11, 'hydropump': 23, 'bubble gun': 14,
#           'lightning strike': 10, 'thunder': 18,
#           'vine whip': 12, 'gaia strike': 14, 'solarbeam': 27}

print(pat.attack_trainer(gary))
print(pat.change_pokemon('Lapras'))
print(pat.attack_trainer(gary))
print(gary.use_potion('super heal'))
print(gary.current_pokemon.revive())
print(gary.use_potion('medium heal'))
print(pat.change_pokemon('Warwick'))
#trainer battling with current active pokemon
#----------------------------------------------------
##early testing
#pat.curr_pokemon.attack(bulbasaur, 'lightning strike')
#print(charmander.lose_health(32))
#print(charmander.gain_health(10))
#print(pikachu.gain_health(10))
#print(charmander.revive())
#print(charmander.attack(bulbasaur, 'fireball'))
#print(squirtle.attack(bulbasaur, 'water gun'))
#print(pikachu.attack(bulbasaur, 'lightning strike'))