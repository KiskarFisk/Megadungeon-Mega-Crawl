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

lvl1_spell = [heal_spell_i, fire_bolt_i, dual_spell_i, lightning_bolt_ii]

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