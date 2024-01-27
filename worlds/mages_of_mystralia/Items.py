from typing import List, NamedTuple, Dict, Optional
from enum import Enum, IntEnum
from BaseClasses import Item, ItemClassification, MultiWorld
from .Names.ItemNames import ItemName
from .Names.LocationNames import LocationName

class ItemType(str, Enum):
   Consumable = "consumables"
   Elixer = "elixer"
   Wand = "wand"
   Robe = "robe"
   Rune = "rune"
   Quest = "quest"
   Event = "event"

class ItemData(NamedTuple):
   ap_id: Optional[int]
   itemName: str
   progression: ItemClassification
   type: ItemType

class EventItemData(ItemData):
    location: str

    def __new__(cls, location, name):
        self = super(ItemData, cls).__new__(cls, (None, name, ItemClassification.progression, ItemType.Event))
        self.location = location
        return self
    
class MagesOfMystraliaItem(Item):
    game: str = "Mages Of Mystralia"



test_items: List[ItemData] = [
    ItemData(2, ItemName.ManaCharm, ItemClassification.progression, ItemType.Consumable),
    ItemData(20, ItemName.FiveGreenBeads, ItemClassification.filler, ItemType.Consumable)
]

events: List[EventItemData] = [
   EventItemData(LocationName.Victory, ItemName.Victory)
]

all_items: List[ItemData] = test_items + events
item_table: Dict[str, ItemData] = {item.itemName: item for item in all_items}

def create_item(name: str, player :int) -> "Item":
    item = item_table[name]
    return MagesOfMystraliaItem(item.itemName, item.progression, item.ap_id, player)


def create_events(multiworld: MultiWorld, player: int):
    for event in events:
        event_item = create_item(event.itemName, player)
        event_location = multiworld.get_location(event.location, player)
        event_location.place_locked_item(event_item)


def create_items(multiworld: MultiWorld, player: int):
    sum_locations = len(multiworld.get_unfilled_locations(player))

    for item in test_items:
        ap_item = create_item(item.itemName, player)
        multiworld.itempool.append(ap_item)
        sum_locations -= 1

    for item in multiworld.random.choices(population=test_items, k=sum_locations):
        ap_item = create_item(item.itemName, player)
        multiworld.itempool.append(ap_item)
