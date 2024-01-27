from typing import List, Dict
from BaseClasses import MultiWorld, Region, Entrance
from .Locations import MagesOfMystraliaLocation, location_name_to_id, LocationType
from . import ItemType
from .Names.LocationNames import LocationName
from .Names.RegionNames import RegionName
from .Names.EntranceNames import EntranceName


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
        LocationName.Victory
    ])
}