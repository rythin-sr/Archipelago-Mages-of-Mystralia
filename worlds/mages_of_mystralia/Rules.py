import math

from worlds.generic.Rules import add_rule, add_item_rule
from typing import Set
from .Items import ItemType, all_items
from .Names.LocationNames import LocationName
from .Names.ItemNames import ItemName
from .Names.EntranceNames import EntranceName
from .Locations import LocationType
from BaseClasses import MultiWorld


def set_entrance_rules(multiworld: MultiWorld, player: int):
    add_rule(multiworld.get_entrance(EntranceName.Haven_WestHaven_DetonateWall, player),
             lambda state: state.has(ItemName.DetonateRune, player))

def set_access_rules(multiworld, player):
    add_rule(multiworld.get_location(LocationName.Victory, player),
             lambda state: state.has(ItemName.ManaCharm, player, 5) and state.has_all([ItemName.Spellbook, ItemName.Immedi, ItemName.Actus, ItemName.Creo, ItemName.Ego], player))

    add_rule(multiworld.get_location(LocationName.Haven_HealthFountainOne, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 24))
    add_rule(multiworld.get_location(LocationName.Haven_HealthFountainTwo, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 28))
    add_rule(multiworld.get_location(LocationName.Haven_HealthFountainThree, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 32))
    add_rule(multiworld.get_location(LocationName.Haven_HealthFountainFour, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 36))
    add_rule(multiworld.get_location(LocationName.Haven_HealthFountainFive, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 40))
    
    add_rule(multiworld.get_location(LocationName.Haven_ManaFountainOne, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 24))
    add_rule(multiworld.get_location(LocationName.Haven_ManaFountainTwo, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 28))
    add_rule(multiworld.get_location(LocationName.Haven_ManaFountainThree, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 32))
    add_rule(multiworld.get_location(LocationName.Haven_ManaFountainFour, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 36))
    add_rule(multiworld.get_location(LocationName.Haven_ManaFountainFive, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 40))
    
    
    add_rule(multiworld.get_location(LocationName.Haven_ManaLilyTwo, player),
             lambda state: state.has(ItemName.ManaLilyBulb, player))
    add_rule(multiworld.get_location(LocationName.Haven_ManaLilyThree, player),
             lambda state: state.has(ItemName.ManaLilyBulb, player, 2))
    add_rule(multiworld.get_location(LocationName.Haven_ManaLilyFour, player),
             lambda state: state.has(ItemName.ManaLilyBulb, player, 3))
    add_rule(multiworld.get_location(LocationName.Haven_ManaLilyFive, player),
             lambda state: state.has(ItemName.ManaLilyBulb, player, 4))
    
    
    add_rule(multiworld.get_location(LocationName.Haven_RandomRunePuzzleRoom, player),
             lambda state: state.has(ItemName.DetonateRune, player))
    
    add_rule(multiworld.get_location(LocationName.WindingGlade_TeleportRunePuzzleRoom, player),
             lambda state: state.has(ItemName.DetonateRune, player))
    
    
    add_rule(multiworld.get_location(LocationName.MystralWoods_ManaLily, player),
             lambda state: state.has(ItemName.Creo, player))


def set_item_rules(multiworld, player):
    pass