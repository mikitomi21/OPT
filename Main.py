
from Player import *
from Point import *
from Tasks import *


name = input("Name of your character: ")
player = Player(name)

while player.get_isAlive():
    player.print_skills()
    mission = rand_mission()
    print_mission(mission, player)


    player.set_isAlive()
del(player)
