from typing import Callable, List, Dict, NamedTuple, Optional
from enum import Enum
from BaseClasses import Location, MultiWorld
from .Names.LocationNames import LocationName
from .Names.ItemNames import ItemName

class LocationType(str, Enum):
   Item = "Item"
   Event = "Event"


def always_on(multiworld, player):
    return True

def quests_items_included(multiworld, player):
    return False

class LocationData(NamedTuple):
    id: Optional[int]
    name: str
    vanilla_item: str
    loc_type: LocationType = LocationType.Item
    event: bool = False
    included: Callable[[MultiWorld, int], bool] = always_on


class MagesOfMystraliaLocation(Location):
    game: str = "Mages Of Mystralia"

base_id: int = 62000

test_locations = [
    LocationData(base_id + 1, LocationName.Haven_InfrontOfTower, ItemName.FiveGreenBeads),
    LocationData(base_id + 2, LocationName.Haven_EnchanterManaLily, ItemName.ManaCharm),
    LocationData(base_id + 3, LocationName.Haven_ManaLilyTwo, ItemName.ManaCharm), #Costs 20 Green Soul Beads
    LocationData(base_id + 4, LocationName.Haven_ManaLilyThree, ItemName.ManaCharm), #Costs 20 Green Soul Beads
    LocationData(base_id + 5, LocationName.Haven_ManaLilyFour, ItemName.ManaCharm), #Costs 20 Green Soul Beads
    LocationData(base_id + 6, LocationName.Haven_ManaLilyFive, ItemName.ManaCharm), #Costs 20 Green Soul Beads
    LocationData(base_id + 7, LocationName.Haven_UpgradeFountainOne, ItemName.HealthUpgrade),
    LocationData(base_id + 8, LocationName.Haven_UpgradeFountainTwo, ItemName.ManaUpgrade),
    LocationData(base_id + 9, LocationName.Haven_UpgradeFountainThree, ItemName.HealthUpgrade),
    LocationData(base_id + 10, LocationName.Haven_UpgradeFountainFour, ItemName.ManaUpgrade),
    LocationData(base_id + 11, LocationName.Haven_UpgradeFountainFive, ItemName.HealthUpgrade),
    LocationData(base_id + 12, LocationName.Haven_UpgradeFountainSix, ItemName.ManaUpgrade),
    LocationData(base_id + 13, LocationName.Haven_UpgradeFountainSeven, ItemName.HealthUpgrade),
    LocationData(base_id + 14, LocationName.Haven_UpgradeFountainEight, ItemName.ManaUpgrade),
    LocationData(base_id + 15, LocationName.Haven_UpgradeFountainNine, ItemName.HealthUpgrade),
    LocationData(base_id + 16, LocationName.Haven_UpgradeFountainTen, ItemName.ManaUpgrade),
    LocationData(base_id + 17, LocationName.Haven_UnderBridge, ItemName.Purple_Soulbead),
    LocationData(base_id + 18, LocationName.Haven_RandomRunePuzzleRoom, ItemName.RandomRune),
    LocationData(base_id + 19, LocationName.WindingGlade_TeleportRunePuzzleRoom, ItemName.TeleportRune),
    LocationData(base_id + 20, LocationName.MystralWoods_ManaLilyCelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(base_id + 21, LocationName.MystralWoods_ManaLily, ItemName.ManaLilyBulb),
    LocationData(base_id + 23, LocationName.MystralWoods_PostCart_PurpleBeadPuzzleRoom, ItemName.Purple_Soulbead),
    LocationData(base_id + 25, LocationName.MystralWoods_Lardee_MoveRune, ItemName.MoveRune),
    LocationData(base_id + 28, LocationName.MystralWoods_DeepWoods_StrangeOldGoblin, ItemName.BigKey),
    LocationData(base_id + 30, LocationName.MystralWoods_Twiggs_LifeElixer, ItemName.WoodWretchElixer),
    LocationData(base_id + 22, LocationName.GreyleafHamlet_ManaLily, ItemName.ManaLilyBulb), #Costs 99 Green Soul Beads
    LocationData(base_id + 32, LocationName.TheRiseSouth_CelestialPuzzle_CloseToMystralWoodsEntrance, ItemName.HomingRune),
    LocationData(base_id + 33, LocationName.TheRiseSouth_StrangeMan_IgniWand, ItemName.IgniWand),
    LocationData(base_id + 34, LocationName.TheRiseSouth_TorchPuzzleNearRopeBridges, ItemName.Purple_Soulbead),
    LocationData(base_id + 35, LocationName.TheRise_SecretRuinsPath, ItemName.ThirtyGreenBeads),
    LocationData(base_id + 36, LocationName.TheRise_RightRune, ItemName.RightRune),
    LocationData(base_id + 37, LocationName.TheRise_RightRunePuzzle, ItemName.BigKey),
    LocationData(base_id + 38, LocationName.TheRiseNorth_HiddenUnderStairsPurpleSoulBead, ItemName.Purple_Soulbead),
    LocationData(base_id + 39, LocationName.TheRiseNorth_RuinsTorchPuzzle, ItemName.Purple_Soulbead),
    LocationData(base_id + 40, LocationName.SkyTempleFrontDoorTorchPuzzle, ItemName.BigKey),
    LocationData(base_id + 41, LocationName.SkyTempleHubDetonateRock, ItemName.TwentyFiveGreenBeads),
    LocationData(base_id + 42, LocationName.SkyTempleHubEastBigKey, ItemName.BigKey),
    LocationData(base_id + 43, LocationName.SkyTempleHubNorthDetonateRune, ItemName.DetonateRune),
    LocationData(base_id + 44, LocationName.SkyTempleHubEastPurpleSoulbeadBehindDetonate, ItemName.Purple_Soulbead),
    LocationData(base_id + 45, LocationName.SkyTempleHubEastPuzzleRoomBehindDetonateRock, ItemName.Purple_Soulbead),
    LocationData(base_id + 46, LocationName.SkyTempleHubPuzzleMasteryRune, ItemName.MasteryRune),
    LocationData(base_id + 47, LocationName.SkyTempleHubChestBehindDetonateRock, ItemName.TenGreenBeads),
    LocationData(base_id + 48, LocationName.SkyTempleUpperBigKey, ItemName.BigKey),
    LocationData(base_id + 49, LocationName.SkyTempleUpperCombatPuzzleRoom, ItemName.Purple_Soulbead),
    LocationData(base_id + 50, LocationName.SkyTempleUpperSleetsRemains, ItemName.SkyShard),
    LocationData(base_id + 51, LocationName.SkyTempleUpperIceLizardElixerChest, ItemName.IceLizardElixer),
    LocationData(base_id + 52, LocationName.SkyTempleUpperCelestialPuzzleNearRemains, ItemName.Purple_Soulbead),
    LocationData(base_id + 53, LocationName.TheRistNorthUpperLedge_ImpactRune, ItemName.ImpactRune),
    LocationData(base_id + 54, LocationName.TheRise_ManaLily, ItemName.ManaLilyBulb),
    LocationData(base_id + 55, LocationName.MystralWoods_Backwoods_DetonateTorch, ItemName.Purple_Soulbead),
    LocationData(base_id + 56, LocationName.MystralWoods_TorchPuzzleOverchargeRune, ItemName.OverchargeRune),
    LocationData(base_id + 57, LocationName.MystralWoods_SuperLardee_AuraWand, ItemName.AuraWand),
    LocationData(base_id + 58, LocationName.OldMinesLardee_PurpleBeadDetonateRock, ItemName.Purple_Soulbead),
    LocationData(base_id + 59, LocationName.HavenWest_RemoteDetonateRock, ItemName.Purple_Soulbead),
    LocationData(base_id + 60, LocationName.Haven_PortalStone, ItemName.PortalStone), #costs 75 green soul beads
    LocationData(base_id + 61, LocationName.Haven_HallOfTrialsWaveFour, ItemName.Purple_Soulbead),
    LocationData(base_id + 62, LocationName.Haven_HallOfTrialsWaveEight, ItemName.ProximityRune),
    LocationData(base_id + 63, LocationName.Haven_HallOfTrialsWaveTwelve, ItemName.ArchmagesRobe),
    LocationData(base_id + 65, LocationName.Haven_HallOfTrialsTenMinutes, ItemName.TrialWand),
    LocationData(base_id + 66, LocationName.Haven_ChestNearManaFountain, ItemName.FifteenGreenBeads),
    LocationData(base_id + 67, LocationName.MystralWoodsMiningArea_PuzzleInTheOldMines, ItemName.Purple_Soulbead),
    LocationData(base_id + 68, LocationName.MystralWoodsMiningArea_TorchesInTheRiver, ItemName.Purple_Soulbead),
    LocationData(base_id + 69, LocationName.MystralWoodsMiningArea_WoodedCombatPuzzle, ItemName.TimeRune),
    LocationData(base_id + 71, LocationName.Highlands_Farmer, ItemName.SeventyFiveGreenBeads),
    LocationData(base_id + 72, LocationName.Highlands_Fisherman, ItemName.AquaWand),
    LocationData(base_id + 73, LocationName.Highlands_Beggar, ItemName.BrokenPortalStone),
    LocationData(base_id + 74, LocationName.Highlands_GuardTowerStealthPuzzle, ItemName.GaeaWand),
    LocationData(base_id + 77, LocationName.TheRiseNorth_TravelingMerchantAnna, ItemName.LifeStaff),
    LocationData(base_id + 79, LocationName.Highlands_ChestOnSmallLandAcrossWater, ItemName.FiftyGreenBeads),
    LocationData(base_id + 80, LocationName.Highlands_SewerCelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(base_id + 82, LocationName.Highlands_WaterWalkingTorchPuzzle, ItemName.BounceRune),
    LocationData(base_id + 83, LocationName.TombOfTheMageKing_BigKeyOne, ItemName.BigKey),
    LocationData(base_id + 84, LocationName.TombOfTheMageKing_DuplicateRuneChest, ItemName.DuplicateRune),
    LocationData(base_id + 85, LocationName.TombOfTheMageKing_SwampyPurpleBeadChest, ItemName.Purple_Soulbead),
    LocationData(base_id + 86, LocationName.TombOfTheMageKing_DuplicatePuzzleRoom, ItemName.Purple_Soulbead),
    LocationData(base_id + 87, LocationName.TombOfTheMageKing_BigKeyTwo, ItemName.BigKey),
    LocationData(base_id + 88, LocationName.TombOfTheMageKing_CelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(base_id + 89, LocationName.TombOfTheMageKing_BigKeyThree, ItemName.BigKey),
    LocationData(base_id + 90, LocationName.TombOfTheMageKing_BeamPuzzle, ItemName.Purple_Soulbead),
    LocationData(base_id + 91, LocationName.TombOfTheMageKing_BigKeyFour, ItemName.BigKey),
    LocationData(base_id + 92, LocationName.TombOfTheMageKing_PuzzleRoomInverseRune, ItemName.InverseRune),
    LocationData(base_id + 93, LocationName.TombOfTheMageKing_GhostQueenLifeElixer, ItemName.GhostQueenElixer),
    LocationData(base_id + 95, LocationName.Graveyard_StatueBigKey, ItemName.BigKey),
    LocationData(base_id + 96, LocationName.HighlandsUpper_BounceTorchPuzzle, ItemName.Purple_Soulbead),
    LocationData(base_id + 97, LocationName.HighlandsUpper_CelestialPuzzle, ItemName.EtherRune),
    LocationData(base_id + 98, LocationName.HighlandsUpper_LowerTorchPuzzle, ItemName.SizeRune),
    LocationData(base_id + 99, LocationName.TheRise_BouncePuzzle, ItemName.RainRune),
    LocationData(base_id + 100, LocationName.GreyleafHamlet_FireRainPuzzle, ItemName.Purple_Soulbead),
    LocationData(base_id + 101, LocationName.GreyleafHamlet_BurnedTowerPuzzle, ItemName.SwiftRune),
    LocationData(base_id + 102, LocationName.GreyleafHamlet_BarTorchPuzzleRoom, ItemName.LeftRune),
    LocationData(base_id + 103, LocationName.GreyleafHamlet_SavedTheCitizens, ItemName.BigKey),
    LocationData(base_id + 104, LocationName.GreyleafHamlet_LedgeCombatPuzzleRoom, ItemName.PushRune),
    LocationData(base_id + 105, LocationName.GreyleafHamletCave_CelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(base_id + 106, LocationName.GreyleafHamletCave_Blasius, ItemName.Aura_Essence),
    LocationData(base_id + 107, LocationName.GreyleafHamlet_JeffsThankYouGift, ItemName.Soul_Scepter),
    LocationData(base_id + 108, LocationName.GreyleafHamlet_Xavier, ItemName.NegationScepter),
    LocationData(base_id + 112, LocationName.SunkenQuarry_HiddenPuzzleRoomNorthWest, ItemName.AtOnceRune),
    LocationData(base_id + 113, LocationName.SunkenQuarry_LedgePuzzleRoomSouthEast, ItemName.Purple_Soulbead),
    LocationData(base_id + 114, LocationName.SunkenQuarry_SouthEastCactusChest, ItemName.Purple_Soulbead),
    LocationData(base_id + 115, LocationName.SunkenQuarry_CelestialPuzzleNorthEast, ItemName.Purple_Soulbead),
    LocationData(base_id + 116, LocationName.SunkenQuarry_NorthWaterChest, ItemName.FiftyGreenBeads),
    LocationData(base_id + 117, LocationName.SunkenQuarry_NorthCombatArenaChest, ItemName.Purple_Soulbead),
    LocationData(base_id + 118, LocationName.SunkenQuarry_Caelius, ItemName.Aqua_Essence),
    LocationData(base_id + 120, LocationName.OldMines_BigKey, ItemName.BigKey),
    LocationData(base_id + 121, LocationName.OldMines_CrystalCombatPuzzleRoom, ItemName.ExpireRune),
    LocationData(base_id + 122, LocationName.OldMines_CrystalCartPuzzle, ItemName.Purple_Soulbead),
    LocationData(base_id + 123, LocationName.OldMines_CelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(base_id + 124, LocationName.OldMines_Drusus, ItemName.Gaea_Essence),
    LocationData(base_id + 126, LocationName.TheRiseSouth_GoblinAmbush_CloseToMystralWoodsEntrance, ItemName.RodOfTheBerserker),
    LocationData(base_id + 127, LocationName.TheRise_ChestNearLavaGrotto, ItemName.TwentyFiveGreenBeads),
    LocationData(base_id + 128, LocationName.TheRise_ChestAcrossLava, ItemName.TwentyGreenBeads),
    LocationData(base_id + 129, LocationName.LavaGrotto_CelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(base_id + 130, LocationName.LavaGrotto_TorchPuzzleBehindLavaWaterfall, ItemName.PeriodicRune),
    LocationData(base_id + 131, LocationName.LavaGrotto_RockPillarPurpleBead, ItemName.Purple_Soulbead),
    LocationData(base_id + 132, LocationName.LavaGrotto_DrainedLavaPoolPurpleBead, ItemName.Purple_Soulbead),
    LocationData(base_id + 133, LocationName.LavaGrotto_RockPillarToCombatRoomPurpleBead, ItemName.Purple_Soulbead),
    LocationData(base_id + 134, LocationName.LavaGrotto_Flavius, ItemName.Igni_Essence),
    LocationData(base_id + 135, LocationName.TheRise_SerpentLockedDoor, ItemName.MystralianElixer),
    LocationData(base_id + 136, LocationName.TheRise_WaterfallPurpleBead, ItemName.Purple_Soulbead),
    LocationData(base_id + 137, LocationName.GreyleafHamlet_WaterboundPurpleBead, ItemName.Purple_Soulbead),
    LocationData(base_id + 138, LocationName.Highlands_CliffsidePurpleBead, ItemName.Purple_Soulbead),
    LocationData(base_id + 139, LocationName.HighlandsUpper_ManaLily, ItemName.ManaLilyBulb),
    LocationData(base_id + 140, LocationName.Highlands_PortNecromancerGhostBusters, ItemName.AfterLifeElixer),
    LocationData(base_id + 141, LocationName.Highlands_SouthernTorchPuzzle, ItemName.Purple_Soulbead),
    LocationData(base_id + 142, LocationName.TheRise_ChestNearDarkTower, ItemName.Purple_Soulbead),
    LocationData(base_id + 143, LocationName.MystralWoods_DeepWoods_StrangeOldGoblinRippingYouOff, ItemName.Purple_Soulbead),  #costs 999 green soul beads,
    LocationData(base_id + 144, LocationName.GreyleafHamlet_MariesBagOfWaresResult, ItemName.FiftyGreenBeads),
    
    LocationData(base_id + 125, LocationName.GreyleafHamlet_Zako, ItemName.RepairedPitchfork, included=quests_items_included),
    LocationData(base_id + 119, LocationName.OldMines_MetalIngot, ItemName.ChunkOfMetal, included=quests_items_included),
    LocationData(base_id + 109, LocationName.Highlands_CousinsFarmer, ItemName.BrokenPitchfork, included=quests_items_included),
    LocationData(base_id + 110, LocationName.HighlandsUpper_GoblinBreadThieves, ItemName.LoavesOfBread, included=quests_items_included),
    LocationData(base_id + 111, LocationName.Highlands_BakerTwo, ItemName.HotBread, included=quests_items_included),
    LocationData(base_id + 94, LocationName.Highlands_PortNecromancer, ItemName.BottleForSpirits, included=quests_items_included),
    LocationData(base_id + 81, LocationName.Highlands_PortBadge, ItemName.Badge, included=quests_items_included),
    LocationData(base_id + 78, LocationName.Highlands_Boar, ItemName.BoarMeat, included=quests_items_included),
    LocationData(base_id + 75, LocationName.Highlands_Baker, ItemName.HotBread, included=quests_items_included), #costs 10 green soul beads
    LocationData(base_id + 70, LocationName.Highlands_Pitchfork, ItemName.Pitchfork, included=quests_items_included),
    LocationData(base_id + 31, LocationName.GreyleafHamlet_JeffsGiftForwife, ItemName.Token, included=quests_items_included), #Costs 75 Green Soul Beads
    LocationData(base_id + 29, LocationName.MystralWoods_DeepWoods_BagOfWaresTwo, ItemName.BagOfWares, included=quests_items_included),
    LocationData(base_id + 26, LocationName.OldMinesLardee_BagOfWares, ItemName.BagOfWares, included=quests_items_included),
    LocationData(base_id + 27, LocationName.MystralWoods_DeepWoods_BagOfWaresOne, ItemName.BagOfWares, included=quests_items_included),
    LocationData(base_id + 24, LocationName.MystralWoods_GoblinCamp_BagOfWares, ItemName.BagOfWares, included=quests_items_included),
    LocationData(base_id + 76, LocationName.Highlands_TownsPersonOnPlatform, ItemName.Flowers, included=quests_items_included),
]


events = [
    LocationData(None, LocationName.MystalWoodsMariesCart, ItemName.FixedMariesCart, LocationType.Event, True),
    LocationData(None, LocationName.WoodWretchTwiggsFight, ItemName.MystralWoodsCleansed, LocationType.Event, True),
    LocationData(None, LocationName.SkyTempleUpperAncientLizardSleet, ItemName.DefeatSleet, LocationType.Event, True),
    LocationData(None, LocationName.MentorGreyleafhamlet, ItemName.EclipseApproaching, LocationType.Event, True),
    LocationData(None, LocationName.SkyTempleHubCelestialPuzzleTorch, ItemName.SkyTempleTorch, LocationType.Event, True),
    LocationData(None, LocationName.SkyTempleHubCampsightTorch, ItemName.SkyTempleTorch, LocationType.Event, True),
    LocationData(None, LocationName.SkyTempleHubNorthTorch, ItemName.SkyTempleTorch, LocationType.Event, True),
    LocationData(None, LocationName.SkyTempleHubNorthTorchBehindDetonateRock, ItemName.SkyTempleTorch, LocationType.Event, True),
    LocationData(None, LocationName.SkyTempleHubEastTorchBehindDetonateRock, ItemName.SkyTempleTorch, LocationType.Event, True),
    LocationData(None, LocationName.TombOfTheMageKing_GhostQueen, ItemName.DefeatGhostQueen, LocationType.Event, True),
    LocationData(None, LocationName.TheRise_GhostStatueAcrossLava, ItemName.BottledGhost, LocationType.Event, True),
    LocationData(None, LocationName.GreyleafHamlet_GraveyardGhostStatue, ItemName.BottledGhost, LocationType.Event, True),
    LocationData(None, LocationName.HighlandsUpper_GhostStatue, ItemName.BottledGhost, LocationType.Event, True),
    LocationData(None, LocationName.DarkTowerAerie, ItemName.EclipseStopped, LocationType.Event, True)
]



all_locations: List[LocationData] = test_locations + events
location_name_to_id: Dict[str, LocationData] = {location.name: location for location in all_locations if location.loc_type != LocationType.Event}