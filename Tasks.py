import random

#skills -> [health, power, loyal, money]
tasks = {"burgers":
            [
                ["Rodzice proponuja abys poszedl do szkoly. Chcesz uczesczac do szkoly?", [0,1,1,0], [0,0,-2,0]],
                ["Bezdomny prosi ciebie o troche pieniadzy na jedzenie. Dasz mu swoje drobne?", [0,0,2,-2], [0,0,-1,0]],
                ["Masz dzisiaj urodziny. Czy odbierzesz prezent urodziny od swoich rodzicow?", [0,0,0,3], [0,0,0,0]],
                ["Widzisz jak 2 ludzi grozi kobiecie ze ja pobija. Zaatakujesz ich w obronie kobiety?", [-2,0,2,2], [0,0,0,0]],
                ["Ojciec prosi cie o pomoc w robocie. Pomozesz mu?", [-1,0,1,1], [1,0,-3,0]],

            ],

        "nobility":
            [
                ["Twoj znajomy proponuje ci kupic czlowieka do zajmowania sie twoim polem. Kupisz go?", [0,1,1,-3], [0,0,-1,0]],
                ["Ktos wlamal sie do twojego mieszkania z nozem. Grozi ci, ze jezeli nie oddasz mu pieniedzy to ciebie zaatakuje. Dasz mu pieniadze?", [0,0,0,-5], [-5,0,0,0]],
                ["Twoi podwadni nazekaja na bardzo niskie warunki pracy. Poprawisz je?", [0,0,2,-3], [-2,0,-2,0]],
                ["Krol przyjezdza do cb z wizyta. Przyjmiesz go do swojej posiadlosci?", [2,2,2,2], [0,0,-8,0]],
                ["Wrog najechal na twoj kraj. Bedziesz bronil swojej ojczyzny?", [-4,2,4,-2], [0,0,-4,0]]
            ],

         "king":
             [
                ["Ktos na tle mieszkancow zaczac cb wyzywac. Ukarasz go?", [0,2,-3,-1], [0,-3,-1,0]],
                ["Przajzny kraj proponuje sojusz. Przyjmiesz go?", [0,2,2,-1], [0,0,-2,0]],
             ]
}


def rand_mission(player):
    return random.randint(0, len(tasks[player.get_estate()]) - 1)

def print_mission(mission, player):
    print(tasks[player.get_estate()][mission][0])
    choice = input()
    if choice == 'y':
        player.add_skills(tasks[player.get_estate()][mission][1])
    elif choice == 'n':
        player.add_skills(tasks[player.get_estate()][mission][2])
