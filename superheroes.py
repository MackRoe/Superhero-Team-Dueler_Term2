from armor import Armor
from hero import Hero
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team
from arena import Arena
# import team_test

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
