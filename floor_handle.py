from player_function import Player, player1

import math
import random
import time
from colorama import Fore, Style, init
init()

floor_number = 1

from shop_function import Shop

import enemy_attack_function as attack
import item_function as item
import weapon_function as weapon
import spell_function as spell

class Secret():
    def __init__(self, condition, item, description, prize, prize_type):
        self.condition = condition # attack, item, code, creative
        self.item = item
        self.description = description
        self.prize = prize
        self.prize_type = prize_type

    def running(self):
        done = 0
        while done == 0:
            print(self.description)
            print("1. Attack the wall\n2. Use an item\n3. Quit")
            print("You can also try inputting something of your own!")
            inp = input("Make a choice: ")
            if inp == "1" and self.condition != "attack":
                print("You slashed at the wall... nothing happened")
            if inp == "1" and self.condition == "attack":
                self.prize_time()
                done = 1

            if inp == "2":
                item = choose_item()
                if item is not None:
                    if item.name == self.item.name:
                        print("It worked!")
                        self.prize_time()
                        done = 1
                    else:
                        print("It did not work")

            if inp == "3":
                done = 1

            if self.condition == "creative" and inp == self.item:
                self.prize_time()
                done = 1

    def prize_time(self):
        if self.prize_type == "item":
            player1.items.append(self.prize)
            print(f"You got {self.prize.name}")
        if self.prize_type == "weapon":
            print(f"You got {self.prize.name}")
            player1.new_weapon(self.prize)
        if self.prize_type == "spell":
            print(f"You got {self.prize.name}")
            player1.new_spell(self.prize)

def choose_item():
    for i, item in enumerate(player1.items, 1):
        print(f"{i}, {item.info()}")

        inp = input("Pick an item, use accurate case: ")

        for item in player1.items:
            if item.name == inp:
                thing = item
                return thing

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
        for item in player1.items:
            if item == item.protection:
                ac += 2

        global floor_number
        global estus_count
        global estus_max
        global mana_pot_count
        global mana_pot_mox
        global player_hp, player_actions_max
        global player_mana, estus_max, player_max_mana

        shop = Shop(self.shop)
        if floor_number % 3 == 0 and floor_number > 1: # fix all of this soon
            print(Fore.GREEN + "Estus Flasks and Mana Potions restored!" + Style.RESET_ALL)
            player1.estus_count = player1.estus_max
            player1.mana_pot_count = player1.mana_pot_max
        if floor_number % 2 == 0 and floor_number > 1:
            player1.level_up()
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
            if inp == "3" and self.shop > 0:
                shop.shopping()
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

class Enemy:
    def __init__(self, name, HP, weakness, resistant, action_count, attack1, attack2, attack3, coin, drop):
        self.name = name
        self.HP = HP
        self.max_HP = HP
        self.weakness = weakness
        self.resistant = resistant
        self.action_count = action_count
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3
        self.coin = coin
        self.drop = drop

    def fight(self):
        rum = random.randint(1,3)

        if rum == 1:
            rum = random.randint(1, 100)
            if rum <= self.attack1.to_hit:
                print(f"{self.name} hit you with {self.attack1.name} for {self.attack1.damage} damage!")
                return self.attack1.damage
            else:
                return None
        if rum == 2:
            if self.attack2 is None:
                rum = random.randint(1, 100)
                if rum <= self.attack1.to_hit:
                    print(f"{self.name} hit you with {self.attack1.name} for {self.attack1.damage} damage!")
                    return self.attack1.damage
                else:
                    return None
            else:
                rum = random.randint(1, 100)
                if rum <= self.attack2.to_hit:
                    print(f"{self.name} hit you with {self.attack2.name} for {self.attack2.damage} damage!")
                    return self.attack2.damage
                else:
                    return None
        if rum == 3:
            if self.attack3 is None:
                inp = random.randint(1,2)
                if inp == 1:
                    rum = random.randint(1, 100)
                    if rum <= self.attack1.to_hit:
                        print(f"{self.name} hit you with {self.attack1.name} for {self.attack1.damage} damage!")
                        return self.attack1.damage
                    else:
                        return None
                if inp == 2 and self.attack2 is not None:
                    rum = random.randint(1, 100)
                    if rum <= self.attack2.to_hit:
                        print(f"{self.name} hit you with {self.attack2.name} for {self.attack2.damage} damage!")
                        return self.attack2.damage
                    else:
                        return None
                elif inp == 2 and self.attack2 is None:
                    rum = random.randint(1, 100)
                    if rum <= self.attack1.to_hit:
                        print(f"{self.name} hit you with {self.attack1.name} for {self.attack1.damage} damage!")
                        return self.attack1.damage
                    else:
                        return None
            else:
                rum = random.randint(1, 100)
                if rum <= self.attack3.to_hit:
                    return self.attack3.damage
                else:
                    return None

    def info(self):
        print(f"{self.name}")
        print(f"HP = {self.HP}")

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

def make_slime_mold():
    return Enemy("Slime Mold", 12, "fire", "normal", 1, attack.infest, None, None, 9, None)
def make_mini_luna():
    return Enemy("Mini Luna", 7, "holy", "dark", 1, attack.bite1, None, None, 1, None)
def make_giant_snail():
    return Enemy("Giant Snail", 12, "lightning", "fire", 1, attack.slime, None, None, 4, None)
def make_lightning_rat():
    return Enemy("Lightning Rat", 8, None, "lightning", 1, attack.shocker1, attack.bite1, None, 4, None)
def make_infected_mini_luna():
    return Enemy("Slime Mold Infected Mini Luna", 23, "lightning", "fire", 1, attack.bite2, attack.infest, None, 8, item.chocolate)

giant_rat = Enemy("Giant Rat", 5, None, None, 1, attack.bite1, None, None, 2, None)
floors.append(Floor(1, giant_rat, None, None, None, 0))

secret = Secret("creative", "push", "The stones of the wall are fairly normal though ones seems to jut out more than the others", weapon.ishmar_blade, "weapon")
giant_rat = Enemy("Giant Rat", 5, None, None, 1, attack.bite1, None, None, 2, None)
thief = Enemy("Thief", 6, None, None, 1, attack.stab, None, None, 5, None)
floors.append(Floor(2, giant_rat, thief, None, secret, 0))

thief = Enemy("Thief", 6, None, None, 1, attack.stab, None, None, 5, None)
flaming_rat = Enemy("Flaming Rat", 5, None, "fire", 1, attack.bite1, attack.spit_flame, None, 2, None)
floors.append(Floor(3, thief, flaming_rat, None, None, 1))

floors.append(Floor(4, make_mini_luna(), make_mini_luna(), None, None, 0))

slime_mold = Enemy("Slime Mold", 12, "fire", "normal", 1, attack.infest, None, None, 9, item.shredded_book)
floors.append(Floor(5, slime_mold, None, None, None, 1))

giant_snail = Enemy("Giant Snail", 12, "lightning", "fire", 1, attack.slime, None, None, 4, None)
flaming_rat = Enemy("Flaming Rat", 5, None, "fire", 1, attack.bite1, attack.spit_flame, None, 2, None)
floors.append(Floor(6, giant_snail, flaming_rat, None, None, 0))

mini_luna = Enemy("Mini Luna", 7, None, None, 1, attack.bite1, None, None, 1, None)
giant_snail = Enemy("Giant Snail", 12, "lightning", "fire", 1, attack.slime, None, None, 4, None)
floors.append(Floor(7, mini_luna, giant_snail, None, None, 0))

secret = Secret("attack", None, "A portion of the wall is cracked", spell.lightning_ball, "spell")
floors.append(Floor(8, make_slime_mold(), make_mini_luna(), None, secret, 1))

floors.append(Floor(9, make_lightning_rat(), make_lightning_rat(), None, None, 0))

floors.append(Floor(10, make_infected_mini_luna(), None, None, None, 1))

# T2

def make_moldequin():
    return Enemy("Moldequin", 20, "lightning", "fire", 1, attack.infest2, None, None, 7, None)
def make_mold_beast():
    return Enemy("Mold Beast", 28, "lightning", "fire", 1, attack.infest2, attack.claw, attack.bite2, 8, None)
def make_rat_infect():
    return Enemy("Giant Infested Rat", 37, "lightning", "fire", 2, attack.bite2, attack.infest2, None, 12, item.rat_crown)
def make_statue():
    return Enemy("Infested Statue", 34, "lightning", "fire", 1, attack.smash, attack.infest, None, 9, None)
def make_great_mold():
    return Enemy("Massive Slime Mold Growth", 57, "lightning", "fire", 1, attack.infest3, None, None, 16, item.slime_key)

floors.append(Floor(11, make_moldequin(), None, None, None, 0))

floors.append(Floor(12, make_moldequin(), make_moldequin(), None, None, 2))

secret = Secret("item", item.shredded_book, "There is a whole in the wall, large enough to place an object inside, there are strange symbols around it.", weapon.longinus_spear, "weapon")
floors.append(Floor(13, make_mold_beast(), None, None, secret, 0))

floors.append(Floor(14, make_moldequin(), make_mold_beast(), None, None, 0))

floors.append(Floor(15, make_rat_infect, None, None, None, 0))

floors.append(Floor(16, make_mold_beast(), make_mold_beast(), None, None, 2))

secret = Secret("creative", "pull", "There is a torch on the wall lower than the rest.", spell.great_dual_spell, "spell")
floors.append(Floor(17, make_statue(), None, None, secret, 0))

floors.append(Floor(18, make_mold_beast(), make_statue(), None, None, 0))

floors.append(Floor(19, make_statue(), make_statue(), None, None, 2))

floors.append(Floor(20, make_great_mold(), make_statue(), None, None, 0))

# Tier 3

def make_kobold():
    return Enemy("Kobold", 28, "ice", "lightning", 1, attack.stab2, None, None, 9, None)
def make_fly_kobold():
    return Enemy("Flying Kobold", 33, "ice", "lightning", 1, attack.stab2, attack.wind_gust, None, 7, None)
def make_lizardfolk():
    return Enemy("Lizardfolk", 40, "ice", "lightning", 1, attack.sword2, attack.stab2, None, 11, None)
def great_lizard():
    return Enemy("Great Lizardfolk", 58, "ice", "lightning", 2, attack.sword2, None, None, 14, None)
def make_half_dragon():
    return Enemy("Half-Dragon", 54, "ice", "lightning", 1, attack.lightning_breath, attack.claw2, None, 4, None)
def lightning_wyrmling():
    return Enemy("Young Blue Dragon", 78, "ice", "lightning", 1, attack.lightning_breath, attack.claw2, None, 30, item.dragon_key)

secret = Secret("item", item.anti_mold, "There is an awful growth of mold on the wall", weapon.moss_infest_sword, "weapon")
floors.append(Floor(21, make_kobold(), None, None, secret, 3))

floors.append(Floor(22, make_kobold(), make_kobold(), None, None, 0))

secret = Secret("item", item.chocolate, "There is one of those awful Luna things growing on the wall", item.protection, "item")
floors.append(Floor(23, make_fly_kobold(), make_fly_kobold(), None, secret, 0))

floors.append(Floor(24, make_lizardfolk(), make_fly_kobold(), None, None, 3))

floors.append(Floor(25, make_lizardfolk(), make_lizardfolk(), None, None, 0))

secret = Secret("item", item.slime_key, "There is a key hole here, it's slimey", spell.ice_blast, "spell")
floors.append(Floor(26, great_lizard(), None, None, secret, 0))

floors.append(Floor(27, make_lizardfolk(), make_lizardfolk(), None , None, 0))

floors.append(Floor(28, make_half_dragon(), None, None, None, 3))

floors.append(Floor(29, make_half_dragon(), None, None, None, 0))

secret = Secret("item", item.dragon_key, "There is a key hole in the wall", weapon.spec_wep, "weapon")
floors.append(Floor(30, lightning_wyrmling(), None, None, secret, 0))