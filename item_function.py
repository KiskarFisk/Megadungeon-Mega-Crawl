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

lvl1_item = [poison, protection]