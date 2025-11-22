import floor_handle
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

while floor_handle.floor_number < len(floor_handle.floors) and player1.hp > 0:
    save.save()
    print("Game saved!")
    floor = floor_handle.floors[floor_handle.floor_number - 1]
    print(floor_handle.floor_number)
    floor.running()
