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
        LocationName.Victory,

        LocationName.Placeholder_PurpleBead1,
        LocationName.Placeholder_PurpleBead2,
        LocationName.Placeholder_PurpleBead3,
        LocationName.Placeholder_PurpleBead4,
        LocationName.Placeholder_PurpleBead5,
        LocationName.Placeholder_PurpleBead6,
        LocationName.Placeholder_PurpleBead7,
        LocationName.Placeholder_PurpleBead8,
        LocationName.Placeholder_PurpleBead9,
        LocationName.Placeholder_PurpleBead10,
        LocationName.Placeholder_PurpleBead11,
        LocationName.Placeholder_PurpleBead12,
        LocationName.Placeholder_PurpleBead13,
        LocationName.Placeholder_PurpleBead14,
        LocationName.Placeholder_PurpleBead15,
        LocationName.Placeholder_PurpleBead16,
        LocationName.Placeholder_PurpleBead17,
        LocationName.Placeholder_PurpleBead18,
        LocationName.Placeholder_PurpleBead19,
        LocationName.Placeholder_PurpleBead20,
        LocationName.Placeholder_PurpleBead21,
        LocationName.Placeholder_PurpleBead22,
        LocationName.Placeholder_PurpleBead23,
        LocationName.Placeholder_PurpleBead24,
        LocationName.Placeholder_PurpleBead25,
        LocationName.Placeholder_PurpleBead26,
        LocationName.Placeholder_PurpleBead27
    ], [EntranceName.Haven_WindingGlade, EntranceName.Haven_WestHaven_DetonateWall, EntranceName.Haven_MystralWoods]),
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
        LocationName.Placeholder_ManaLily1,
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
        LocationName.MystralWoods_DeepWoods_StrangeOldGoblin
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
    ],
    [

    ]),
    RegionName.Greyleaf_Hamlet_South: EntranceData(RegionName.Greyleaf_Hamlet_South,
    [
        LocationName.GreyleafHamlet_ManaLily
    ], 
    [
        EntranceName.GreyleaHamletfSouth_GreyleafHamlet,
        EntranceName.GreyleaHamletSouth_TheHighlands
    ]),
    RegionName.Greyleaf_Hamlet_North: EntranceData(RegionName.Greyleaf_Hamlet_North,
    [
        LocationName.MentorGreyleafhamlet
    ], 
    [
        EntranceName.GreyleaHamletfNorth_GreyleafHamlet
    ]),
    RegionName.Greyleaf_Hamlet: EntranceData(RegionName.Greyleaf_Hamlet,
    [
        LocationName.GreyleafHamlet_JeffsGiftForwife,
        LocationName.GreyleafHamlet_MariesBagOfWaresResult
    ], 
    [

    ]),
    RegionName.RiseSouth: EntranceData(RegionName.RiseSouth,
    [
        LocationName.TheRiseSouth_CelestialPuzzle_CloseToMystralWoodsEntrance,
        LocationName.TheRiseSouth_StrangeMan_IgniWand,
        LocationName.TheRiseSouth_TorchPuzzleNearRopeBridges
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
        LocationName.TheRise_ManaLily
    ], 
    [
        EntranceName.Rise_RiseNorth,
        EntranceName.Rise_LavaGrotto
    ]),
    RegionName.RiseNorth: EntranceData(RegionName.RiseNorth,
    [
        LocationName.TheRiseNorth_HiddenUnderStairsPurpleSoulBead,
        LocationName.TheRiseNorth_RuinsTorchPuzzle
    ], 
    [
        EntranceName.RiseNorth_SkyTempleFrontDoor
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
        LocationName.SkyTempleUpperAncientLizardSleet,
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
    ],
    [
        
    ]),
    RegionName.LavaGrotto: EntranceData(RegionName.LavaGrotto, 
    [ 
    ],
    [
        
    ])
}