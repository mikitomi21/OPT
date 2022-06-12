from Player import *
from Tasks import *

def choose_option():
    print(f"{player.get_name()} lat {player.get_age()}")
    print("""Wybierz opcje:
    1.Nastepna tura
    2.Wyswietl umiejetnosci
    """)
    option = input()

def ask_for_next_game():
    while True:
        nextGame = input("Czy chcesz grac nowa postacia? (y/n)")
        if nextGame == 'y':
            return True
        elif nextGame == 'n':
            return False

if __name__ == "__main__":
    gameOn = True
    while gameOn:
        name = input("Name of your character: ")
        player = Player(name)

        while player.get_isAlive():
            player.print_skills()
            mission = rand_mission(player)
            print_mission(mission, player)

            player.set_isAlive()

        del(player)
        gameOn = ask_for_next_game()
