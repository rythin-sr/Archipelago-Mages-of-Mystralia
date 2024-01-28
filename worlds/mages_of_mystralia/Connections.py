from typing import Callable, List, Optional
from BaseClasses import MultiWorld, Entrance, CollectionState
from . import ItemType
from .Names.RegionNames import RegionName
from .Names.EntranceNames import EntranceName


class ConnectionData:
    source_entrance: str
    target: str

    def __init__(self, _source_entrance: str, _target: str):
        self.source_entrance = _source_entrance
        self.target = _target

connections: List[ConnectionData] = \
[
    ConnectionData(EntranceName.Menu_StartGame, RegionName.Haven),
    ConnectionData(EntranceName.Haven_WestHaven_DetonateWall, RegionName.WesternHaven),
    ConnectionData(EntranceName.Haven_WindingGlade, RegionName.WindingGlade),
    ConnectionData(EntranceName.Haven_MystralWoods, RegionName.MystralWoods),
    ConnectionData(EntranceName.MystralWoods_GreyleafHamlet, RegionName.Greyleaf_Hamlet)
]


def create_connections(multiworld: MultiWorld, player: int):
    for connection in connections:
        entrance = multiworld.get_entrance(connection.source_entrance, player)
        target = multiworld.get_region(connection.target, player)

        entrance.connect(target)