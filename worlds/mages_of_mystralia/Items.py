from typing import List, NamedTuple, Dict, Optional
from enum import Enum, IntEnum
from BaseClasses import Item, ItemClassification, MultiWorld
from worlds.AutoWorld import World
from .Names.ItemNames import ItemName
from .Names.LocationNames import LocationName
import logging

class ItemType(str, Enum):
   Consumable = "consumables"
   Currency = "currency"
   Elixer = "elixer"
   Wand = "wand"
   Rune = "rune"
   Focus = "focus" #ie, Immedi, Actus, Creo, Ego
   Upgrade = "upgrade"
   Quest = "quest"
   Event = "event"

class ItemData(NamedTuple):
    ap_id: Optional[int]
    itemName: str
    progression: ItemClassification
    type: ItemType
    quantity: int = 1

class EventItemData(ItemData):
    location: str

    def __new__(cls, location, name):
        self = super(ItemData, cls).__new__(cls, (None, name, ItemClassification.progression, ItemType.Event))
        self.location = location
        return self
    
class MagesOfMystraliaItem(Item):
    game: str = "Mages Of Mystralia"


tutorial_items: List[ItemData] = [
    ItemData(1, ItemName.Spellbook, ItemClassification.progression, ItemType.Focus),
    ItemData(2, ItemName.Immedi, ItemClassification.progression, ItemType.Focus),
    ItemData(3, ItemName.Actus, ItemClassification.progression, ItemType.Focus),
    ItemData(4, ItemName.Creo, ItemClassification.progression, ItemType.Focus),
    ItemData(5, ItemName.Ego, ItemClassification.progression, ItemType.Focus)
]

test_items: List[ItemData] = [
    ItemData(10, ItemName.ManaCharm, ItemClassification.progression, ItemType.Consumable, 5),
    ItemData(11, ItemName.Purple_Soulbead, ItemClassification.progression, ItemType.Currency, 40),
    ItemData(11, ItemName.HealthUpgrade, ItemClassification.useful, ItemType.Upgrade, 5),
    ItemData(11, ItemName.ManaUpgrade, ItemClassification.useful, ItemType.Upgrade, 5),
    ItemData(12, ItemName.FiveGreenBeads, ItemClassification.filler, ItemType.Currency),
    ItemData(13, ItemName.TeleportRune, ItemClassification.useful, ItemType.Rune),
    ItemData(14, ItemName.DetonateRune, ItemClassification.progression, ItemType.Rune),
    ItemData(15, ItemName.RandomRune, ItemClassification.useful, ItemType.Rune),
    ItemData(16, ItemName.ManaLilyBulb, ItemClassification.progression, ItemType.Currency, 4)
]


events: List[EventItemData] = [
   EventItemData(LocationName.Victory, ItemName.Victory)
]


all_items: List[ItemData] = tutorial_items + test_items + events
item_table: Dict[str, ItemData] = {item.itemName: item for item in all_items}


def create_item(name: str, player :int) -> Item:
    item = item_table[name]
    return MagesOfMystraliaItem(item.itemName, item.progression, item.ap_id, player)


def create_events(multiworld: MultiWorld, player: int):
    for event in events:
        event_item = create_item(event.itemName, player)
        event_location = multiworld.get_location(event.location, player)
        event_location.place_locked_item(event_item)


def create_items(multiworld: MultiWorld, world: World, player: int):
    sum_locations = len(multiworld.get_unfilled_locations(player))

    for tutorial_item in tutorial_items:
        ap_item = create_item(tutorial_item.itemName, player)
        world.options.start_inventory.value[ tutorial_item.itemName ] = 1
        multiworld.push_precollected(ap_item)

    for item in test_items:
        for nr in range(item.quantity):
            ap_item = create_item(item.itemName, player)
            multiworld.itempool.append(ap_item)
            sum_locations -= 1

    for item in multiworld.random.choices(population=test_items, k=sum_locations):
        ap_item = create_item(item.itemName, player)
        multiworld.itempool.append(ap_item)
