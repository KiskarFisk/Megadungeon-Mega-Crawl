from player_function import Player, player1

import math
import random
import time
from colorama import Fore, Style, init
init()

floor_number = 1

class Floor():
    def __init__(self, number, enemy1, enemy2, enemy3, secret, shop):
        self.number = number
        self.enemies = []
        self.enemies.append(enemy1)
        if enemy2 is not None:
            self.enemies.append(enemy2)

        self.enemy1 = enemy1
        self.enemy2 = enemy2

        self.defeated = 0
        self.secret = secret
        self.shop = shop

    def running(self):
        global ac
        ac = 2
        #for item in player1.items: UNDO AFTER ADDING THE ITEM STUFF AGAIN
            #if item == protection:
                #ac += 2

        global floor_number
        global estus_count
        global estus_max
        global mana_pot_count
        global mana_pot_mox
        global player_hp, player_actions_max
        global player_mana, estus_max, player_max_mana

        #shop = Shop(self.shop)
        if floor_number % 3 == 0 and floor_number > 1:
            print(Fore.GREEN + "Estus Flasks and Mana Potions restored!" + Style.RESET_ALL)
            estus_count = estus_max
            mana_pot_count = mana_pot_mox
        if floor_number % 2 == 0 and floor_number > 1:
            player1.level_up() #add that
        if floor_number % 5 == 0:
            print("HP and Mana restored!")
            player1.hp = player1.max_hp
            player1.mana = player1.max_mana
        if floor_number == 6:
            print("You get another action")
            player1.actions_max += 1

            if player1.mana < player1.max_mana:
                player1.mana += 1
                print("You regained 1 mana!")

        while self.defeated < 2:
            print(f"\nYou are on floor {self.number}")
            if self.defeated == 0:
                print("1. Fight the level's enemy")
            if self.secret is not None:
                print("2. Check secret")
            if self.shop > 0:
                print("3. Shop")
            if self.defeated == 1:
                print("4. Go to the next floor")
            print("5. View inventory")
            print("6. View spells")
            inp = input("Choose what to do ")

            if inp == "1" and self.defeated == 0:
                self.fight()
            if inp == "2" and self.secret is not None:
                self.secret.running()
            #if inp == "3" and self.shop > 0:
                #shop.shopping()
            if inp == "4" and self.defeated == 1:
                floor_number += 1
                if floor_number % 5 == 0:
                    player1.upgrade_estus() #add that
                return
            if inp == "5":
                player1.show_inv()
            if inp == "6":
                if player1.spell1 is not None:
                    print(f"{player1.spell1.info()}")
                if player1.spell2 is not None:
                    print(player1.spell2.info())
                if player1.spell3 is not None:
                    player1.spell3.info()
            if inp == "7":
                player1.swap_weapon()

    def fight(self):
        dmg_red = 0
        while self.defeated == 0:
            dmg_red = 0
            if player1.hp <= 0:
                print("\nYou are defeated...")
                quit()

            player1.actions = player1.actions_max
            print("Enemies:")
            if self.enemy1 is not None:
                self.enemy1.info()
            if self.enemy2 is not None:
                self.enemy2.info()

            while player1.actions > 0:
                print(f"You have {player1.hp} HP and {player1.mana} Mana")
                print(f"Remaining actions: {player1.actions}")
                print("1. Attack\n2. Magic\n3. Defend\n4. Items")
                inp = input("Choose what to do ")
                if inp == "1": # Attacking
                    target_select = 0
                    target = None
                    if self.enemy1 is not None and self.enemy2 is None:
                        target = self.enemy1
                        target_select = 1
                    if self.enemy1 is None and self.enemy2 is not None:
                        target = self.enemy2
                        target_select = 2
                    while target_select == 0:
                        print("Which enemy to attack (1 or 2)?")
                        inp = input("Your decision: ")
                        if inp == "1" and self.enemy1 is not None:
                            target = self.enemy1
                            target_select = 1
                        if inp == "1" and self.enemy1 is None:
                            print("No enemy 1")
                        if inp == "2" and self.enemy2 is not None:
                            target = self.enemy2
                            target_select = 1
                        if inp == "2" and self.enemy2 is None:
                            print("No enemy 2")
                    rum = random.randint(1,100)
                    if rum <= player1.equipped_item.to_hit:
                        damage = damage_modifier(target, player1.equipped_item.damage_type, player1.equipped_item.damage)
                        target.HP -= damage
                        print(f"Attacked {target.name} for {damage} damage")
                        time.sleep(1)
                        player1.actions -= 1
                    else:
                        print(f"Missed {target.name}")
                        time.sleep(1)
                        player1.actions -= 1
                    inp = 0

                if inp == "2": #Casting a spell
                    target_select = 0
                    target = None
                    if self.enemy1 is not None and self.enemy2 is None:
                        target = self.enemy1
                        target_select = 1
                    if self.enemy1 is None and self.enemy2 is not None:
                        target = self.enemy2
                        target_select = 2
                    while target_select == 0:
                        print("Which enemy to attack (1 or 2)?")
                        inp = input("Your decision: ")
                        if inp == "1" and self.enemy1 is not None:
                            target = self.enemy1
                            target_select = 1
                        if inp == "1" and self.enemy1 is None:
                            print("No enemy 1")
                        if inp == "2" and self.enemy2 is not None:
                            target = self.enemy2
                            target_select = 1
                        if inp == "2" and self.enemy2 is None:
                            print("No enemy 2")
                    damage, passes, heal, type = player1.cast_spell()
                    if passes > 0:
                        player1.actions -= 1
                        if damage > 0:
                            damage = damage_modifier(target, type, damage)
                            print(f"You deal {damage} damage to {target.name}")
                            target.HP -= damage
                        if heal > 0:
                            print(f"You heal {heal} HP")
                            player1.hp += heal

                if inp == "3": # defending
                    print("You brace yourself")
                    dmg_red = ac
                    print(f"Your damage reduction is {dmg_red}")
                    player1.actions -= 1

                if inp == "4":
                    player1.show_inv()

            if self.enemy1 is not None:
                if self.enemy1.HP > 0:
                    damage = self.enemy1.fight()
                    if damage is not None:
                        damage -= dmg_red
                        if damage > 0:
                            player1.hp -= damage
                    else:
                        print(f"{self.enemy1.name} missed")

            if self.enemy2 is not None:
                if self.enemy2.HP > 0:
                    damage = self.enemy2.fight()
                    if damage is not None:
                        damage -= dmg_red
                        if damage > 0:
                            player1.hp -= damage
                    else:
                        print(f"{self.enemy2.name} missed")

            if self.enemy1 is not None:
                if self.enemy1.HP <= 0:
                    print(f"Defeated {self.enemy1.name}")
                    print(f"Gained {self.enemy1.coin} coin")
                    player1.coin += self.enemy1.coin
                    if self.enemy1.drop is not None:
                        print(f"They also dropped {self.enemy1.drop.info()}")
                        player1.items.append(self.enemy1.drop)
                    self.enemy1 = None

            if self.enemy2 is not None:
                if self.enemy2.HP <= 0:
                    print(f"Defeated {self.enemy2.name}")
                    print(f"Gained {self.enemy2.coin} coin")
                    player1.coin += self.enemy2.coin
                    if self.enemy2.drop is not None:
                        print(f"They also dropped {self.enemy2.drop.info()}")
                        player1.items.append(self.enemy2.drop)
                    self.enemy2 = None

            if self.enemy1 is None and self.enemy2 is None:
                self.defeated = 1

def damage_modifier(enemy, type, damage):
    if enemy.weakness is not None:
        if enemy.weakness == type:
            damage *= 2
            damage = math.floor(damage)
            return damage
    if enemy.resistant is not None:
        if enemy.resistant == type:
            damage *= 0.5
            damage = math.floor(damage)
            return damage
    return damage

floors = []

floors.append(Floor(1, None, None, None, None, 0))

# giant rat floor 1 btw