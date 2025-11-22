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

lvl1_weapon = [long_sword, short_sword2, short_sword3, flail, flaming_short_sword, long_sword2, frozen_short_sword]

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

# T4

t4spec = Weapon("Ashen Sword", 23, 70, "normal", 0)