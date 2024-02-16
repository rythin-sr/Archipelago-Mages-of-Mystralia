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
    return can_cast_spells(state, player) and state.has_all([ItemName.Creo, ItemName.Gaea_Essence], player)

def can_defeat_wood_wretch(state: CollectionState, player: int) -> bool:
    return can_light_torches(state, player) and state.has(ItemName.MoveRune, player)

def can_detonate(state: CollectionState, player: int) -> bool:
    return can_activate_starswitch(state, player) and state.has(ItemName.DetonateRune, player)


def set_entrance_rules(multiworld: MultiWorld, player: int):
    add_rule(multiworld.get_entrance(EntranceName.Haven_WestHaven_DetonateWall, player),
             lambda state: can_detonate(state, player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoods_PostCart, player),
             lambda state: can_perform_basic_combat(state, player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsPostCart_GoblinCamp, player),
             lambda state: can_activate_starswitch(state, player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsGoblinCamp_Lardee, player),
             lambda state: can_detonate(state, player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsLardee_OldMines, player),
             lambda state: can_light_torches(state, player) and state.has(ItemName.MoveRune, player))    
     
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsLardee_DeepWoods, player),
             lambda state: can_light_torches(state, player) and state.has(ItemName.MoveRune, player))    

    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsDeepWoods_Twiggs, player),
             lambda state: state.has(ItemName.BigKey, player, 1))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsDeepWoods_BackWoods, player),
             lambda state: state.has(ItemName.MystralWoodsCleansed, player)) 
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsBackWoods_BackWoodsWest, player),
             lambda state: state.has(ItemName.EclipseApproaching, player)) 
    
    add_rule(multiworld.get_entrance(EntranceName.GreyleaHamletfNorth_GreyleafHamlet, player),
             lambda state: state.has(ItemName.EclipseApproaching, player))
    
    add_rule(multiworld.get_entrance(EntranceName.Rise_RiseNorth, player),
             lambda state: state.has(ItemName.BigKey, player, 2))
    
    add_rule(multiworld.get_entrance(EntranceName.SkyTempleFrontDoor_SkyTempleHubArea, player),
             lambda state: state.has(ItemName.BigKey, player, 1) and can_light_torches(state, player) and state.has(ItemName.MoveRune, player))
    
    add_rule(multiworld.get_entrance(EntranceName.SkyTempleHubArea_SkyTempleHubNorth, player),
             lambda state: state.has(ItemName.BigKey, player, 1))
    
    add_rule(multiworld.get_entrance(EntranceName.RiseUpperLedges_SkyTemplePostSleet, player),
             lambda state: state.has_all([ItemName.MoveRune, ItemName.ImpactRune], player))
    
    add_rule(multiworld.get_entrance(EntranceName.GreyleaHamletSouth_TheHighlands, player),
             lambda state: can_detonate(state, player))
    
    add_rule(multiworld.get_entrance(EntranceName.MystralWoods_MystralMiningArea, player),
             lambda state: can_detonate(state, player))
    add_rule(multiworld.get_entrance(EntranceName.Graveyard_TombOfTheMageKing, player),
             lambda state: can_light_torches and can_activate_starswitch and state.has(ItemName.MoveRune, player))
    add_rule(multiworld.get_entrance(EntranceName.TombOfTheMageKing_TombOfTheMageKingSecondLevel, player),
             lambda state: state.has(ItemName.BigKey, player, 2)) 
    add_rule(multiworld.get_entrance(EntranceName.TombOfTheMageKingSecondLevel_TombOfTheMageKingThirdLevel, player),
             lambda state: state.has(ItemName.BigKey, player, 1)) 
    add_rule(multiworld.get_entrance(EntranceName.Highlands_HighlandsUpper, player),
             lambda state: state.has(ItemName.BigKey, player, 1)) 
    add_rule(multiworld.get_entrance(EntranceName.GreyleafHamlet_GreyleafHamletCaves, player),
             lambda state: can_light_torches(state, player) and can_detonate(state, player) and state.has_all([ItemName.MoveRune, ItemName.ImpactRune, ItemName.DefeatGhostQueen], player) and state.has(ItemName.BigKey, player, 1)) 
    add_rule(multiworld.get_entrance(EntranceName.Highlands_SunkenQuarry, player),
             lambda state: can_walk_on_water(state, player) and state.has_all([ItemName.MoveRune, ItemName.Aura_Essence], player)) 
    add_rule(multiworld.get_entrance(EntranceName.MystralWoodsMiningArea_OldMines, player),
             lambda state: can_block_wind(state, player) and state.has(ItemName.Aqua_Essence, player)) 
    add_rule(multiworld.get_entrance(EntranceName.OldMinesKeyDoor, player),
             lambda state: state.has(ItemName.BigKey, player, 1)) 
    add_rule(multiworld.get_entrance(EntranceName.RiseUpperLedges_LavaGrotto, player),
             lambda state: can_walk_on_lava(state, player)) 
    add_rule(multiworld.get_entrance(EntranceName.Haven_WindingGlade, player),
             lambda state: state.has(ItemName.BrokenPortalStone, player))
    add_rule(multiworld.get_entrance(EntranceName.Rise_DarkTower, player),
             lambda state: state.has(ItemName.DefeatGhostQueen, player))
    
    if False:
        add_rule(multiworld.get_entrance(EntranceName.Highlands_Graveyard, player),
             lambda state: state.has(ItemName.Badge, player))


def set_access_rules(multiworld, player):
    add_rule(multiworld.get_location(LocationName.DarkTowerAerie, player),
             lambda state: state.can_reach(LocationName.GreyleafHamletCave_Blasius, 'Location', player) and 
             state.can_reach(LocationName.SunkenQuarry_Caelius, 'Location', player) and 
             state.can_reach(LocationName.OldMines_Drusus, 'Location', player) and 
             state.can_reach(LocationName.LavaGrotto_Flavius, 'Location', player))

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
    
    add_rule(multiworld.get_location(LocationName.MystralWoods_Twiggs_LifeElixer, player),
             lambda state: can_defeat_wood_wretch(state, player))
    
    
    add_rule(multiworld.get_location(LocationName.TheRiseSouth_TorchPuzzleNearRopeBridges, player),
             lambda state: can_light_torches(state, player) and state.has(ItemName.MoveRune, player))
    
    add_rule(multiworld.get_location(LocationName.TheRiseNorth_RuinsTorchPuzzle, player),
             lambda state: can_light_torches(state, player) and state.has(ItemName.MoveRune, player))
    
    add_rule(multiworld.get_location(LocationName.SkyTempleFrontDoorTorchPuzzle, player),
             lambda state: can_light_torches(state, player) and state.has(ItemName.MoveRune, player))   
      
    add_rule(multiworld.get_location(LocationName.SkyTempleHubPuzzleMasteryRune, player),
             lambda state: state.has(ItemName.SkyTempleTorch, player, 5))
    
    add_rule(multiworld.get_location(LocationName.SkyTempleUpperAncientLizardSleet, player),
             lambda state: can_block_wind(state, player) and state.has(ItemName.BigKey, player, 12))
    
    add_rule(multiworld.get_location(LocationName.SkyTempleUpperSleetsRemains, player),
             lambda state: state.has(ItemName.DefeatSleet, player))
    add_rule(multiworld.get_location(LocationName.SkyTempleUpperIceLizardElixerChest, player),
             lambda state: state.has(ItemName.DefeatSleet, player))
    
    add_rule(multiworld.get_location(LocationName.TheRise_ManaLily, player),
             lambda state: can_walk_on_water(state, player))
    
    
    add_rule(multiworld.get_location(LocationName.MystralWoods_Backwoods_DetonateTorch, player),
             lambda state: can_light_torches(state, player))
    add_rule(multiworld.get_location(LocationName.MystralWoods_TorchPuzzleOverchargeRune, player),
             lambda state: can_light_torches(state, player) and can_walk_on_water(state, player) and state.has(ItemName.MoveRune, player))
    
    add_rule(multiworld.get_location(LocationName.MystralWoods_SuperLardee_AuraWand, player),
             lambda state: state.has(ItemName.DefeatSleet, player))
    
    add_rule(multiworld.get_location(LocationName.HavenWest_RemoteDetonateRock, player),
             lambda state: can_light_torches(state, player) and state.has_all([ItemName.ImpactRune, ItemName.MoveRune], player))
    
    add_rule(multiworld.get_location(LocationName.MystralWoodsMiningArea_TorchesInTheRiver, player),
             lambda state: can_light_torches(state, player) and state.has(ItemName.MoveRune, player))
    
    add_rule(multiworld.get_location(LocationName.Haven_PortalStone, player),
             lambda state: state.has(ItemName.DefeatSleet, player)) #npc apears after the cutscene you get from returning to haven after your sky temple trip
    add_rule(multiworld.get_location(LocationName.Haven_HallOfTrialsWaveFour, player),
             lambda state: state.has(ItemName.DefeatSleet, player)) #npc apears after the cutscene you get from returning to haven after your sky temple trip
    add_rule(multiworld.get_location(LocationName.Haven_HallOfTrialsWaveEight, player),
             lambda state: state.has(ItemName.DefeatSleet, player)) #npc apears after the cutscene you get from returning to haven after your sky temple trip
    add_rule(multiworld.get_location(LocationName.Haven_HallOfTrialsWaveTwelve, player),
             lambda state: state.has(ItemName.DefeatSleet, player)) #npc apears after the cutscene you get from returning to haven after your sky temple trip
    add_rule(multiworld.get_location(LocationName.Haven_HallOfTrialsTenMinutes, player),
             lambda state: state.has_all([ItemName.DefeatSleet, ItemName.RainRune], player)) #npc apears after the cutscene you get from returning to haven after your sky temple trip
    
    add_rule(multiworld.get_location(LocationName.Highlands_ChestOnSmallLandAcrossWater, player),
             lambda state: can_walk_on_water(state, player))
    add_rule(multiworld.get_location(LocationName.Highlands_SewerCelestialPuzzle, player),
             lambda state: can_walk_on_water(state, player))
    add_rule(multiworld.get_location(LocationName.Highlands_WaterWalkingTorchPuzzle, player),
             lambda state: can_walk_on_water(state, player) and can_light_torches and state.has(ItemName.MoveRune, player))
    add_rule(multiworld.get_location(LocationName.TombOfTheMageKing_DuplicateRuneChest, player),
             lambda state: state.has(ItemName.DuplicateRune, player))
    add_rule(multiworld.get_location(LocationName.TombOfTheMageKing_SwampyPurpleBeadChest, player),
             lambda state: state.has(ItemName.DuplicateRune, player))
    add_rule(multiworld.get_location(LocationName.TombOfTheMageKing_DuplicatePuzzleRoom, player),
             lambda state: state.has(ItemName.DuplicateRune, player))
    add_rule(multiworld.get_location(LocationName.TombOfTheMageKing_BigKeyTwo, player),
             lambda state: state.has(ItemName.DuplicateRune, player))
    add_rule(multiworld.get_location(LocationName.TombOfTheMageKing_CelestialPuzzle, player),
             lambda state: state.has(ItemName.DuplicateRune, player))
    add_rule(multiworld.get_location(LocationName.TombOfTheMageKing_BigKeyThree, player),
             lambda state: state.has(ItemName.DuplicateRune, player))
    add_rule(multiworld.get_location(LocationName.TombOfTheMageKing_BeamPuzzle, player),
             lambda state: state.has(ItemName.DuplicateRune, player))
    add_rule(multiworld.get_location(LocationName.TombOfTheMageKing_BigKeyFour, player),
             lambda state: state.has(ItemName.DuplicateRune, player))
    add_rule(multiworld.get_location(LocationName.TombOfTheMageKing_GhostQueen, player),
             lambda state: state.has(ItemName.BigKey, player, 10) and state.has(ItemName.DuplicateRune, player))
    add_rule(multiworld.get_location(LocationName.TombOfTheMageKing_GhostQueenLifeElixer, player),
             lambda state: state.has(ItemName.DefeatGhostQueen, player))
    add_rule(multiworld.get_location(LocationName.Graveyard_StatueBigKey, player),
             lambda state: state.has(ItemName.DuplicateRune, player))
    add_rule(multiworld.get_location(LocationName.HighlandsUpper_BounceTorchPuzzle, player),
             lambda state: can_light_torches(state, player) and state.has_all([ItemName.DuplicateRune, ItemName.MoveRune, ItemName.BounceRune], player))
    add_rule(multiworld.get_location(LocationName.HighlandsUpper_BounceTorchPuzzle, player),
             lambda state: can_light_torches(state, player) and state.has_all([ItemName.DuplicateRune, ItemName.MoveRune, ItemName.RightRune], player))
    add_rule(multiworld.get_location(LocationName.TheRise_BouncePuzzle, player),
             lambda state: can_light_torches(state, player) and state.has_all([ItemName.MoveRune, ItemName.BounceRune], player))
    add_rule(multiworld.get_location(LocationName.GreyleafHamlet_FireRainPuzzle, player),
             lambda state: can_light_torches(state, player) and state.has_all([ItemName.MoveRune, ItemName.RainRune, ItemName.DefeatGhostQueen], player))
    add_rule(multiworld.get_location(LocationName.GreyleafHamlet_BurnedTowerPuzzle, player),
             lambda state: can_light_torches(state, player) and state.has_all([ItemName.MoveRune, ItemName.DuplicateRune, ItemName.DefeatGhostQueen], player)) #hint torch considered it out of logic
    add_rule(multiworld.get_location(LocationName.GreyleafHamlet_BarTorchPuzzleRoom, player),
             lambda state: can_light_torches(state, player) and state.has_all([ItemName.MoveRune, ItemName.DuplicateRune, ItemName.DefeatGhostQueen, ItemName.TimeRune], player))
    add_rule(multiworld.get_location(LocationName.GreyleafHamlet_SavedTheCitizens, player),
             lambda state: can_light_torches(state, player) and can_detonate(state, player) and state.has_all([ItemName.MoveRune, ItemName.ImpactRune, ItemName.DefeatGhostQueen], player))
    add_rule(multiworld.get_location(LocationName.SkyTempleUpperCombatPuzzleRoom, player),
             lambda state: can_light_torches(state, player) and can_detonate(state, player) and state.has_all([ItemName.MoveRune, ItemName.ImpactRune, ItemName.DefeatGhostQueen], player))
    add_rule(multiworld.get_location(LocationName.GreyleafHamletCave_Blasius, player),
             lambda state: can_walk_on_water(state, player) and state.has(ItemName.Aura_Essence, player))
    add_rule(multiworld.get_location(LocationName.GreyleafHamlet_Xavier, player),
             lambda state: state.has_all([ItemName.DefeatGhostQueen, ItemName.RepairedPitchfork], player))
    add_rule(multiworld.get_location(LocationName.SunkenQuarry_LedgePuzzleRoomSouthEast, player),
             lambda state: state.has_all([ItemName.LeftRune, ItemName.TimeRune], player))
    add_rule(multiworld.get_location(LocationName.OldMines_BigKey, player),
             lambda state: state.has(ItemName.DuplicateRune, player))
    add_rule(multiworld.get_location(LocationName.OldMines_Drusus, player),
             lambda state: can_light_torches(state, player) and state.has(ItemName.MoveRune, player))
    add_rule(multiworld.get_location(LocationName.MystralWoodsMiningArea_PuzzleInTheOldMines, player),
             lambda state: can_light_torches(state, player) and state.has_all([ItemName.MoveRune, ItemName.LeftRune, ItemName.BounceRune], player))
    add_rule(multiworld.get_location(LocationName.TheRiseSouth_GoblinAmbush_CloseToMystralWoodsEntrance, player),
             lambda state: state.has_all([ItemName.DefeatGhostQueen], player))
    add_rule(multiworld.get_location(LocationName.TheRise_ChestAcrossLava, player),
             lambda state: can_walk_on_lava(state, player))
    add_rule(multiworld.get_location(LocationName.LavaGrotto_TorchPuzzleBehindLavaWaterfall, player),
             lambda state: can_light_torches(state, player) and state.has_all([ItemName.DuplicateRune, ItemName.ImpactRune, ItemName.MoveRune], player))
    add_rule(multiworld.get_location(LocationName.LavaGrotto_RockPillarPurpleBead, player),
             lambda state: can_light_torches(state, player) and state.has_all([ItemName.ImpactRune, ItemName.MoveRune], player))
    add_rule(multiworld.get_location(LocationName.LavaGrotto_DrainedLavaPoolPurpleBead, player),
             lambda state: can_light_torches(state, player) and state.has_all([ItemName.RightRune, ItemName.TimeRune, ItemName.BounceRune, ItemName.MoveRune], player))
    add_rule(multiworld.get_location(LocationName.LavaGrotto_RockPillarToCombatRoomPurpleBead, player),
             lambda state: can_light_torches(state, player) and state.has_all([ItemName.ImpactRune, ItemName.MoveRune], player))
    add_rule(multiworld.get_location(LocationName.LavaGrotto_Flavius, player),
             lambda state: can_activate_starswitch(state, player) and state.has_all([ItemName.MoveRune], player))
    add_rule(multiworld.get_location(LocationName.TheRise_SerpentLockedDoor, player),
             lambda state: state.has_all([ItemName.SkyShard, ItemName.DefeatGhostQueen], player))
    add_rule(multiworld.get_location(LocationName.TheRise_WaterfallPurpleBead, player),
             lambda state: can_block_wind(state, player) and state.has(ItemName.HomingRune, player))
    add_rule(multiworld.get_location(LocationName.GreyleafHamlet_WaterboundPurpleBead, player),
             lambda state: can_block_wind(state, player) and state.has_all([ItemName.HomingRune, ItemName.DefeatGhostQueen], player))
    add_rule(multiworld.get_location(LocationName.Highlands_CliffsidePurpleBead, player),
             lambda state: can_block_wind(state, player) and state.has(ItemName.HomingRune, player))
    add_rule(multiworld.get_location(LocationName.MystralWoods_ManaLilyCelestialPuzzle, player),
             lambda state: can_walk_on_lava(state, player) and state.has(ItemName.SizeRune, player))
    add_rule(multiworld.get_location(LocationName.Highlands_PortNecromancerGhostBusters, player),
             lambda state: state.has(ItemName.BottledGhost, player, 3) and state.has(ItemName.DefeatGhostQueen, player))
    add_rule(multiworld.get_location(LocationName.Highlands_SouthernTorchPuzzle, player),
             lambda state: can_light_torches(state, player) and state.has_all([ItemName.MoveRune, ItemName.PeriodicRune], player))
    add_rule(multiworld.get_location(LocationName.TheRise_ChestNearDarkTower, player),
             lambda state: can_block_wind(state, player) and state.has_all([ItemName.DefeatGhostQueen, ItemName.MoveRune], player))
    add_rule(multiworld.get_location(LocationName.MystralWoods_DeepWoods_StrangeOldGoblinRippingYouOff, player),
             lambda state: state.has_all([ItemName.MystralWoodsCleansed, ItemName.DefeatGhostQueen], player))


    if False:
        add_rule(multiworld.get_location(LocationName.Highlands_PortBadge, player),
             lambda state: can_walk_on_water(state, player))   
        add_rule(multiworld.get_location(LocationName.GreyleafHamlet_Zako, player),
             lambda state: state.has_all([ItemName.DefeatGhostQueen, ItemName.BrokenPitchfork, ItemName.ChunkOfMetal], player))
        add_rule(multiworld.get_location(LocationName.Highlands_CousinsFarmer, player),
             lambda state: state.has_all([ItemName.DefeatGhostQueen, ItemName.Pitchfork], player))
        add_rule(multiworld.get_location(LocationName.HighlandsUpper_GoblinBreadThieves, player),
             lambda state: state.has_all([ItemName.DefeatGhostQueen], player))
        add_rule(multiworld.get_location(LocationName.Highlands_BakerTwo, player),
             lambda state: state.has_all([ItemName.DefeatGhostQueen, ItemName.LoavesOfBread], player))
        add_rule(multiworld.get_location(LocationName.Highlands_PortNecromancer, player),
             lambda state: state.has(ItemName.DefeatGhostQueen, player))
        
        add_rule(multiworld.get_location(LocationName.GreyleafHamlet_MariesBagOfWaresResult, player),
             lambda state: state.has(ItemName.BagOfWares, player, 4))
        add_rule(multiworld.get_location(LocationName.GreyleafHamlet_JeffsThankYouGift, player),
             lambda state: state.has_all([ItemName.Token, ItemName.DefeatGhostQueen], player))
        add_rule(multiworld.get_location(LocationName.Highlands_Farmer, player),
             lambda state: state.has(ItemName.Pitchfork, player))
        add_rule(multiworld.get_location(LocationName.Highlands_Beggar, player),
             lambda state: state.has(ItemName.HotBread, player, 2))
        add_rule(multiworld.get_location(LocationName.Highlands_Fisherman, player),
             lambda state: state.has(ItemName.BoarMeat, player))
        add_rule(multiworld.get_location(LocationName.TheRiseNorth_TravelingMerchantAnna, player),
             lambda state: state.has(ItemName.Flowers, player))
        add_rule(multiworld.get_location(LocationName.TheRise_GhostStatueAcrossLava, player),
             lambda state: can_walk_on_lava(state, player) and state.has(ItemName.BottleForSpirits, player))
        add_rule(multiworld.get_location(LocationName.GreyleafHamlet_GraveyardGhostStatue, player),
             lambda state: state.has_all([ItemName.BottleForSpirits, ItemName.DefeatGhostQueen], player))
        add_rule(multiworld.get_location(LocationName.HighlandsUpper_GhostStatue, player),
             lambda state: state.has(ItemName.BottleForSpirits, player))



def set_item_rules(multiworld, player):
    pass