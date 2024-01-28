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
        LocationName.Haven_HealthFountainOne,
        LocationName.Haven_HealthFountainTwo,
        LocationName.Haven_HealthFountainThree,
        LocationName.Haven_HealthFountainFour,
        LocationName.Haven_HealthFountainFive,
        LocationName.Haven_ManaFountainOne,
        LocationName.Haven_ManaFountainTwo,
        LocationName.Haven_ManaFountainThree,
        LocationName.Haven_ManaFountainFour,
        LocationName.Haven_ManaFountainFive,
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
        LocationName.Placeholder_PurpleBead27,
        LocationName.Placeholder_PurpleBead28,
        LocationName.Placeholder_DetonateRune
    ], [EntranceName.Haven_WindingGlade, EntranceName.Haven_WestHaven_DetonateWall, EntranceName.Haven_MystralWoods]),
    RegionName.WindingGlade: EntranceData(RegionName.WindingGlade, 
    [
        LocationName.WindingGlade_TeleportRunePuzzleRoom
    ]),
    RegionName.WesternHaven: EntranceData(RegionName.WesternHaven, 
    []),
    RegionName.MystralWoods: EntranceData(RegionName.MystralWoods, 
    [
        LocationName.MystralWoods_ManaLilyCelestialPuzzle,
        LocationName.MystralWoods_ManaLily,
        LocationName.Placeholder_ManaLily1,
        LocationName.Placeholder_ManaLily2
    ],
    [
        EntranceName.MystralWoods_GreyleafHamlet
    ]),
    RegionName.Greyleaf_Hamlet: EntranceData(RegionName.Greyleaf_Hamlet,
    [
        LocationName.GreyleafHamlet_ManaLily
    ])
}