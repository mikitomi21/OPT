from Player import *
from Tasks import *


def ask_for_next_game():
    while True:
        nextGame = input("Czy chcesz grac nowa postacia? (y/n)")
        if nextGame == 'y':
            return True
        elif nextGame == 'n':
            return False


shop_elements = [("czlowiek", 18), ("miecz", 10), ("kwiatek", 2), ("ksiazki", 10), ("piwo", 7)]


def buy_element(player):
    print(f"Wybierz element, ktory chcesz kupic. Masz {player.get_money()} monety")
    for index, element in enumerate(shop_elements):
        print(f"{index + 1}. {element[0]}")
    choice = int(input())-1
    if player.get_money() >= shop_elements[choice][1]:
        player.add_money(-shop_elements[choice][1])
        player.add_element_to_backpack(shop_elements[choice][0])

def show_elements(player):
    elements = player.get_backpack()
    for index, elem in enumerate(elements):
        print(f"{index + 1}. {elem}")

def shop(player):
    print("""Wybierz co chcesz zrobic:
    1.Kup przedmiot
    2.Sprzedaj przedmiot
    3.Pokaz twoje przedmioty""")
    choice = int(input())
    if choice == 1:
        buy_element(player)
    elif choice == 2:
        pass
        # sell_element()
    elif choice == 3:
        show_elements(player)


def choose_option():
    print(f"{player.get_name()} lat {player.get_age()}")
    print("""Wybierz opcje:
    1.Nastepna tura
    2.Wyswietl umiejetnosci
    3.Idz na zakupy:
    4.Popelnij samobojstwo""")
    option = int(input())
    return option


if __name__ == "__main__":
    gameOn = True
    while gameOn:
        name = input("Name of your character: ")
        player = Player(name)

        while player.get_isAlive():
            option = choose_option()
            if option == 1:
                mission = rand_mission(player)
                print_mission(mission, player)
            elif option == 2:
                player.print_skills()
            elif option == 3:
                shop(player)
            elif option == 4:
                player.kill_outself()
            player.set_isAlive()

        del (player)
        gameOn = ask_for_next_game()
