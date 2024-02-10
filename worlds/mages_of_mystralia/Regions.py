from typing import List, Dict
from BaseClasses import MultiWorld, Region, Entrance
from .Locations import MagesOfMystraliaLocation, location_name_to_id, LocationType
from . import ItemType
from .Names.LocationNames import LocationName
from .Names.RegionNames import RegionName
from .Names.EntranceNames import EntranceName
import logging


class EntranceData:
    name: str
    locations: List[str]
    exits: List[str]

    def __init__(self, _name: str, _locations: List[str] = None, _exits: List[str] = None):
        if _locations is None:
            _locations = []

        if _exits is None:
            _exits = []

        self.name = _name
        self.locations = _locations
        self.exits = _exits


def create_region(multiworld: MultiWorld, player: int, regionData: EntranceData):
    region = Region(regionData.name, player, multiworld)
    for location in regionData.locations:
        location_data = location_name_to_id.get(location, None)

        if location_data is None:
            loc = MagesOfMystraliaLocation(player, location, None, region)
        else:
            loc = MagesOfMystraliaLocation(player, location, location_data.id, region)

        region.locations.append(loc)

    for regionExit in regionData.exits:
        region.create_exit(regionExit)

    multiworld.regions.append(region)


def create_regions(multiworld: MultiWorld, player: int):
    for region in regions.values():
        create_region(multiworld, player, region)

regions: Dict[str, EntranceData] = {
    RegionName.Menu: EntranceData(RegionName.Menu, None, [EntranceName.Menu_StartGame]),
    RegionName.Haven: EntranceData(RegionName.Haven,
    [
        LocationName.Haven_InfrontOfTower,
        LocationName.Haven_EnchanterManaLily,
        LocationName.Haven_ManaLilyTwo,
        LocationName.Haven_ManaLilyThree,
        LocationName.Haven_ManaLilyFour,
        LocationName.Haven_ManaLilyFive,
        LocationName.Haven_UnderBridge,
        LocationName.Haven_UpgradeFountainOne,
        LocationName.Haven_UpgradeFountainTwo,
        LocationName.Haven_UpgradeFountainThree,
        LocationName.Haven_UpgradeFountainFour,
        LocationName.Haven_UpgradeFountainFive,
        LocationName.Haven_UpgradeFountainSix,
        LocationName.Haven_UpgradeFountainSeven,
        LocationName.Haven_UpgradeFountainEight,
        LocationName.Haven_UpgradeFountainNine,
        LocationName.Haven_UpgradeFountainTen,
        LocationName.Haven_RandomRunePuzzleRoom,
        LocationName.Haven_PortalStone,
        LocationName.Haven_HallOfTrialsWaveFour,
        LocationName.Haven_HallOfTrialsWaveEight,
        LocationName.Haven_HallOfTrialsWaveTwelve,
        LocationName.Haven_HallOfTrialsTenMinutes,
        LocationName.Haven_ChestNearManaFountain
    ], 
    [
        EntranceName.Haven_WindingGlade, 
        EntranceName.Haven_WestHaven_DetonateWall, 
        EntranceName.Haven_MystralWoods
    ]),
    RegionName.WindingGlade: EntranceData(RegionName.WindingGlade, 
    [
        LocationName.WindingGlade_TeleportRunePuzzleRoom
    ]),
    RegionName.WesternHaven: EntranceData(RegionName.WesternHaven, 
    [
        LocationName.HavenWest_RemoteDetonateRock
    ],
    [
        EntranceName.WestHaven_RiseSouth
    ]),
    RegionName.MystralWoods: EntranceData(RegionName.MystralWoods, 
    [
        LocationName.MystralWoods_ManaLilyCelestialPuzzle,
        LocationName.MystralWoods_ManaLily,
        LocationName.MystalWoodsMariesCart,
        LocationName.MystralWoods_TorchPuzzleOverchargeRune
    ],
    [
        EntranceName.MystralWoods_GreyleafHamletSouth,
        EntranceName.MystralWoods_PostCart,
        EntranceName.MystralWoods_MystralMiningArea
    ]),
    RegionName.MystralWoodsPostCart: EntranceData(RegionName.MystralWoodsPostCart, 
    [
        LocationName.MystralWoods_PostCart_PurpleBeadPuzzleRoom
    ],
    [
        EntranceName.MystralWoodsPostCart_GoblinCamp
    ]),
    RegionName.MystralWoodsGoblinCamp: EntranceData(RegionName.MystralWoodsGoblinCamp, 
    [
        LocationName.MystralWoods_GoblinCamp_BagOfWares
    ],
    [
        EntranceName.MystralWoodsGoblinCamp_Lardee
    ]),
    RegionName.MystralWoodsLardeeArea: EntranceData(RegionName.MystralWoodsLardeeArea, 
    [ 
        LocationName.MystralWoods_Lardee_MoveRune,
        LocationName.MystralWoods_SuperLardee_AuraWand
    ],
    [
        EntranceName.MystralWoodsLardee_OldMines,
        EntranceName.MystralWoodsLardee_DeepWoods
    ]),
    RegionName.MystralWoodsDeepWoods: EntranceData(RegionName.MystralWoodsDeepWoods, 
    [ 
        LocationName.MystralWoods_DeepWoods_BagOfWaresOne,
        LocationName.MystralWoods_DeepWoods_BagOfWaresTwo,
        LocationName.MystralWoods_DeepWoods_StrangeOldGoblin,
        LocationName.MystralWoods_DeepWoods_StrangeOldGoblinRippingYouOff
    ],
    [
        EntranceName.MystralWoodsDeepWoods_Twiggs,
        EntranceName.MystralWoodsDeepWoods_BackWoods
    ]),
    RegionName.MystralWoodsTwiggs: EntranceData(RegionName.MystralWoodsTwiggs, 
    [
        LocationName.WoodWretchTwiggsFight,
        LocationName.MystralWoods_Twiggs_LifeElixer
    ],
    [
    ]),
    RegionName.MystralWoodsBackWoods: EntranceData(RegionName.MystralWoodsBackWoods, 
    [ 

    ],
    [
        EntranceName.MystralWoodsBackWoods_GreyleafHamletNorth,
        EntranceName.MystralWoodsBackWoods_BackWoodsWest
    ]),
    RegionName.MystralWoodsBackWoodsWest: EntranceData(RegionName.MystralWoodsBackWoodsWest, 
    [ 
        LocationName.MystralWoods_Backwoods_DetonateTorch
    ],
    [

    ]),
    RegionName.MystralWoodsMiningArea: EntranceData(RegionName.MystralWoodsMiningArea, 
    [ 
        LocationName.MystralWoodsMiningArea_PuzzleInTheOldMines,
        LocationName.MystralWoodsMiningArea_TorchesInTheRiver,
        LocationName.MystralWoodsMiningArea_WoodedCombatPuzzle
    ],
    [
        EntranceName.MystralWoodsMiningArea_OldMines
    ]),
    RegionName.Greyleaf_Hamlet_South: EntranceData(RegionName.Greyleaf_Hamlet_South,
    [
        LocationName.GreyleafHamlet_ManaLily,
        LocationName.GreyleafHamlet_WaterboundPurpleBead
    ], 
    [
        EntranceName.GreyleaHamletSouth_TheHighlands
    ]),
    RegionName.Greyleaf_Hamlet_North: EntranceData(RegionName.Greyleaf_Hamlet_North,
    [
        LocationName.MentorGreyleafhamlet,
        LocationName.GreyleafHamlet_GraveyardGhostStatue
    ], 
    [
        EntranceName.GreyleaHamletfNorth_GreyleafHamlet
    ]),
    RegionName.Greyleaf_Hamlet: EntranceData(RegionName.Greyleaf_Hamlet,
    [
        LocationName.GreyleafHamlet_JeffsGiftForwife,
        LocationName.GreyleafHamlet_MariesBagOfWaresResult,
        LocationName.GreyleafHamlet_FireRainPuzzle, #burning greyleaf
        LocationName.GreyleafHamlet_BurnedTowerPuzzle, #burning greyleaf
        LocationName.GreyleafHamlet_BarTorchPuzzleRoom, #burning greyleaf
        LocationName.GreyleafHamlet_SavedTheCitizens, #burning greyleaf
        LocationName.GreyleafHamlet_LedgeCombatPuzzleRoom, #burning greyleaf
        LocationName.GreyleafHamlet_JeffsThankYouGift, #post burning greyleaf
        LocationName.GreyleafHamlet_Xavier, #post burning greyleaf
        LocationName.GreyleafHamlet_Zako #post burning greyleaf
    ], 
    [
        EntranceName.GreyleafHamlet_GreyleafHamletCaves
    ]),
    RegionName.Greyleaf_Hamlet_Caves: EntranceData(RegionName.Greyleaf_Hamlet_Caves,
    [
        LocationName.GreyleafHamletCave_CelestialPuzzle,
        LocationName.GreyleafHamletCave_Blasius
    ], 
    [
    ]),
    RegionName.RiseSouth: EntranceData(RegionName.RiseSouth,
    [
        LocationName.TheRiseSouth_CelestialPuzzle_CloseToMystralWoodsEntrance,
        LocationName.TheRiseSouth_StrangeMan_IgniWand,
        LocationName.TheRiseSouth_TorchPuzzleNearRopeBridges,
        LocationName.TheRiseSouth_GoblinAmbush_CloseToMystralWoodsEntrance,
        LocationName.TheRise_SerpentLockedDoor,
        LocationName.TheRise_WaterfallPurpleBead
    ], 
    [
        EntranceName.RiseSouth_MystralWoodsBackWoodsWest,
        EntranceName.RiseSouth_Rise
    ]),
    RegionName.TheRise: EntranceData(RegionName.TheRise,
    [
        LocationName.TheRise_SecretRuinsPath,
        LocationName.TheRise_RightRune,
        LocationName.TheRise_RightRunePuzzle,
        LocationName.TheRise_ManaLily,
        LocationName.TheRise_ChestNearDarkTower
    ], 
    [
        EntranceName.Rise_RiseNorth,
        EntranceName.RiseUpperLedges,
        EntranceName.Rise_DarkTower
    ]),
    RegionName.RiseNorth: EntranceData(RegionName.RiseNorth,
    [
        LocationName.TheRiseNorth_HiddenUnderStairsPurpleSoulBead,
        LocationName.TheRiseNorth_RuinsTorchPuzzle,
        LocationName.TheRiseNorth_TravelingMerchantAnna
    ], 
    [
        EntranceName.RiseNorth_SkyTempleFrontDoor
    ]),
    RegionName.RiseUpperLedges: EntranceData(RegionName.RiseUpperLedges,
    [
        LocationName.TheRise_BouncePuzzle,
        LocationName.TheRise_ChestNearLavaGrotto,
        LocationName.TheRise_ChestAcrossLava,
        LocationName.TheRise_GhostStatueAcrossLava
    ], 
    [
        EntranceName.RiseUpperLedges_LavaGrotto,
        EntranceName.RiseUpperLedges_SkyTemplePostSleet
    ]),
    RegionName.SkyTempleFrontDoor: EntranceData(RegionName.SkyTempleFrontDoor,
    [
        LocationName.SkyTempleFrontDoorTorchPuzzle
    ], 
    [
        EntranceName.SkyTempleFrontDoor_SkyTempleHubArea
    ]),
    RegionName.SkyTempleHub: EntranceData(RegionName.SkyTempleHub,
    [
        LocationName.SkyTempleHubDetonateRock,
        LocationName.SkyTempleHubCelestialPuzzleTorch,
        LocationName.SkyTempleHubCampsightTorch,
        LocationName.SkyTempleHubEastBigKey,
        LocationName.SkyTempleHubEastPurpleSoulbeadBehindDetonate,
        LocationName.SkyTempleHubEastTorchBehindDetonateRock,
        LocationName.SkyTempleHubEastPuzzleRoomBehindDetonateRock,
        LocationName.SkyTempleHubChestBehindDetonateRock,
        LocationName.SkyTempleHubPuzzleMasteryRune
    ], 
    [
        EntranceName.SkyTempleHubArea_SkyTempleHubNorth,
        EntranceName.SkyTempleHubArea_SkyTempleHubUpper
    ]),
    RegionName.SkyTempleHubNorth: EntranceData(RegionName.SkyTempleHubNorth,
    [
        LocationName.SkyTempleHubNorthDetonateRune,
        LocationName.SkyTempleHubNorthTorch,
        LocationName.SkyTempleHubNorthTorchBehindDetonateRock
    ], 
    [
    ]),
    RegionName.SkyTempleUpper: EntranceData(RegionName.SkyTempleUpper,
    [
        LocationName.SkyTempleUpperBigKey,
        LocationName.SkyTempleUpperCombatPuzzleRoom,
        LocationName.SkyTempleUpperAncientLizardSleet
    ], 
    [
    ]),
    RegionName.SkyTemplePostSleetArea: EntranceData(RegionName.SkyTemplePostSleetArea,
    [
        LocationName.SkyTempleUpperSleetsRemains,
        LocationName.SkyTempleUpperIceLizardElixerChest,
        LocationName.SkyTempleUpperCelestialPuzzleNearRemains,
        LocationName.TheRistNorthUpperLedge_ImpactRune
    ], 
    [
    ]),
    RegionName.OldMinesLardeeArea: EntranceData(RegionName.OldMinesLardeeArea, 
    [ 
        LocationName.OldMinesLardee_BagOfWares,
        LocationName.OldMinesLardee_PurpleBeadDetonateRock
    ],
    [
        
    ]),
    RegionName.Highlands: EntranceData(RegionName.Highlands, 
    [
        LocationName.Highlands_Farmer,
        LocationName.Highlands_Pitchfork,
        LocationName.Highlands_Fisherman,
        LocationName.Highlands_GuardTowerStealthPuzzle,
        LocationName.Highlands_Baker,
        LocationName.Highlands_Beggar,
        LocationName.Highlands_TownsPersonOnPlatform,
        LocationName.Highlands_Boar,
        LocationName.Highlands_ChestOnSmallLandAcrossWater,
        LocationName.Highlands_SewerCelestialPuzzle,
        LocationName.Highlands_WaterWalkingTorchPuzzle,
        LocationName.Highlands_PortBadge,
        LocationName.Highlands_PortNecromancer,
        LocationName.Highlands_CliffsidePurpleBead,
        LocationName.Highlands_PortNecromancerGhostBusters,
        LocationName.Highlands_SouthernTorchPuzzle,
        LocationName.Highlands_CousinsFarmer, #accessible post fire greyleaf hamlet
        LocationName.Highlands_BakerTwo #accessible post fire greyleaf hamlet
    ],
    [
        EntranceName.Highlands_Graveyard,
        EntranceName.Highlands_SunkenQuarry
    ]),
    RegionName.HighlandsGraveyard: EntranceData(RegionName.HighlandsGraveyard, 
    [ 
        LocationName.Graveyard_StatueBigKey
    ],
    [
        EntranceName.Graveyard_TombOfTheMageKing,
        EntranceName.Highlands_HighlandsUpper
    ]),
    RegionName.HighlandsUpperArea: EntranceData(RegionName.HighlandsUpperArea, 
    [ 
        LocationName.HighlandsUpper_BounceTorchPuzzle,
        LocationName.HighlandsUpper_CelestialPuzzle,
        LocationName.HighlandsUpper_LowerTorchPuzzle,
        LocationName.HighlandsUpper_GoblinBreadThieves,
        LocationName.HighlandsUpper_GhostStatue,
        LocationName.HighlandsUpper_ManaLily
    ],
    [
    ]),
    RegionName.TombOfMageKing: EntranceData(RegionName.TombOfMageKing, 
    [
        LocationName.TombOfTheMageKing_BigKeyOne,
        LocationName.TombOfTheMageKing_SwampyPurpleBeadChest
    ],
    [
        EntranceName.TombOfTheMageKing_TombOfTheMageKingSecondLevel
    ]),
    RegionName.TombOfMageKing_SecondLevel: EntranceData(RegionName.TombOfMageKing_SecondLevel, 
    [ 
        LocationName.TombOfTheMageKing_DuplicateRuneChest,
        LocationName.TombOfTheMageKing_DuplicatePuzzleRoom,
        LocationName.TombOfTheMageKing_BigKeyTwo,
        LocationName.TombOfTheMageKing_CelestialPuzzle
    ],
    [
        EntranceName.TombOfTheMageKingSecondLevel_TombOfTheMageKingThirdLevel
    ]),
    RegionName.TombOfMageKing_ThirdLevel: EntranceData(RegionName.TombOfMageKing_ThirdLevel, 
    [ 
        LocationName.TombOfTheMageKing_BigKeyThree,
        LocationName.TombOfTheMageKing_BeamPuzzle,
        LocationName.TombOfTheMageKing_BigKeyFour,
        LocationName.TombOfTheMageKing_PuzzleRoomInverseRune,
        LocationName.TombOfTheMageKing_GhostQueen,
        LocationName.TombOfTheMageKing_GhostQueenLifeElixer
    ],
    [
        
    ]),
    RegionName.SunkenQuarry: EntranceData(RegionName.SunkenQuarry, 
    [
        LocationName.SunkenQuarry_HiddenPuzzleRoomNorthWest,
        LocationName.SunkenQuarry_LedgePuzzleRoomSouthEast,
        LocationName.SunkenQuarry_SouthEastCactusChest,
        LocationName.SunkenQuarry_CelestialPuzzleNorthEast,
        LocationName.SunkenQuarry_NorthWaterChest,
        LocationName.SunkenQuarry_NorthCombatArenaChest,
        LocationName.SunkenQuarry_Caelius #locked behind the royal blobs boss fight
    ],
    [
        
    ]),
    RegionName.OldMines: EntranceData(RegionName.OldMines, 
    [ 
        LocationName.OldMines_MetalIngot,
        LocationName.OldMines_BigKey,
        LocationName.OldMines_CrystalCombatPuzzleRoom
    ],
    [
        EntranceName.OldMinesKeyDoor
    ]),
    RegionName.OldMinesKeyLocked: EntranceData(RegionName.OldMinesKeyLocked, 
    [ 
        LocationName.OldMines_CrystalCartPuzzle,
        LocationName.OldMines_CelestialPuzzle,
        LocationName.OldMines_Drusus
    ],
    [
        
    ]),
    RegionName.LavaGrotto: EntranceData(RegionName.LavaGrotto, 
    [ 
        LocationName.LavaGrotto_CelestialPuzzle,
        LocationName.LavaGrotto_TorchPuzzleBehindLavaWaterfall,
        LocationName.LavaGrotto_RockPillarPurpleBead,
        LocationName.LavaGrotto_DrainedLavaPoolPurpleBead,
        LocationName.LavaGrotto_RockPillarToCombatRoomPurpleBead,
        LocationName.LavaGrotto_Flavius
    ],
    [
        
    ]),
    RegionName.DarkTower: EntranceData(RegionName.DarkTower, 
    [ 
        LocationName.DarkTowerAerie
    ],
    [
        
    ])
}