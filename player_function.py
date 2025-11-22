import time

from weapon_function import short_sword
from spell_function import lightning_bolt_i

class Player():
    def __init__(self):
        self.hp = 10
        self.max_hp = 10

        self.ac = 2

        self.mana = 5
        self.max_mana = 5

        self.equipped_item = short_sword

        self.items = []

        self.actions = 1
        self.actions_max = 1

        self.coin = 0

        self.spell1 = lightning_bolt_i
        self.spell2 = None
        self.spell3 = None

        self.estus_count = 4
        self.estus_max = 4
        self.estus_heal = 4

        self.mana_pot_count = 1
        self.mana_pot_max = 1
        self.mana_pot_restore = 4

        # Extra weapons
        self.secondary_weapon = None
        self.tertiary_weapon = None
        self.quaternary_weapon = None

    def new_weapon(self, weapon):
        if self.secondary_weapon is None:
            self.secondary_weapon = weapon
        elif self.tertiary_weapon is None:
            self.secondary_weapon = weapon
        elif self.quaternary_weapon is None:
            self.quaternary_weapon = weapon
        else:
            self.equipped_item.info()
            self.secondary_weapon.info()
            self.tertiary_weapon.info()
            self.quaternary_weapon.info()

            inp = input("1-4 to replace a weapon: ")

            if inp == "1":
                self.equipped_item = weapon
            if inp == "2":
                self.secondary_weapon = weapon
            if inp == "3":
                self.tertiary_weapon = weapon
            if inp == "4":
                self.quaternary_weapon = weapon

    def show_inv(self):
        print()
        for i, item in enumerate(self.items, 1):
            print(f"{item.info()}")

        print(f"{self.hp} HP")
        print(f"{self.mana} Mana")
        print(f"{self.estus_count} Estus Flasks - Heals {self.estus_heal} HP")
        print(f"{self.mana_pot_count} Mana Potions - Restores {self.mana_pot_restore} Mana")
        print(f"You have {self.coin} coins")

        print("\n1. Use Estus Flask\n2. Use Mana Potion\n3. Swap weapons")
        inp = input("Choose an option: ")
        if inp == "1" and self.estus_count > 0:
            self.use_estus()
        if inp == "2" and self.mana_pot_count > 0:
            self.use_mana_pot()
        if inp == "3":
            self.swap_weapon()

        time.sleep(1)

    def use_estus(self):
        self.estus_count -= 1
        self.hp += self.estus_heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp
            print("Healed to max HP!")
        else:
            print(f"Healed {self.estus_heal} HP!")

    def use_mana_pot(self):
        self.mana_pot_count -= 1
        self.mana += self.mana_pot_restore
        if self.mana > self.max_mana:
            self.mana = self.max_mana
            print("Restored mana to max!")
        else:
            print(f"Restore {self.mana_pot_restore} mana!")

    def cast_spell(self):
        spell_chosen = 0
        while spell_chosen < 1:
            if self.spell1 is not None:
                self.spell1.info()
            if self.spell2 is not None:
                self.spell2.info()
            if self.spell3 is not None:
                self.spell3.info()
            inp = input("Choose a spell (1-3) ")
            if inp == "1" and self.spell1 is not None:
                if self.spell1.cost > self.mana:
                    print("Insufficient mana")
                    return 0, 0, 0, None
                else:
                    self.mana -= self.spell1.cost
                    return self.spell1.damage, 1, self.spell1.heal, self.spell1.damage_type  # The one is to tell the fight system that it actually worked
            if inp == "2" and self.spell2 is not None:
                if self.spell2.cost > self.mana:
                    print("Insufficient mana")
                    return 0, 0, 0, None
                else:
                    self.mana -= self.spell2.cost
                    return self.spell2.damage, 2, self.spell2.heal, self.spell2.damage_type
            if inp == "3" and self.spell3 is not None:
                if self.spell3.cost > self.mana:
                    print("Insufficient mana")
                    return 0, 0, 0, None
                else:
                    self.mana -= self.spell3.cost
                    return self.spell3.damage, 2, self.spell3.heal, self.spell2.damage_type

    def swap_weapon(self):
        swap = None

        print("1.")
        self.equipped_item.info()
        if self.secondary_weapon is not None:
            print("2.")
            self.secondary_weapon.info()
        if self.tertiary_weapon is not None:
            print("3.")
            self.tertiary_weapon.info()
        if self.quaternary_weapon is not None:
            print("4.")
            self.quaternary_weapon.info()

        inp = input("Swap to: ")
        if inp == "2" and self.secondary_weapon is not None:
            swap = self.equipped_item
            self.equipped_item = self.secondary_weapon
            self.secondary_weapon = swap
        if inp == "3" and self.tertiary_weapon is not None:
            swap = self.equipped_item
            self.equipped_item = self.tertiary_weapon
            self.tertiary_weapon = swap

    def level_up(self):
        decision = 0
        while decision == 0:
            print(f"Max HP: {self.max_hp}\nMax Mana: {self.max_mana}")
            print("You may add either 3 points to you max HP or 2 to your mana")
            inp = input("1. HP\n2. Mana\nEnter: ")
            if inp == "1":
                self.max_hp += 3
                self.hp += 3
                decision = 1
            if inp == "2":
                self.max_mana += 2
                self.mana += 2
                decision = 1
        print(f"Max HP: {self.max_hp}\nMax Mana: {self.max_mana}")

    def new_spell(self, spell):
        if self.spell1 is None:
            self.spell1 = spell
        elif self.spell2 is None:
            self.spell2 = spell
        elif self.spell3 is None:
            self.spell3 = spell
        else:
            self.spell1.info()
            self.spell2.info()
            self.spell3.info()
            inp = input("1-3 to replace a spell ")
            if inp == "1":
                self.spell1 = spell
            if inp == "2":
                self.spell2 = spell
            if inp == "3":
                self.spell3 = spell

    def upgrade_estus(self):
        decision = 0
        while decision == 0:
            print(f"You can have a max of {self.estus_max} Estus Flasks and {self.mana_pot_max} Mana Potions")
            print(f"The Estus Flask heals {self.estus_heal} and the Mana Potion restores {self.mana_pot_restore} Mana")
            inp = input("You may have one more of either, 1 for Estus, 2 for Mana: ")
            if inp == "1":
                self.estus_max += 1
                decision = 1
                self.estus_count += 1
            if inp == "2":
                self.mana_pot_max += 1
                decision = 1
                self.mana_pot_count += 1
        decision = 0
        while decision == 0:
            inp = input("Now you may make one heal/restore by 2 more points: ")
            if inp == "1":
                self.estus_heal += 2
                decision = 1
            if inp == "2":
                self.mana_pot_restore += 2
                decision = 1

player1 = Player()