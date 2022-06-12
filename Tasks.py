import random

tasks = [
    ["Czy chcesz przywitac sie z nowymi mieszkancami miasta?", [0,0,2,0], [0,0,-2,0]],
    ["Czy pomozesz bezdomnemu?", [1,0,2,-3], [-1,0,-2,0]]
]


def rand_mission():
    return random.randint(0, len(tasks) - 1)

def print_mission(mission, player):
    print(tasks[mission][0])
    choice = input()
    if choice == 'y':
        player.add_skills(tasks[mission][1])
    elif choice == 'n':
        player.add_skills(tasks[mission][2])
