import random
from player_function import Player, player1

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
        global coin
        self.weapon.info()
        print(self.item.info())
        self.spell.info()
        print(f"You have {coin} coins")
        print(f"\n1. Buy the {self.weapon.name}\n2. Buy the {self.item.name}\n3. Buy the {self.spell.name}")
        inp = input("Your choice: ")
        if inp == "1" and coin >= self.weapon.coin:
            player1.new_weapon(self.weapon)
            coin -= self.weapon.coin
        if inp == "2" and coin >= self.item.coin:
            player1.items.append(self.item)
            coin -= self.item.coin
        if inp == "3" and coin >= self.spell.coin:
            player1.new_spell(self.spell)
            coin -= self.spell.coin