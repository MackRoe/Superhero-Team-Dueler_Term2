from armor import Armor
from hero import Hero
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team
from arena import Arena
import team_test

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
    # print('')
    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)
    # print('')
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # # print(hero.abilities)
    # print(hero.attack())
    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)
    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())

    # hero = Hero("Wonder Woman")
    # weapon = Weapon("Lasso of Truth", 90)
    # hero.add_weapon(weapon)
    # print(hero.attack())

    arena = Arena()
    # arena.build_team_one()
    # arena.build_team_two()
    hero1 = team_test.build_hero(num_of_weapons=1, num_of_armor=1, num_of_abilities=1)
    hero2 = team_test.build_hero(num_of_weapons=1, num_of_armor=1, num_of_abilities=1)
    team1z = team_test.create_team([hero1])
    team2z = team_test.create_team([hero2])
    arena.team_one = team1z
    arena.team_two = team2z
    arena.team_one_size = 1
    arena.team_two_size = 1
    arena.team_battle()
    arena.show_stats()
