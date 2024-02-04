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
    ItemData(1, ItemName.Spellbook, ItemClassification.progression, ItemType.Wand),
    ItemData(2, ItemName.Immedi, ItemClassification.progression, ItemType.Focus),
    ItemData(3, ItemName.Actus, ItemClassification.progression, ItemType.Focus),
    ItemData(4, ItemName.Creo, ItemClassification.progression, ItemType.Focus),
    ItemData(5, ItemName.Ego, ItemClassification.progression, ItemType.Focus),
    ItemData(6, ItemName.ApprenticeWand, ItemClassification.progression, ItemType.Wand)
]


test_items: List[ItemData] = [
    ItemData(10, ItemName.ManaCharm, ItemClassification.progression, ItemType.Consumable, 5),
    ItemData(11, ItemName.Purple_Soulbead, ItemClassification.progression, ItemType.Currency, 40),
    ItemData(12, ItemName.HealthUpgrade, ItemClassification.useful, ItemType.Upgrade, 5),
    ItemData(13, ItemName.ManaUpgrade, ItemClassification.useful, ItemType.Upgrade, 5),
    ItemData(14, ItemName.FiveGreenBeads, ItemClassification.filler, ItemType.Currency),
    ItemData(15, ItemName.TeleportRune, ItemClassification.useful, ItemType.Rune),
    ItemData(16, ItemName.DetonateRune, ItemClassification.progression, ItemType.Rune),
    ItemData(17, ItemName.RandomRune, ItemClassification.useful, ItemType.Rune),
    ItemData(18, ItemName.ManaLilyBulb, ItemClassification.progression, ItemType.Currency, 4),
    ItemData(19, ItemName.BagOfWares, ItemClassification.progression, ItemType.Quest, 4),
    ItemData(20, ItemName.MoveRune, ItemClassification.progression, ItemType.Rune),
    ItemData(21, ItemName.BigKey, ItemClassification.progression, ItemType.Quest, 10),
    ItemData(22, ItemName.WoodWretchElixer, ItemClassification.useful, ItemType.Upgrade),
    ItemData(23, ItemName.Token, ItemClassification.progression, ItemType.Quest),
    ItemData(24, ItemName.FiftyGreenBeads, ItemClassification.filler, ItemType.Currency, 2),
    ItemData(25, ItemName.HomingRune, ItemClassification.useful, ItemType.Rune),
    ItemData(26, ItemName.IgniWand, ItemClassification.useful, ItemType.Wand),
    ItemData(27, ItemName.ThirtyGreenBeads, ItemClassification.filler, ItemType.Currency),
    ItemData(28, ItemName.RightRune, ItemClassification.progression, ItemType.Rune),
    ItemData(29, ItemName.TwentyFiveGreenBeads, ItemClassification.filler, ItemType.Currency),
    ItemData(30, ItemName.MasteryRune, ItemClassification.filler, ItemType.Rune),
    ItemData(31, ItemName.TenGreenBeads, ItemClassification.filler, ItemType.Currency),
    ItemData(32, ItemName.SkyShard, ItemClassification.progression, ItemType.Quest),
    ItemData(33, ItemName.IceLizardElixer, ItemClassification.useful, ItemType.Upgrade),
    ItemData(34, ItemName.ImpactRune, ItemClassification.progression, ItemType.Rune),
    ItemData(35, ItemName.OverchargeRune, ItemClassification.filler, ItemType.Rune),
    ItemData(36, ItemName.AuraWand, ItemClassification.useful, ItemType.Wand),
    ItemData(37, ItemName.PortalStone, ItemClassification.useful, ItemType.Upgrade),
    ItemData(38, ItemName.ArchmagesRobe, ItemClassification.useful, ItemType.Upgrade),
    ItemData(39, ItemName.TrialWand, ItemClassification.useful, ItemType.Wand),
    ItemData(40, ItemName.ProximityRune, ItemClassification.useful, ItemType.Rune),
    ItemData(41, ItemName.FifteenGreenBeads, ItemClassification.filler, ItemType.Currency),
    ItemData(42, ItemName.TimeRune, ItemClassification.filler, ItemType.Rune),
    ItemData(43, ItemName.Pitchfork, ItemClassification.progression, ItemType.Quest),
    ItemData(44, ItemName.SeventyFiveGreenBeads, ItemClassification.filler, ItemType.Currency),
    ItemData(45, ItemName.BoarMeat, ItemClassification.filler, ItemType.Quest),
    ItemData(46, ItemName.GaeaWand, ItemClassification.useful, ItemType.Wand),
    ItemData(47, ItemName.HotBread, ItemClassification.progression, ItemType.Quest),
    ItemData(48, ItemName.BrokenPortalStone, ItemClassification.progression, ItemType.Quest),
    ItemData(49, ItemName.Flowers, ItemClassification.progression, ItemType.Quest),
    ItemData(50, ItemName.LifeStaff, ItemClassification.useful, ItemType.Wand),
    ItemData(51, ItemName.AquaWand, ItemClassification.useful, ItemType.Wand),
    ItemData(52, ItemName.BounceRune, ItemClassification.progression, ItemType.Rune),
    ItemData(53, ItemName.Badge, ItemClassification.progression, ItemType.Quest),
    ItemData(54, ItemName.DuplicateRune, ItemClassification.progression, ItemType.Rune),
    ItemData(55, ItemName.InverseRune, ItemClassification.filler, ItemType.Rune),
    ItemData(56, ItemName.GhostQueenElixer, ItemClassification.useful, ItemType.Upgrade),
    ItemData(57, ItemName.BottleForSpirits, ItemClassification.progression, ItemType.Quest),
    ItemData(58, ItemName.EtherRune, ItemClassification.filler, ItemType.Rune),
    ItemData(59, ItemName.SizeRune, ItemClassification.filler, ItemType.Rune),
    ItemData(60, ItemName.RainRune, ItemClassification.useful, ItemType.Rune)
]


events: List[EventItemData] = [
    EventItemData(LocationName.MystalWoodsMariesCart, ItemName.FixedMariesCart),
    EventItemData(LocationName.WoodWretchTwiggsFight, ItemName.MystralWoodsCleansed),
    EventItemData(LocationName.MentorGreyleafhamlet, ItemName.EclipseApproaching),
    EventItemData(LocationName.SkyTempleUpperAncientLizardSleet, ItemName.DefeatSleet),
    EventItemData(LocationName.SkyTempleHubCelestialPuzzleTorch, ItemName.SkyTempleTorch),
    EventItemData(LocationName.SkyTempleHubCampsightTorch, ItemName.SkyTempleTorch),
    EventItemData(LocationName.SkyTempleHubNorthTorch, ItemName.SkyTempleTorch),
    EventItemData(LocationName.SkyTempleHubNorthTorchBehindDetonateRock, ItemName.SkyTempleTorch),
    EventItemData(LocationName.SkyTempleHubEastTorchBehindDetonateRock, ItemName.SkyTempleTorch),
    EventItemData(LocationName.TombOfTheMageKing_GhostQueen, ItemName.DefeatGhostQueen),
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
