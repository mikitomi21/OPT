from Player import *
from Point import *

name = input("Name of your character: ")
player = Player(name)

while player.get_isAlive():
    print(f"Health: {player.get_health()}")
    print(f"Power: {player.get_power()}")
    print(f"Loyal: {player.get_loyal()}")
    print(f"Money: {player.get_money()}")
    
    player.set_isAlive()
