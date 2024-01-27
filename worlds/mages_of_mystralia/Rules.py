import math

from worlds.generic.Rules import add_rule, add_item_rule
from typing import Set
from .Items import ItemType, all_items
from .Names.LocationNames import LocationName
from .Names.ItemNames import ItemName
from .Names.EntranceNames import EntranceName
from .Locations import LocationType
from BaseClasses import MultiWorld


def set_entrance_rules(multiworld: MultiWorld, player: int):
    pass

def set_access_rules(multiworld, player):
    add_rule(multiworld.get_location(LocationName.Victory, player),
             lambda state: state.has(ItemName.ManaCharm, player))


def set_item_rules(multiworld, player):
    pass