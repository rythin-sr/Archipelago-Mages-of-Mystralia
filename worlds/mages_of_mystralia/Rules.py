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
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoods_PostCart, player),
             lambda state: state.has_all([ItemName.Spellbook, ItemName.ApprenticeWand], player) and state.has_any([ItemName.Immedi, ItemName.Actus, ItemName.Creo], player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsPostCart_GoblinCamp, player),
             lambda state: state.has_all([ItemName.Spellbook, ItemName.ApprenticeWand, ItemName.Immedi], player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsGoblinCamp_Lardee, player),
             lambda state: state.has(ItemName.DetonateRune, player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsLardee_OldMines, player),
             lambda state: state.has_all([ItemName.Actus, ItemName.MoveRune], player))    
     
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsLardee_DeepWoods, player),
             lambda state: state.has_all([ItemName.Actus, ItemName.MoveRune], player)) 

    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsDeepWoods_Twiggs, player),
             lambda state: state.has([ItemName.BigKey], player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsDeepWoods_Twiggs, player),
             lambda state: state.can_reach(LocationName.MystralWoods_Twiggs_LifeElixer, 'Location', player)) 
    
    add_rule(multiworld.get_entrance(EntranceName.Haven_WestHaven_DetonateWall, player),
             lambda state: state.has_all([ItemName.Spellbook, ItemName.ApprenticeWand] , player) and state.has(ItemName.Immedi, player))


def set_access_rules(multiworld, player):
    add_rule(multiworld.get_location(LocationName.Victory, player),
             lambda state: state.has(ItemName.ManaCharm, player, 5) and state.has_all([ItemName.Spellbook, ItemName.ApprenticeWand ,ItemName.Immedi, ItemName.Actus, ItemName.Creo, ItemName.Ego], player))

    add_rule(multiworld.get_location(LocationName.Haven_UpgradeFountainOne, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 4))
    add_rule(multiworld.get_location(LocationName.Haven_UpgradeFountainTwo, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 8))
    add_rule(multiworld.get_location(LocationName.Haven_UpgradeFountainThree, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 12))
    add_rule(multiworld.get_location(LocationName.Haven_UpgradeFountainFour, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 16))
    add_rule(multiworld.get_location(LocationName.Haven_UpgradeFountainFive, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 20))
    add_rule(multiworld.get_location(LocationName.Haven_UpgradeFountainSix, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 24))
    add_rule(multiworld.get_location(LocationName.Haven_UpgradeFountainSeven, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 28))
    add_rule(multiworld.get_location(LocationName.Haven_UpgradeFountainEight, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 32))
    add_rule(multiworld.get_location(LocationName.Haven_UpgradeFountainNine, player),
             lambda state: state.has(ItemName.Purple_Soulbead, player, 36))
    add_rule(multiworld.get_location(LocationName.Haven_UpgradeFountainTen, player),
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
    add_rule(multiworld.get_location(LocationName.MystralWoods_PostCart_PurpleBeadPuzzleRoom, player),
             lambda state: state.has_all([ItemName.Creo, ItemName.Immedi, ItemName.Ego, ItemName.Actus], player))
    add_rule(multiworld.get_location(LocationName.MystralWoods_Lardee_MoveRune, player),
             lambda state: state.has(ItemName.Actus, player))
    add_rule(multiworld.get_location(LocationName.MystralWoods_Twiggs_LifeElixer, player),
             lambda state: state.has_all([ItemName.Actus, ItemName.MoveRune, ItemName.Immedi], player))

def set_item_rules(multiworld, player):
    pass