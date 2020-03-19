import pokemon_classes
from datetime import datetime

#creating Trainers: class(name, potions, active pokemon)
pat = pokemon_classes.Trainer('Pat', None, None, None)
gary = pokemon_classes.Trainer('Gary', None, None, None)

#player instances
print("(Player1)"+str(pat))
print("(Player2)"+str(gary))

#GAME START
def user_interface():
    print("GAME START: " + str(datetime.now()) + '\n' + "Randomizing pokemon teams...")
    player_turn = True
    game_state = True
    action = 0

    while(game_state == True):
        if player_turn == True:
            active_player = pat
            inactive_player = gary
            if (inactive_player.current_pokemon.TKO == True):
                inactive_player.change_pokemon()
            elif(active_player.current_pokemon.TKO == True):
                active_player.change_pokemon()
        print(active_player.name + "'s turn, choose an option:\n1) Attack\n2) Change Pokemon\n3) Use potion\n4) Do nothing\n5) Surrender")
        print(str(active_player.current_pokemon) + ' vs ' + str(inactive_player.current_pokemon))
        action = input("# (1-5): ")
        if action == '1':
            active_player.attack_trainer(inactive_player)
            if(inactive_player.current_pokemon.curr_hp <= 0):
                print(str(inactive_player.current_pokemon) + " has fainted!!")
                inactive_player.change_pokemon()
        elif action == '2':
            active_player.change_pokemon()
        elif action == '3':
            print(active_player.use_potion('medium heal'))
        elif action == '4':
            print("Turn skipped.")
        elif action == '5':
            print(active_player.name + " surrenders! " + inactive_player.name + " wins!!")
            game_state = False
            return game_state
        else:
            print("Error input, try again")
            continue
        player_turn = False
        if player_turn == False:
            active_player = gary
            inactive_player = pat
            if (inactive_player.current_pokemon.TKO == True):
                inactive_player.change_pokemon()
            elif(active_player.current_pokemon.TKO == True):
                active_player.change_pokemon()
        print(active_player.name + "'s turn, choose an option:\n1) Attack\n2) Change Pokemon\n3) Use potion\n4) Do nothing\n5) Surrender")
        print(str(active_player.current_pokemon) + ' vs ' + str(inactive_player.current_pokemon))
        action = input("# (1-5): ")
        if action == '1':
            active_player.attack_trainer(inactive_player)
            if(inactive_player.current_pokemon.curr_hp <= 0):
                print(str(inactive_player.current_pokemon) + " has fainted!!")
                inactive_player.change_pokemon()
        elif action == '2':
            active_player.change_pokemon()
        elif action == '3':
            print(active_player.use_potion('medium heal'))
        elif action == '4':
            print("Turn skipped.")
        elif action == '5':
            print(active_player.name + " surrenders. " + inactive_player.name + " wins!!")
            game_state = False
            return game_state
        else:
            print("Error input, try again")
            continue
        player_turn = True

    if game_state == False:
        print("GAME OVER")
        return True


user_interface()