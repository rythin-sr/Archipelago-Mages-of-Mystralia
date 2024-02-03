import math

from worlds.generic.Rules import add_rule, add_item_rule
from typing import Set
from .Items import ItemType, all_items
from .Names.LocationNames import LocationName
from .Names.ItemNames import ItemName
from .Names.EntranceNames import EntranceName
from .Locations import LocationType
from BaseClasses import MultiWorld, CollectionState

def can_cast_spells(state: CollectionState, player: int) -> bool:
    return state.has_all([ItemName.Spellbook, ItemName.ApprenticeWand], player)

def can_perform_basic_combat(state: CollectionState, player: int) -> bool:
    return can_cast_spells(state, player) and state.has_any([ItemName.Immedi, ItemName.Actus, ItemName.Creo], player)

def can_light_torches(state: CollectionState, player: int) -> bool:
    return can_cast_spells(state, player) and state.has(ItemName.Actus, player)

def can_activate_starswitch(state: CollectionState, player: int) -> bool:
    return can_cast_spells(state, player) and state.has(ItemName.Immedi, player)

def can_walk_on_water(state: CollectionState, player: int) -> bool:
    return can_cast_spells(state, player) and state.has(ItemName.Creo, player)

def can_block_wind(state: CollectionState, player: int) -> bool:
    return can_cast_spells(state, player) and state.has(ItemName.Ego, player)

def can_walk_on_lava(state: CollectionState, player: int) -> bool:
    pass

def can_defeat_wood_wretch(state: CollectionState, player: int):
    return can_light_torches(state, player) and state.has(ItemName.MoveRune, player)

def can_detonate(state: CollectionState, player: int):
    return can_activate_starswitch(state, player) and state.has(ItemName.DetonateRune, player)

def set_entrance_rules(multiworld: MultiWorld, player: int):
    add_rule(multiworld.get_entrance(EntranceName.Haven_WestHaven_DetonateWall, player),
             lambda state: state.has(ItemName.DetonateRune, player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoods_PostCart, player),
             lambda state: can_perform_basic_combat(state, player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsPostCart_GoblinCamp, player),
             lambda state: can_light_torches(state, player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsGoblinCamp_Lardee, player),
             lambda state: can_detonate(state, player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsLardee_OldMines, player),
             lambda state: can_light_torches(state, player) and state.has(ItemName.MoveRune, player))    
     
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsLardee_DeepWoods, player),
             lambda state: can_light_torches(state, player) and state.has(ItemName.MoveRune, player))    

    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsDeepWoods_Twiggs, player),
             lambda state: state.has(ItemName.BigKey, player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsDeepWoods_BackWoods, player),
             lambda state: state.has(ItemName.MystralWoodsCleansed, player)) 
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsBackWoods_BackWoodsWest, player),
             lambda state: state.has_all(ItemName.MystralWoodsCleansed, ItemName.EclipseApproaching, player)) 
    
    add_rule(multiworld.get_entrance(EntranceName.GreyleaHamletfNorth_GreyleafHamlet, player),
             lambda state: state.has(ItemName.EclipseApproaching, player))
    
    add_rule(multiworld.get_entrance(EntranceName.GreyleaHamletfSouth_GreyleafHamlet, player),
             lambda state: state.has(ItemName.EclipseApproaching, player))
    
    add_rule(multiworld.get_entrance(EntranceName.Haven_WestHaven_DetonateWall, player),
             lambda state: can_detonate(state, player))
    
    add_rule(multiworld.get_entrance(EntranceName.RiseSouth_Rise, player),
             lambda state: can_detonate(state, player))
    
    add_rule(multiworld.get_entrance(EntranceName.Rise_RiseNorth, player),
             lambda state: state.has(ItemName.BigKey, player))
    
    add_rule(multiworld.get_entrance(EntranceName.SkyTempleFrontDoor_SkyTempleHubArea, player),
             lambda state: state.has(ItemName.BigKey, player) and state.has(ItemName.MoveRune, player))
    
    add_rule(multiworld.get_entrance(EntranceName.SkyTempleHubArea_SkyTempleHubNorth, player),
             lambda state: state.has(ItemName.BigKey, player) and can_light_torches(state, player))    
    
    add_rule(multiworld.get_entrance(EntranceName.SkyTempleHubArea_SkyTempleHubUpper, player),
             lambda state: can_detonate(state, player) and can_light_torches(state, player))
    
    add_rule(multiworld.get_entrance(EntranceName.GreyleaHamletSouth_TheHighlands, player),
             lambda state: can_detonate(state, player))    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoods_MystralMiningArea, player),
             lambda state: can_detonate(state, player))



def set_access_rules(multiworld, player):
    add_rule(multiworld.get_location(LocationName.Victory, player),
             lambda state: state.has(ItemName.DefeatSleet, player))

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
             lambda state: can_detonate(state, player))
    
    add_rule(multiworld.get_location(LocationName.WindingGlade_TeleportRunePuzzleRoom, player),
             lambda state: can_detonate(state, player))
    
    
    add_rule(multiworld.get_location(LocationName.MystralWoods_ManaLily, player),
             lambda state: can_walk_on_water(state, player))
    add_rule(multiworld.get_location(LocationName.MystralWoods_PostCart_PurpleBeadPuzzleRoom, player),
             lambda state: can_light_torches(state, player) and can_walk_on_water(state, player) and can_activate_starswitch(state, player) and can_block_wind(state, player))
    add_rule(multiworld.get_location(LocationName.MystralWoods_Lardee_MoveRune, player),
             lambda state: can_perform_basic_combat(state, player))
    add_rule(multiworld.get_location(LocationName.MystralWoods_Twiggs_LifeElixer, player),
             lambda state: can_defeat_wood_wretch(state, player))
    
    add_rule(multiworld.get_location(LocationName.GreyleafHamlet_MariesBagOfWaresResult, player),
             lambda state: state.has(ItemName.BagOfWares, player, 4))
    
    add_rule(multiworld.get_location(LocationName.TheRiseSouth_TorchPuzzleNearRopeBridges, player),
             lambda state: can_light_torches(state, player) and state.has(ItemName.MoveRune, player))
    
    add_rule(multiworld.get_location(LocationName.TheRiseNorth_RuinsTorchPuzzle, player),
             lambda state: can_light_torches(state, player) and state.has(ItemName.MoveRune, player))
    
    add_rule(multiworld.get_location(LocationName.SkyTempleFrontDoorTorchPuzzle, player),
             lambda state: can_light_torches(state, player) and state.has(ItemName.MoveRune, player))   
     
    add_rule(multiworld.get_location(LocationName.SkyTempleHubNorthTorchBehindDetonateRock, player),
             lambda state: can_detonate(state, player))   
      
    add_rule(multiworld.get_location(LocationName.SkyTempleHubPuzzleMasteryRune, player),
             lambda state: state.has(ItemName.SkyTempleTorch, player, 5))
    
    add_rule(multiworld.get_location(LocationName.SkyTempleUpperAncientLizardSleet, player),
             lambda state: can_block_wind(state, player) and state.has(ItemName.BigKey, player))
    
    add_rule(multiworld.get_location(LocationName.SkyTempleUpperSleetsRemains, player),
             lambda state: state.has(ItemName.DefeatSleet, player))
    add_rule(multiworld.get_location(LocationName.SkyTempleUpperIceLizardElixerChest, player),
             lambda state: state.has(ItemName.DefeatSleet, player))
    add_rule(multiworld.get_location(LocationName.SkyTempleUpperCelestialPuzzleNearRemains, player),
             lambda state: state.has(ItemName.DefeatSleet, player))
    add_rule(multiworld.get_location(LocationName.TheRistNorthUpperLedge_ImpactRune, player),
             lambda state: state.has(ItemName.DefeatSleet, player))
    add_rule(multiworld.get_location(LocationName.TheRise_ManaLily, player),
             lambda state: can_walk_on_water(state, player) and can_detonate(state, player))
    
    
    add_rule(multiworld.get_location(LocationName.MystralWoods_Backwoods_DetonateTorch, player),
             lambda state: can_light_torches(state, player) and can_detonate(state, player))
    add_rule(multiworld.get_location(LocationName.MystralWoods_TorchPuzzleOverchargeRune, player),
             lambda state: can_light_torches(state, player) and can_walk_on_water(state, player) and state.has(ItemName.MoveRune, player))
    
    add_rule(multiworld.get_location(LocationName.MystralWoods_SuperLardee_AuraWand, player),
             lambda state: state.has(ItemName.EclipseApproaching, player))
    add_rule(multiworld.get_location(LocationName.OldMinesLardee_PurpleBeadDetonateRock, player),
             lambda state: can_detonate(state, player))
    add_rule(multiworld.get_location(LocationName.HavenWest_RemoteDetonateRock, player),
             lambda state: can_detonate(state, player) and state.has(ItemName.ImpactRune, player))



def set_item_rules(multiworld, player):
    pass