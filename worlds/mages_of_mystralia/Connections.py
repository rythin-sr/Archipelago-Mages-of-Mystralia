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
    ConnectionData(EntranceName.WestHaven_RiseSouth, RegionName.RiseSouth),
    ConnectionData(EntranceName.MystralWoods_GreyleafHamletSouth, RegionName.Greyleaf_Hamlet_South),
    ConnectionData(EntranceName.MystralWoods_PostCart, RegionName.MystralWoodsPostCart),
    ConnectionData(EntranceName.MystralWoodsPostCart_GoblinCamp, RegionName.MystralWoodsGoblinCamp),
    ConnectionData(EntranceName.MystralWoodsGoblinCamp_Lardee, RegionName.MystralWoodsLardeeArea),
    ConnectionData(EntranceName.MystralWoodsLardee_OldMines, RegionName.OldMinesLardeeArea),
    ConnectionData(EntranceName.MystralWoodsLardee_DeepWoods, RegionName.MystralWoodsDeepWoods),
    ConnectionData(EntranceName.MystralWoodsDeepWoods_Twiggs, RegionName.MystralWoodsTwiggs),
    ConnectionData(EntranceName.MystralWoodsDeepWoods_BackWoods, RegionName.MystralWoodsBackWoods),
    ConnectionData(EntranceName.MystralWoodsBackWoods_GreyleafHamletNorth, RegionName.Greyleaf_Hamlet_North),
    ConnectionData(EntranceName.MystralWoodsBackWoods_BackWoodsWest, RegionName.MystralWoodsBackWoodsWest),
    ConnectionData(EntranceName.GreyleaHamletfNorth_GreyleafHamlet, RegionName.Greyleaf_Hamlet),
    ConnectionData(EntranceName.RiseSouth_MystralWoodsBackWoodsWest, RegionName.MystralWoodsBackWoodsWest),
    ConnectionData(EntranceName.RiseSouth_Rise, RegionName.TheRise),
    ConnectionData(EntranceName.Rise_RiseNorth, RegionName.RiseNorth),
    ConnectionData(EntranceName.RiseNorth_SkyTempleFrontDoor, RegionName.SkyTempleFrontDoor),
    ConnectionData(EntranceName.SkyTempleFrontDoor_SkyTempleHubArea, RegionName.SkyTempleHub),
    ConnectionData(EntranceName.SkyTempleHubArea_SkyTempleHubNorth, RegionName.SkyTempleHubNorth),
    ConnectionData(EntranceName.SkyTempleHubArea_SkyTempleHubUpper, RegionName.SkyTempleUpper),
    ConnectionData(EntranceName.RiseUpperLedges, RegionName.RiseUpperLedges),
    ConnectionData(EntranceName.RiseUpperLedges_SkyTemplePostSleet, RegionName.SkyTemplePostSleetArea),
    ConnectionData(EntranceName.RiseUpperLedges_LavaGrotto, RegionName.LavaGrotto),
    ConnectionData(EntranceName.GreyleaHamletSouth_TheHighlands, RegionName.Highlands),
    ConnectionData(EntranceName.MystralWoods_MystralMiningArea, RegionName.MystralWoodsMiningArea),
    ConnectionData(EntranceName.Highlands_Graveyard, RegionName.HighlandsGraveyard),
    ConnectionData(EntranceName.Highlands_HighlandsUpper, RegionName.HighlandsUpperArea),
    ConnectionData(EntranceName.Graveyard_TombOfTheMageKing, RegionName.TombOfMageKing),
    ConnectionData(EntranceName.TombOfTheMageKing_TombOfTheMageKingSecondLevel, RegionName.TombOfMageKing_SecondLevel),
    ConnectionData(EntranceName.TombOfTheMageKingSecondLevel_TombOfTheMageKingThirdLevel, RegionName.TombOfMageKing_ThirdLevel),
    ConnectionData(EntranceName.GreyleafHamlet_GreyleafHamletCaves, RegionName.Greyleaf_Hamlet_Caves),
    ConnectionData(EntranceName.Highlands_SunkenQuarry, RegionName.SunkenQuarry),
    ConnectionData(EntranceName.MystralWoodsMiningArea_OldMines, RegionName.OldMines),
    ConnectionData(EntranceName.OldMinesKeyDoor, RegionName.OldMinesKeyLocked),
    ConnectionData(EntranceName.Rise_DarkTower, RegionName.DarkTower)
]


def create_connections(multiworld: MultiWorld, player: int):
    for connection in connections:
        entrance = multiworld.get_entrance(connection.source_entrance, player)
        target = multiworld.get_region(connection.target, player)

        entrance.connect(target)