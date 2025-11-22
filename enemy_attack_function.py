import random


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

# Tier 4

tremble = Attack("Tremble", 100, 0)
cower = Attack("Cower", 100, 0)
spear = Attack("Spear", 65, random.randint(9,13))
stab3 = Attack("Stab", 70, 9)
sword3 = Attack("Sword", 70, 14)
ash_gust = Attack("Gust of Ash", 80, 10)