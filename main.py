from floor_handle import floors, Floor
from player_function import Player, player1

from colorama import Fore, Style, init
init()

floor = 1

print("MDMC 0.3.3")

floor_number = 1
while floor_number < len(floors) and player1.hp > 0:
    floor = floors[floor_number - 1]
    floor.running()