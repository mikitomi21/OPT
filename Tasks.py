import random

#skills -> [health, power, loyal, money]
tasks = {"burgers":
    [["Czy chcesz przywitac sie z nowymi mieszkancami miasta?", [0,0,2,0], [0,0,-2,0]],
    ["Czy pomozesz bezdomnemu?", [1,0,2,-3], [-1,0,-2,0]]],

        "nobility":[],

         "king":[]
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
