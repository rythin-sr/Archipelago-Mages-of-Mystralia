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

class LocationData(NamedTuple):
    id: Optional[int]
    name: str
    vanilla_item: str
    loc_type: LocationType = LocationType.Item
    event: bool = False
    included: Callable[[MultiWorld, int], bool] = always_on


class MagesOfMystraliaLocation(Location):
    game: str = "Mages Of Mystralia"

test_locations = [
    LocationData(1, LocationName.Haven_InfrontOfTower, ItemName.FiveGreenBeads),
    LocationData(2, LocationName.Haven_EnchanterManaLily, ItemName.ManaCharm),

    LocationData(3, LocationName.Haven_ManaLilyTwo, ItemName.ManaCharm), #Costs 20 Green Soul Beads
    LocationData(4, LocationName.Haven_ManaLilyThree, ItemName.ManaCharm), #Costs 20 Green Soul Beads
    LocationData(5, LocationName.Haven_ManaLilyFour, ItemName.ManaCharm), #Costs 20 Green Soul Beads
    LocationData(6, LocationName.Haven_ManaLilyFive, ItemName.ManaCharm), #Costs 20 Green Soul Beads

    LocationData(7, LocationName.Haven_UpgradeFountainOne, ItemName.HealthUpgrade),
    LocationData(8, LocationName.Haven_UpgradeFountainTwo, ItemName.ManaUpgrade),
    LocationData(9, LocationName.Haven_UpgradeFountainThree, ItemName.HealthUpgrade),
    LocationData(10, LocationName.Haven_UpgradeFountainFour, ItemName.ManaUpgrade),
    LocationData(11, LocationName.Haven_UpgradeFountainFive, ItemName.HealthUpgrade),
    LocationData(12, LocationName.Haven_UpgradeFountainSix, ItemName.ManaUpgrade),
    LocationData(13, LocationName.Haven_UpgradeFountainSeven, ItemName.HealthUpgrade),
    LocationData(14, LocationName.Haven_UpgradeFountainEight, ItemName.ManaUpgrade),
    LocationData(15, LocationName.Haven_UpgradeFountainNine, ItemName.HealthUpgrade),
    LocationData(16, LocationName.Haven_UpgradeFountainTen, ItemName.ManaUpgrade),
    
    LocationData(17, LocationName.Haven_UnderBridge, ItemName.Purple_Soulbead),
    LocationData(18, LocationName.Haven_RandomRunePuzzleRoom, ItemName.RandomRune),
    LocationData(19, LocationName.WindingGlade_TeleportRunePuzzleRoom, ItemName.TeleportRune),

    LocationData(20, LocationName.MystralWoods_ManaLilyCelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(21, LocationName.MystralWoods_ManaLily, ItemName.ManaLilyBulb),
    LocationData(23, LocationName.MystralWoods_PostCart_PurpleBeadPuzzleRoom, ItemName.Purple_Soulbead),
    LocationData(24, LocationName.MystralWoods_GoblinCamp_BagOfWares, ItemName.BagOfWares),
    LocationData(25, LocationName.MystralWoods_Lardee_MoveRune, ItemName.MoveRune),
    LocationData(26, LocationName.OldMinesLardee_BagOfWares, ItemName.BagOfWares),
    LocationData(27, LocationName.MystralWoods_DeepWoods_BagOfWaresOne, ItemName.BagOfWares),
    LocationData(28, LocationName.MystralWoods_DeepWoods_StrangeOldGoblin, ItemName.BigKey),
    LocationData(29, LocationName.MystralWoods_DeepWoods_BagOfWaresTwo, ItemName.BagOfWares),
    LocationData(30, LocationName.MystralWoods_Twiggs_LifeElixer, ItemName.WoodWretchElixer),

    LocationData(22, LocationName.GreyleafHamlet_ManaLily, ItemName.ManaLilyBulb), #Costs 99 Green Soul Beads
    LocationData(31, LocationName.GreyleafHamlet_JeffsGiftForwife, ItemName.Token), #Costs 75 Green Soul Beads

    LocationData(32, LocationName.TheRiseSouth_CelestialPuzzle_CloseToMystralWoodsEntrance, ItemName.HomingRune),
    LocationData(33, LocationName.TheRiseSouth_StrangeMan_IgniWand, ItemName.IgniWand),
    LocationData(34, LocationName.TheRiseSouth_TorchPuzzleNearRopeBridges, ItemName.Purple_Soulbead),

    LocationData(35, LocationName.TheRise_SecretRuinsPath, ItemName.ThirtyGreenBeads),
    LocationData(36, LocationName.TheRise_RightRune, ItemName.RightRune),
    LocationData(37, LocationName.TheRise_RightRunePuzzle, ItemName.BigKey),

    LocationData(38, LocationName.TheRiseNorth_HiddenUnderStairsPurpleSoulBead, ItemName.Purple_Soulbead),
    LocationData(39, LocationName.TheRiseNorth_RuinsTorchPuzzle, ItemName.Purple_Soulbead),

    LocationData(40, LocationName.SkyTempleFrontDoorTorchPuzzle, ItemName.BigKey),
    LocationData(41, LocationName.SkyTempleHubDetonateRock, ItemName.TwentyFiveGreenBeads),
    LocationData(42, LocationName.SkyTempleHubEastBigKey, ItemName.BigKey),
    LocationData(43, LocationName.SkyTempleHubNorthDetonateRune, ItemName.DetonateRune),
    LocationData(44, LocationName.SkyTempleHubEastPurpleSoulbeadBehindDetonate, ItemName.Purple_Soulbead),
    LocationData(45, LocationName.SkyTempleHubEastPuzzleRoomBehindDetonateRock, ItemName.Purple_Soulbead),
    LocationData(46, LocationName.SkyTempleHubPuzzleMasteryRune, ItemName.MasteryRune),
    LocationData(47, LocationName.SkyTempleHubChestBehindDetonateRock, ItemName.TenGreenBeads),
    LocationData(48, LocationName.SkyTempleUpperBigKey, ItemName.BigKey),
    LocationData(49, LocationName.SkyTempleUpperCombatPuzzleRoom, ItemName.Purple_Soulbead),
    LocationData(50, LocationName.SkyTempleUpperSleetsRemains, ItemName.SkyShard),
    LocationData(51, LocationName.SkyTempleUpperIceLizardElixerChest, ItemName.IceLizardElixer),
    LocationData(52, LocationName.SkyTempleUpperCelestialPuzzleNearRemains, ItemName.Purple_Soulbead),
    LocationData(53, LocationName.TheRistNorthUpperLedge_ImpactRune, ItemName.ImpactRune),

    LocationData(54, LocationName.TheRise_ManaLily, ItemName.ManaLilyBulb),
    LocationData(55, LocationName.MystralWoods_Backwoods_DetonateTorch, ItemName.Purple_Soulbead),
    LocationData(56, LocationName.MystralWoods_TorchPuzzleOverchargeRune, ItemName.OverchargeRune),
    LocationData(57, LocationName.MystralWoods_SuperLardee_AuraWand, ItemName.AuraWand),
    LocationData(58, LocationName.OldMinesLardee_PurpleBeadDetonateRock, ItemName.Purple_Soulbead),
    LocationData(59, LocationName.HavenWest_RemoteDetonateRock, ItemName.Purple_Soulbead),
    LocationData(60, LocationName.Haven_PortalStone, ItemName.PortalStone), #costs 75 green soul beads

    LocationData(61, LocationName.Haven_HallOfTrialsWaveFour, ItemName.Purple_Soulbead),
    LocationData(62, LocationName.Haven_HallOfTrialsWaveEight, ItemName.ProximityRune),
    LocationData(63, LocationName.Haven_HallOfTrialsWaveTwelve, ItemName.ArchmagesRobe),
    LocationData(65, LocationName.Haven_HallOfTrialsTenMinutes, ItemName.TrialWand),
    LocationData(66, LocationName.Haven_ChestNearManaFountain, ItemName.FifteenGreenBeads),
    LocationData(67, LocationName.MystralWoodsMiningArea_PuzzleInTheOldMines, ItemName.Purple_Soulbead),
    LocationData(68, LocationName.MystralWoodsMiningArea_TorchesInTheRiver, ItemName.Purple_Soulbead),
    LocationData(69, LocationName.MystralWoodsMiningArea_WoodedCombatPuzzle, ItemName.TimeRune),
    LocationData(70, LocationName.Highlands_Pitchfork, ItemName.Pitchfork),
    LocationData(71, LocationName.Highlands_Farmer, ItemName.SeventyFiveGreenBeads),
    LocationData(72, LocationName.Highlands_Fisherman, ItemName.AquaWand),
    LocationData(73, LocationName.Highlands_Beggar, ItemName.BrokenPortalStone),
    LocationData(74, LocationName.Highlands_GuardTowerStealthPuzzle, ItemName.GaeaWand),
    LocationData(75, LocationName.Highlands_Baker, ItemName.HotBread), #costs 10 green soul beads
    LocationData(76, LocationName.Highlands_TownsPersonOnPlatform, ItemName.Flowers),
    LocationData(77, LocationName.TheRiseNorth_TravelingMerchantAnna, ItemName.LifeStaff),
    LocationData(78, LocationName.Highlands_Boar, ItemName.BoarMeat),
    LocationData(79, LocationName.Highlands_ChestOnSmallLandAcrossWater, ItemName.FiftyGreenBeads),
    LocationData(80, LocationName.Highlands_SewerCelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(81, LocationName.Highlands_PortBadge, ItemName.Badge),
    LocationData(82, LocationName.Highlands_WaterWalkingTorchPuzzle, ItemName.BounceRune),
    LocationData(83, LocationName.TombOfTheMageKing_BigKeyOne, ItemName.BigKey),
    LocationData(84, LocationName.TombOfTheMageKing_DuplicateRuneChest, ItemName.DuplicateRune),
    LocationData(85, LocationName.TombOfTheMageKing_SwampyPurpleBeadChest, ItemName.Purple_Soulbead),
    LocationData(86, LocationName.TombOfTheMageKing_DuplicatePuzzleRoom, ItemName.Purple_Soulbead),
    LocationData(87, LocationName.TombOfTheMageKing_BigKeyTwo, ItemName.BigKey),
    LocationData(88, LocationName.TombOfTheMageKing_CelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(89, LocationName.TombOfTheMageKing_BigKeyThree, ItemName.BigKey),
    LocationData(90, LocationName.TombOfTheMageKing_BeamPuzzle, ItemName.Purple_Soulbead),
    LocationData(91, LocationName.TombOfTheMageKing_BigKeyFour, ItemName.BigKey),
    LocationData(92, LocationName.TombOfTheMageKing_PuzzleRoomInverseRune, ItemName.InverseRune),
    LocationData(93, LocationName.TombOfTheMageKing_GhostQueenLifeElixer, ItemName.GhostQueenElixer),
    LocationData(94, LocationName.Highlands_PortNecromancer, ItemName.BottleForSpirits),
    LocationData(95, LocationName.Graveyard_StatueBigKey, ItemName.BigKey),
    LocationData(96, LocationName.HighlandsUpper_BounceTorchPuzzle, ItemName.Purple_Soulbead),
    LocationData(97, LocationName.HighlandsUpper_CelestialPuzzle, ItemName.EtherRune),
    LocationData(98, LocationName.HighlandsUpper_LowerTorchPuzzle, ItemName.SizeRune),
    LocationData(99, LocationName.TheRise_BouncePuzzle, ItemName.RainRune),
    LocationData(100, LocationName.GreyleafHamlet_FireRainPuzzle, ItemName.Purple_Soulbead),
    LocationData(101, LocationName.GreyleafHamlet_BurnedTowerPuzzle, ItemName.SwiftRune),
    LocationData(102, LocationName.GreyleafHamlet_BarTorchPuzzleRoom, ItemName.LeftRune),
    LocationData(103, LocationName.GreyleafHamlet_SavedTheCitizens, ItemName.BigKey),
    LocationData(104, LocationName.GreyleafHamlet_LedgeCombatPuzzleRoom, ItemName.PushRune),
    LocationData(105, LocationName.GreyleafHamletCave_CelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(106, LocationName.GreyleafHamletCave_Blasius, ItemName.Aura_Essence),
    LocationData(107, LocationName.GreyleafHamlet_JeffsThankYouGift, ItemName.Soul_Scepter),
    LocationData(108, LocationName.GreyleafHamlet_Xavier, ItemName.NegationScepter),
    LocationData(109, LocationName.Highlands_CousinsFarmer, ItemName.BrokenPitchfork),
    LocationData(110, LocationName.HighlandsUpper_GoblinBreadThieves, ItemName.LoavesOfBread),
    LocationData(111, LocationName.Highlands_BakerTwo, ItemName.HotBread),
    LocationData(112, LocationName.SunkenQuarry_HiddenPuzzleRoomNorthWest, ItemName.AtOnceRune),
    LocationData(113, LocationName.SunkenQuarry_LedgePuzzleRoomSouthEast, ItemName.Purple_Soulbead),
    LocationData(114, LocationName.SunkenQuarry_SouthEastCactusChest, ItemName.Purple_Soulbead),
    LocationData(115, LocationName.SunkenQuarry_CelestialPuzzleNorthEast, ItemName.Purple_Soulbead),
    LocationData(116, LocationName.SunkenQuarry_NorthWaterChest, ItemName.FiftyGreenBeads),
    LocationData(117, LocationName.SunkenQuarry_NorthCombatArenaChest, ItemName.Purple_Soulbead),
    LocationData(118, LocationName.SunkenQuarry_Caelius, ItemName.Aqua_Essence),
    LocationData(119, LocationName.OldMines_MetalIngot, ItemName.ChunkOfMetal),
    LocationData(120, LocationName.OldMines_BigKey, ItemName.BigKey),
    LocationData(121, LocationName.OldMines_CrystalCombatPuzzleRoom, ItemName.ExpireRune),
    LocationData(122, LocationName.OldMines_CrystalCartPuzzle, ItemName.Purple_Soulbead),
    LocationData(123, LocationName.OldMines_CelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(124, LocationName.OldMines_Drusus, ItemName.Gaea_Essence),
    LocationData(125, LocationName.GreyleafHamlet_Zako, ItemName.RepairedPitchfork),
    LocationData(126, LocationName.TheRiseSouth_GoblinAmbush_CloseToMystralWoodsEntrance, ItemName.RodOfTheBerserker),
    LocationData(127, LocationName.TheRise_ChestNearLavaGrotto, ItemName.TwentyFiveGreenBeads),
    LocationData(128, LocationName.TheRise_ChestAcrossLava, ItemName.TwentyGreenBeads),
    LocationData(129, LocationName.LavaGrotto_CelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(130, LocationName.LavaGrotto_TorchPuzzleBehindLavaWaterfall, ItemName.PeriodicRune),
    LocationData(131, LocationName.LavaGrotto_RockPillarPurpleBead, ItemName.Purple_Soulbead),
    LocationData(132, LocationName.LavaGrotto_DrainedLavaPoolPurpleBead, ItemName.Purple_Soulbead),
    LocationData(133, LocationName.LavaGrotto_RockPillarToCombatRoomPurpleBead, ItemName.Purple_Soulbead),
    LocationData(134, LocationName.LavaGrotto_Flavius, ItemName.Igni_Essence),
    LocationData(135, LocationName.TheRise_SerpentLockedDoor, ItemName.MystralianElixer),
    LocationData(136, LocationName.TheRise_WaterfallPurpleBead, ItemName.Purple_Soulbead),
    LocationData(137, LocationName.GreyleafHamlet_WaterboundPurpleBead, ItemName.Purple_Soulbead),
    LocationData(138, LocationName.Highlands_CliffsidePurpleBead, ItemName.Purple_Soulbead),
    LocationData(139, LocationName.HighlandsUpper_ManaLily, ItemName.ManaLilyBulb),
    LocationData(140, LocationName.Highlands_PortNecromancerGhostBusters, ItemName.AfterLifeElixer),
    LocationData(141, LocationName.Highlands_SouthernTorchPuzzle, ItemName.Purple_Soulbead),
    LocationData(142, LocationName.TheRise_ChestNearDarkTower, ItemName.Purple_Soulbead),
    LocationData(143, LocationName.MystralWoods_DeepWoods_StrangeOldGoblinRippingYouOff, ItemName.Purple_Soulbead)  #costs 999 green soul beads
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
    LocationData(None, LocationName.Victory, ItemName.Victory, LocationType.Event, True)
]



all_locations: List[LocationData] = test_locations + events
location_name_to_id: Dict[str, LocationData] = {location.name: location for location in all_locations if location.loc_type != LocationType.Event}