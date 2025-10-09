import math
import random
import time

from colorama import Fore, Style, init
init()

floor = 1
floors = []

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
                    if item.name == self.item:
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
        global player_items
        if self.prize_type == "item":
            player_items.append(self.prize)
            print(f"You got {self.prize.name}")
        if self.prize_type == "weapon":
            print(f"You got {self.prize.name}")
            new_weapon(self.prize)
        if self.prize_type == "spell":
            print(f"You got {self.prize.name}")
            new_spell(self.prize)

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
            new_weapon(self.weapon)
            coin -= self.weapon.coin
        if inp == "2" and coin >= self.item.coin:
            player_items.append(self.item)
            coin -= self.item.coin
        if inp == "3" and coin >= self.spell.coin:
            new_spell(self.spell)
            coin -= self.spell.coin

class Spell:
    def __init__(self, name, cost, damage, heal, damage_type, coin):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.heal = heal
        self.damage_type = damage_type
        self.coin = coin

    def info(self):
        print(f"{self.name} - Costs {self.cost} mana, {self.coin} coins")
        if self.damage > 0:
            print(f"Deals {self.damage} {self.damage_type} damage")
        if self.heal > 0:
            print(f"Heals {self.heal} HP")

lightning_bolt_i = Spell("Lightning Bolt I", 2, 5, 0, "lightning", 4)
lightning_bolt_ii = Spell("Lightning Bolt II", 3, 7, 0, "lightning", 10)

lightning_ball = Spell("Lightning Ball", 5, 14, 0, "lightning", 0)

heal_spell_i = Spell("Heal Spell I", 2, 0, 3, None, 6)
fire_bolt_i = Spell("Fire Bolt I", 3, 8, 0, "fire", 12)
dual_spell_i = Spell("Dual Spell I", 2, 2, 2, None, 5)

### Tier 2

lightning_bolt_iii = Spell("Lightning Bolt III", 4, 10, 0, "lightning", 14)
heal_spell_ii = Spell("Heal Spell II", 4, 0, 8, None, 15)
fire_bolt_ii = Spell("Fire Bolt II", 6, 15, 0, "fire", 21)
freeze = Spell("Freeze", 3, 8, 0, "ice", 10)
corrupt = Spell("Corrupt", 7, 23, 0, "dark", 32)
dual_spell_ii = Spell("Dual Spell II", 4, 5, 5, None, 12)

great_dual_spell = Spell("Greater Dual Spell", 6, 10, 10, None, 0)

t2_spell = [lightning_bolt_iii, heal_spell_ii, fire_bolt_ii, freeze, dual_spell_ii]

### T3

lightning_bolt_iv = Spell("Lightning Bolt IV", 5, 14, 0, "lightning", 20)
heal_spell_iii = Spell("Heal Spell III", 5, 0, 13, None, 21)
fire_bolt_iii = Spell("Fire Bolt III", 9, 22, 0, "fire", 24)
freeze_ii = Spell("Freeze II", 3, 11, 0, "ice", 16)
corrupt_ii = Spell("Corrupt II", 10, 35, 0, "dark", 50)
divine_smite = Spell("Divine Blast", 3, 11, 0, "holy", 10)

ice_blast = Spell("Ice Blast", 4, 14, 0, "ice", 0)

t3_spell = [lightning_bolt_iv, heal_spell_iii, fire_bolt_iii, freeze_ii, corrupt_ii, divine_smite]

class Weapon:
    def __init__(self, name, damage, to_hit, damage_type, coin):
        self.name = name
        self.damage = damage
        self.to_hit = to_hit
        self.damage_type = damage_type
        self.coin = coin

    def info(self):
        print(f"{self.name} - {self.to_hit}% to hit, {self.damage} {self.damage_type} damage, {self.coin} coins")

short_sword = Weapon("Short Sword", 3, 70, "normal", 5)
flaming_short_sword = Weapon("Flaming Short Sword", 3, 70, "fire", 7)
frozen_short_sword = Weapon("Frozen Short Sword", 3, 70, "ice", 6)
short_sword2 = Weapon("Short Sword +1", 5, 70, "normal", 8)
short_sword3 = Weapon("Short Sword +2", 7, 70, "normal", 10)
long_sword = Weapon("Long Sword", 5, 75, "normal", 9)
long_sword2 = Weapon("Long Sword +1", 8, 75, "normal", 11)

flail = Weapon("Flail", 12, 40, "normal", 10)

ishmar_blade = Weapon("Ishmar's Blade", 8, 70, "fire", 0)
longinus_spear = Weapon("Spear of Longinus", 11, 75, "holy", 777)

### Tier 2 weapons

harpe = Weapon("Harpe", 8, 70, "normal", 12)
harpe2 = Weapon("Harpe +1", 10, 70, "normal", 15)
harpe3 = Weapon("Harpe +2", 13, 70, "normal", 17)
flaming_harpe = Weapon("Flaming Harpe", 8, 70, "fire", 16)
electric_harpe = Weapon("Electrified Harpe", 9, 70, "lightning", 17)

spatha = Weapon("Spatha", 7, 75, "normal", 11)
dark_spatha = Weapon("Corrupted Spatha", 10, 75, "dark", 14)

axe = Weapon("Axe", 12, 60, "normal", 14)
bless_axe = Weapon("Glowing Axe", 13, 60, "holy", 20)

lvl_2_weapon = [harpe, harpe2, harpe3, flaming_harpe, electric_harpe, spatha, dark_spatha, axe, bless_axe]

## T3

axe2 = Weapon("Axe +1", 15, 60, "normal", 17)
flaming_axe = Weapon("Flaming Axe", 15, 60, "fire", 19)

spatha2 = Weapon("Spatha +1", 10, 75, "normal", 15)
spatha3 = Weapon("Spatha +2", 13, 75, "normal", 18)

mace = Weapon("Mace", 17, 52, "normal", 15)
enhanced_mace = Weapon("Enhanced Mace", 21, 65, "normal", 32)

great_hammer = Weapon("Great Hammer", 20, 60, "normal", 22)

spec_wep = Weapon("Sword of the Small Hero", 18, 65, "holy", 0)
moss_infest_sword = Weapon("Moss Infested Sword", 14, 70, "normal", 0)

t3_weapon = [axe2, flaming_axe, spatha2, spatha3, mace, enhanced_mace, great_hammer]

class Item:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin

    def info(self):
        return f"{self.name} - {self.coin} coins"

poison = Item("Vial of Poison", 8)
shredded_book = Item("Shredded Book", 0)
acid = Item("Vial of acid", 6)
chocolate = Item("A Bar of Chocolate", 5)
protection = Item("A protection talisman", 12)

## Tier 2

rat_crown = Item("Rat Crown", 0)
slime_key = Item("Slimey Key", 0)
anti_mold = Item("Anti-Mold Spray", 10)

t2_item = [protection, acid, anti_mold]

## Tier 3

dragon_key = Item("Dragon Scale Key", 0)

t3_item = [protection]

class Attack:
    def __init__(self, name, to_hit, damage):
        self.name = name
        self.to_hit = to_hit
        self.damage = damage

stab = Attack("Stab", 70, 3)
bite1 = Attack("Bite", 65, 3)
bite2 = Attack("Bite", 65, 6)
sword1 = Attack("Sword", 70, 4)
spit_flame = Attack("Spit Flame", 60, 6)
infest = Attack("Infest", 40, 7)
slime = Attack("Slime", 60, 5)
shocker1 = Attack("Electric Shock", 50, 7)

# T2

infest2 = Attack("Infest", 40, 8)
strangle = Attack("Strangle", 50, 6)
claw = Attack("Claw", 70, 4)
smash = Attack("Smash", 60, 7)
infest3 = Attack("Infest", 40, 11)

# T3

stab2 = Attack("Stab", 70, 6)
wind_gust = Attack("Wind Gust", 50, 12)
sword2 = Attack("Sword", 70, 9)
lightning_breath = Attack("Lightning Breath", 60, 14)
claw2 = Attack("Claw", 70, 8)

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
        for item in player_items:
            if item == protection:
                ac += 2
        global floor_number
        global estus_count
        global estus_max
        global mana_pot_count
        global mana_pot_mox
        global player_hp, player_actions_max
        global player_mana, estus_max, player_max_mana
        shop = Shop(self.shop)
        if floor_number % 3 == 0 and floor_number > 1:
            print(Fore.GREEN + "Estus Flasks and Mana Potions restored!" + Style.RESET_ALL)
            estus_count = estus_max
            mana_pot_count = mana_pot_mox
        if floor_number % 2 == 0 and floor_number > 1:
            level_up()
        if floor_number % 5 == 0:
            print("HP and Mana restored!")
            player_hp = player_max_hp
            player_mana = player_max_mana
        if floor_number == 6:
            print("You get another action")
            player_actions_max += 1
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
                    upgrade_estus()
                return
            if inp == "5":
                show_inv()
            if inp == "6":
                if spell1 is not None:
                    print(f"{spell1.info()}")
                if spell2 is not None:
                    print(spell2.info())
                if spell3 is not None:
                    spell3.info()
            if inp == "7":
                swap_weapon()

    def fight(self):
        global player_hp
        global coin
        dmg_red = 0
        while self.defeated == 0:
            dmg_red = 0
            if player_hp <= 0:
                print("\nYou are defeated...")
                quit()

            player_actions = player_actions_max
            print("Enemies:")
            if self.enemy1 is not None:
                self.enemy1.info()
            if self.enemy2 is not None:
                self.enemy2.info()

            while player_actions > 0:
                print(f"You have {player_hp} HP and {player_mana} Mana")
                print(f"Remaining actions: {player_actions}")
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
                    if rum <= player_equipped_item.to_hit:
                        damage = damage_modifier(target, player_equipped_item.damage_type, player_equipped_item.damage)
                        target.HP -= damage
                        print(f"Attacked {target.name} for {damage} damage")
                        time.sleep(1)
                        player_actions -= 1
                    else:
                        print(f"Missed {target.name}")
                        time.sleep(1)
                        player_actions -= 1
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
                    damage, passes, heal, type = cast_spell()
                    if passes > 0:
                        player_actions -= 1
                        if damage > 0:
                            damage = damage_modifier(target, type, damage)
                            print(f"You deal {damage} damage to {target.name}")
                            target.HP -= damage
                        if heal > 0:
                            print(f"You heal {heal} HP")
                            player_hp += heal

                if inp == "3": # defending
                    print("You brace yourself")
                    dmg_red = ac
                    print(f"Your damage reduction is {dmg_red}")
                    player_actions -= 1

                if inp == "4":
                    show_inv()

            if self.enemy1 is not None:
                if self.enemy1.HP > 0:
                    damage = self.enemy1.fight()
                    if damage is not None:
                        damage -= dmg_red
                        if damage > 0:
                            player_hp -= damage
                    else:
                        print(f"{self.enemy1.name} missed")

            if self.enemy2 is not None:
                if self.enemy2.HP > 0:
                    damage = self.enemy2.fight()
                    if damage is not None:
                        damage -= dmg_red
                        if damage > 0:
                            player_hp -= damage
                    else:
                        print(f"{self.enemy2.name} missed")

            if self.enemy1 is not None:
                if self.enemy1.HP <= 0:
                    print(f"Defeated {self.enemy1.name}")
                    print(f"Gained {self.enemy1.coin} coin")
                    coin += self.enemy1.coin
                    if self.enemy1.drop is not None:
                        print(f"They also dropped {self.enemy1.drop.info()}")
                        player_items.append(self.enemy1.drop)
                    self.enemy1 = None

            if self.enemy2 is not None:
                if self.enemy2.HP <= 0:
                    print(f"Defeated {self.enemy2.name}")
                    print(f"Gained {self.enemy2.coin} coin")
                    coin += self.enemy2.coin
                    if self.enemy2.drop is not None:
                        print(f"They also dropped {self.enemy2.drop.info()}")
                        player_items.append(self.enemy2.drop)
                    self.enemy2 = None

            if self.enemy1 is None and self.enemy2 is None:
                self.defeated = 1

def upgrade_estus():
    global estus_max
    global mana_pot_mox
    global estus_heal
    global mana_pot_restore
    global estus_count
    global mana_pot_count
    decision = 0
    while decision == 0:
        print(f"You can have a max of {estus_max} Estus Flasks and {mana_pot_mox} Mana Potions")
        print(f"The Estus Flask heals {estus_heal} and the Mana Potion restores {mana_pot_restore} Mana")
        inp = input("You may have one more of either, 1 for Estus, 2 for Mana: ")
        if inp == "1":
            estus_max += 1
            decision = 1
            estus_count += 1
        if inp == "2":
            mana_pot_mox += 1
            decision = 1
            mana_pot_count += 1
    decision = 0
    while decision == 0:
        inp = input("Now you may make one heal/restore by 2 more points: ")
        if inp == "1":
            estus_heal += 2
            decision = 1
        if inp == "2":
            mana_pot_restore += 2
            decision = 1

def make_slime_mold():
    return Enemy("Slime Mold", 12, "fire", "normal", 1, infest, None, None, 9, None)
def make_mini_luna():
    return Enemy("Mini Luna", 7, "holy", "dark", 1, bite1, None, None, 1, None)
def make_giant_snail():
    return Enemy("Giant Snail", 12, "lightning", "fire", 1, slime, None, None, 4, None)
def make_lightning_rat():
    return Enemy("Lightning Rat", 8, None, "lightning", 1, shocker1, bite1, None, 4, None)
def make_infected_mini_luna():
    return Enemy("Slime Mold Infected Mini Luna", 23, "lightning", "fire", 1, bite2, infest, None, 8, chocolate)

enemy1 = Enemy("Test", 50, None, None, 1, bite1, None, None, 2, None)

giant_rat = Enemy("Giant Rat", 5, None, None, 1, bite1, None, None, 2, None)
floors.append(Floor(1, giant_rat, None, None, None, 0))

secret = Secret("creative", "push", "The stones of the wall are fairly normal though ones seems to jut out more than the others", ishmar_blade, "weapon")
giant_rat = Enemy("Giant Rat", 5, None, None, 1, bite1, None, None, 2, None)
thief = Enemy("Thief", 6, None, None, 1, stab, None, None, 5, None)
floors.append(Floor(2, giant_rat, thief, None, secret, 0))

thief = Enemy("Thief", 6, None, None, 1, stab, None, None, 5, None)
flaming_rat = Enemy("Flaming Rat", 5, None, "fire", 1, bite1, spit_flame, None, 2, None)
floors.append(Floor(3, thief, flaming_rat, None, None, 1))

floors.append(Floor(4, make_mini_luna(), make_mini_luna(), None, None, 0))

slime_mold = Enemy("Slime Mold", 12, "fire", "normal", 1, infest, None, None, 9, shredded_book)
floors.append(Floor(5, slime_mold, None, None, None, 1))

giant_snail = Enemy("Giant Snail", 12, "lightning", "fire", 1, slime, None, None, 4, None)
flaming_rat = Enemy("Flaming Rat", 5, None, "fire", 1, bite1, spit_flame, None, 2, None)
floors.append(Floor(6, giant_snail, flaming_rat, None, None, 0))

mini_luna = Enemy("Mini Luna", 7, None, None, 1, bite1, None, None, 1, None)
giant_snail = Enemy("Giant Snail", 12, "lightning", "fire", 1, slime, None, None, 4, None)
floors.append(Floor(7, mini_luna, giant_snail, None, None, 0))

secret = Secret("attack", None, "A portion of the wall is cracked", lightning_ball, "spell")
floors.append(Floor(8, make_slime_mold(), make_mini_luna(), None, secret, 1))

floors.append(Floor(9, make_lightning_rat(), make_lightning_rat(), None, None, 0))

floors.append(Floor(10, make_infected_mini_luna(), None, None, None, 1))

# T2

def make_moldequin():
    return Enemy("Moldequin", 20, "lightning", "fire", 1, infest2, None, None, 7, None)
def make_mold_beast():
    return Enemy("Mold Beast", 28, "lightning", "fire", 1, infest2, claw, bite2, 8, None)
def make_rat_infect():
    return Enemy("Giant Infested Rat", 37, "lightning", "fire", 2, bite2, infest2, None, 12, rat_crown)
def make_statue():
    return Enemy("Infested Statue", 34, "lightning", "fire", 1, smash, infest, None, 9, None)
def make_great_mold():
    return Enemy("Massive Slime Mold Growth", 57, "lightning", "fire", 1, infest3, None, None, 16, slime_key)

floors.append(Floor(11, make_moldequin(), None, None, None, 0))

floors.append(Floor(12, make_moldequin(), make_moldequin(), None, None, 2))

secret = Secret("item", shredded_book, "There is a whole in the wall, large enough to place an object inside, there are strange symbols around it.", longinus_spear, "weapon")
floors.append(Floor(13, make_mold_beast(), None, None, secret, 0))

floors.append(Floor(14, make_moldequin(), make_mold_beast(), None, None, 0))

floors.append(Floor(15, make_rat_infect, None, None, None, 0))

floors.append(Floor(16, make_mold_beast(), make_mold_beast(), None, None, 2))

secret = Secret("creative", "pull", "There is a torch on the wall lower than the rest.", great_dual_spell, "spell")
floors.append(Floor(17, make_statue(), None, None, secret, 0))

floors.append(Floor(18, make_mold_beast(), make_statue(), None, None, 0))

floors.append(Floor(19, make_statue(), make_statue(), None, None, 2))

floors.append(Floor(20, make_great_mold(), make_statue(), None, None, 0))

# Tier 3

def make_kobold():
    return Enemy("Kobold", 28, "ice", "lightning", 1, stab2, None, None, 9, None)
def make_fly_kobold():
    return Enemy("Flying Kobold", 33, "ice", "lightning", 1, stab2, wind_gust, None, 7, None)
def make_lizardfolk():
    return Enemy("Lizardfolk", 40, "ice", "lightning", 1, sword2, stab2, None, 11, None)
def great_lizard():
    return Enemy("Great Lizardfolk", 58, "ice", "lightning", 2, sword2, None, None, 14, None)
def make_half_dragon():
    return Enemy("Half-Dragon", 54, "ice", "lightning", 1, lightning_breath, claw2, None, 4, None)
def lightning_wyrmling():
    return Enemy("Young Blue Dragon", 78, "ice", "lightning", 1, lightning_breath, claw2, None, 30, dragon_key)

secret = Secret("item", anti_mold, "There is an awful growth of mold on the wall", moss_infest_sword, "weapon")
floors.append(Floor(21, make_kobold(), None, None, secret, 3))

floors.append(Floor(22, make_kobold(), make_kobold(), None, None, 0))

secret = Secret("item", chocolate, "There is one of those awful Luna things growing on the wall", protection, "item")
floors.append(Floor(23, make_fly_kobold(), make_fly_kobold(), None, secret, 0))

floors.append(Floor(24, make_lizardfolk(), make_fly_kobold(), None, None, 3))

floors.append(Floor(25, make_lizardfolk(), make_lizardfolk(), None, None, 0))

secret = Secret("item", slime_key, "There is a key hole here, it's slimey", ice_blast, "spell")
floors.append(Floor(26, great_lizard(), None, None, secret, 0))

floors.append(Floor(27, make_lizardfolk(), make_lizardfolk(), None , None, 0))

floors.append(Floor(28, make_half_dragon(), None, None, None, 3))

floors.append(Floor(29, make_half_dragon(), None, None, None, 0))

secret = Secret("item", dragon_key, "There is a key hole in the wall", spec_wep, "weapon")
floors.append(Floor(30, lightning_wyrmling(), None, None, secret, 0))

player_hp = 10
ac = 2
player_max_hp = 10
player_mana = 5
player_max_mana = 5
player_equipped_item = short_sword
player_items = []
player_actions = 1
player_actions_max = 1
coin = 0

secondary_weapon = None
tertiary_weapon = None
quaternary_weapon = None

def new_weapon(weapon):
    global player_equipped_item
    global secondary_weapon
    global tertiary_weapon
    global quaternary_weapon

    if secondary_weapon is None:
        secondary_weapon = weapon
    elif tertiary_weapon is None:
        tertiary_weapon = weapon
    elif quaternary_weapon is None:
        quaternary_weapon = weapon
    else:
        player_equipped_item.info()
        secondary_weapon.info()
        tertiary_weapon.info()
        quaternary_weapon.info()
        inp = input("1-4 to replace a weapon")
        if inp == "1":
            player_equipped_item = weapon
        if inp == "2":
            secondary_weapon = weapon
        if inp =="3":
            tertiary_weapon = weapon
        if inp == "4":
            quaternary_weapon = weapon

def swap_weapon():
    global player_equipped_item
    global secondary_weapon
    global tertiary_weapon
    global quaternary_weapon
    swap = None

    print("1.")
    player_equipped_item.info()
    if secondary_weapon is not None:
        print("2.")
        secondary_weapon.info()
    if tertiary_weapon is not None:
        print("3.")
        tertiary_weapon.info()
    if quaternary_weapon is not None:
        print("4.")
        quaternary_weapon.info()

    inp = input("Swap to: ")
    if inp == "2" and secondary_weapon is not None:
        swap = player_equipped_item
        player_equipped_item = secondary_weapon
        secondary_weapon = swap
    if inp == "3" and tertiary_weapon is not None:
        swap = player_equipped_item
        player_equipped_item = tertiary_weapon
        tertiary_weapon = swap

spell1 = lightning_bolt_i
spell2 = None
spell3 = None

def new_spell(spell):
    global spell1
    global spell2
    global spell3

    if spell1 is None:
        spell1 = spell
    elif spell2 is None:
        spell2 = spell
    elif spell3 is None:
        spell3 = spell
    else:
        spell1.info()
        spell2.info()
        spell3.info()
        inp = input("1-3 to replace a spell ")
        if inp == "1":
            spell1 = spell
        if inp == "2":
            spell2 = spell
        if inp == "3":
            spell3 = spell

estus_count = 4
estus_max = 4
estus_heal = 4

mana_pot_count = 1
mana_pot_mox = 1
mana_pot_restore = 4

def cast_spell():
    global spell1
    global spell2
    global spell3
    global player_mana
    spell_chosen = 0
    while spell_chosen < 1:
        if spell1 is not None:
            spell1.info()
        if spell2 is not None:
            spell2.info()
        if spell3 is not None:
            spell3.info()
        inp = input("Choose a spell (1-3) ")
        if inp == "1" and spell1 is not None:
            if spell1.cost > player_mana:
                print("Insufficient mana")
                return 0, 0, 0, None
            else:
                player_mana -= spell1.cost
                return spell1.damage, 1, spell1.heal, spell1.damage_type # The one is to tell the fight system that it actually worked
        if inp == "2" and spell2 is not None:
            if spell2.cost > player_mana:
                print("Insufficient mana")
                return 0, 0, 0, None
            else:
                player_mana -= spell2.cost
                return spell2.damage, 2, spell2.heal, spell2.damage_type
        if inp == "3" and spell3 is not None:
            if spell3.cost > player_mana:
                print("Insufficient mana")
                return 0, 0, 0, None
            else:
                player_mana -= spell3.cost
                return spell3.damage, 2, spell3.heal, spell2.damage_type

def choose_item():
    global player_items

    for i, item in enumerate(player_items, 1):
        print(f"{i}, {item.info()}")

        inp = input("Pick an item, use accurate case: ")

        for item in player_items:
            if item.name == inp:
                thing = item
                return thing

def show_inv():
    global player_items
    global estus_count
    global mana_pot_count
    global estus_heal
    global mana_pot_restore
    global coin

    print()
    for i, item in enumerate(player_items, 1):
        print(f"{item.info()}")  # assuming item.info() returns a string

    print(f"{player_hp} HP")
    print(f"{player_mana} Mana")
    print(f"{estus_count} Estus Flasks - Heals {estus_heal} HP")
    print(f"{mana_pot_count} Mana Potions - Restores {mana_pot_restore} Mana")
    print(f"You have {coin} coins")

    print("\n1. Use Estus Flask\n2. Use Mana Potion\n3. Swap weapons")
    inp = input("Choose an option: ")
    if inp == "1" and estus_count > 0:
        use_estus()
    if inp == "2" and mana_pot_count > 0:
        use_mana_pot()
    if inp == "3":
        swap_weapon()

    time.sleep(1)

def use_estus():
    global estus_count
    global estus_max
    global estus_heal
    global player_hp

    estus_count -= 1
    player_hp += estus_heal
    if player_hp > player_max_hp:
        player_hp = player_max_hp
        print("Healed to max HP!")
    else:
        print(f"Healed {estus_heal} HP!")

def use_mana_pot():
    global mana_pot_count
    global mana_pot_restore
    global player_mana
    global player_max_mana

    mana_pot_count -= 1
    player_mana += mana_pot_restore
    if player_mana > player_max_mana:
        player_mana = player_max_mana
        print("Restored mana to max!")
    else:
        print(f"Restore {mana_pot_restore} mana!")

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

lvl1_weapon = [long_sword, short_sword2, short_sword3, flail, flaming_short_sword, long_sword2, frozen_short_sword]
lvl1_item = [poison, protection]
lvl1_spell = [heal_spell_i, fire_bolt_i, dual_spell_i, lightning_bolt_ii]

def level_up():
    global player_max_hp
    global player_max_mana
    decision = 0
    while decision == 0:
        print(f"Max HP: {player_max_hp}\nMax Mana: {player_max_mana}")
        print("You may add either 3 points to you max HP or 2 to your mana")
        inp = input("1. HP\n2. Mana\nEnter: ")
        if inp == "1":
            player_max_hp += 3
            decision = 1
        if inp == "2":
            player_max_mana += 2
            decision = 1
    print(f"Max HP: {player_max_hp}\nMax Mana: {player_max_mana}")

print("MDMC 0.3.0")

floor_number = 1
while floor_number < len(floors) and player_hp > 0:
    floor = floors[floor_number - 1]
    floor.running()
