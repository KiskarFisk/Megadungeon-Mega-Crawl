import pickle as pkl

from player_function import player1
import floor_handle

def save():
    with open("save.pkl", "wb") as f:
        pkl.dump((
            floor_handle.floor_number,
            player1.hp,
            player1.max_hp,
            player1.mana,
            player1.max_mana,
            player1.equipped_item,
            player1.items,
            player1.actions,
            player1.actions_max,
            player1.coin,
            player1.spell1,
            player1.spell2,
            player1.spell3,
            player1.estus_count,
            player1.estus_max,
            player1.estus_heal,
            player1.mana_pot_count,
            player1.mana_pot_max,
            player1.mana_pot_restore,
            player1.secondary_weapon,
            player1.tertiary_weapon,
            player1.quaternary_weapon
            ),
        f
        )

def load():
    with open("save.pkl", "rb") as f:
        (floor_handle.floor_number,
        player1.hp,
        player1.max_hp,
        player1.mana,
        player1.max_mana,
        player1.equipped_item,
        player1.items,
        player1.actions,
        player1.actions_max,
        player1.coin,
        player1.spell1,
        player1.spell2,
        player1.spell3,
        player1.estus_count,
        player1.estus_max,
        player1.estus_heal,
        player1.mana_pot_count,
        player1.mana_pot_max,
        player1.mana_pot_restore,
        player1.secondary_weapon,
        player1.tertiary_weapon,
        player1.quaternary_weapon
         ) = pkl.load(f)