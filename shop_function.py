import random
from player_function import Player, player1

from weapon_function import lvl1_weapon, lvl_2_weapon, t3_weapon
from item_function import lvl1_item, t2_item, t3_item
from spell_function import lvl1_spell, t2_spell, t3_spell

class Shop():
    def __init__(self, level):
        self.level = level

        if self.level == 1:
            self.weapon = random.choice(lvl1_weapon)
            self.item = random.choice(lvl1_item)
            self.spell = random.choice(lvl1_spell)

        if self.level == 2:
            self.weapon = random.choice(lvl_2_weapon)
            self.spell = random.choice(t2_spell)
            self.item = random.choice(t2_item)

        if self.level == 3:
            self.weapon = random.choice(t3_weapon)
            self.spell = random.choice(t3_spell)
            self.item = random.choice(t3_item)

    def shopping(self):
        self.weapon.info()
        print(self.item.info())
        self.spell.info()
        print(f"You have {player1.coin} coins")
        print(f"\n1. Buy the {self.weapon.name}\n2. Buy the {self.item.name}\n3. Buy the {self.spell.name}")
        inp = input("Your choice: ")
        if inp == "1" and player1.coin >= self.weapon.coin:
            player1.new_weapon(self.weapon)
            player1.coin -= self.weapon.coin
        if inp == "2" and player1.coin >= self.item.coin:
            player1.items.append(self.item)
            player1.coin -= self.item.coin
        if inp == "3" and player1.coin >= self.spell.coin:
            player1.new_spell(self.spell)
            player1.coin -= self.spell.coin