from floor_handle import floors, floor_number
from player_function import Player, player1
import save_function as save
import os

from colorama import Fore, Style, init
init()

if os.path.exists("save.pkl"):
    inp = input("y/n load existing save? ")
    if inp == "y":
        save.load()
    else:
        print("Not loading save, good luck!")

print("MDMC 0.3.4")

while floor_number < len(floors) and player1.hp > 0:
    save.save()
    print("Game saved!")
    floor = floors[floor_number - 1]
    floor.running()
    floor_number += 1