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
   Essence = "essence" #aura, igni, aqua, gaea
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

base_id: int = 62000

tutorial_items: List[ItemData] = [
    ItemData(base_id + 1, ItemName.Spellbook, ItemClassification.progression, ItemType.Wand),
    ItemData(base_id + 2, ItemName.Immedi, ItemClassification.progression, ItemType.Focus),
    ItemData(base_id + 3, ItemName.Actus, ItemClassification.progression, ItemType.Focus),
    ItemData(base_id + 4, ItemName.Creo, ItemClassification.progression, ItemType.Focus),
    ItemData(base_id + 5, ItemName.Ego, ItemClassification.progression, ItemType.Focus),
    ItemData(base_id + 6, ItemName.ApprenticeWand, ItemClassification.progression, ItemType.Wand)
]


test_items: List[ItemData] = [
    ItemData(base_id + 21, ItemName.ForestKey, ItemClassification.progression, ItemType.Consumable),
    ItemData(base_id + 121, ItemName.TheRiseKey, ItemClassification.progression, ItemType.Consumable),
    ItemData(base_id + 122, ItemName.SkyTempleFrontDoorKey, ItemClassification.progression, ItemType.Consumable),
    ItemData(base_id + 123, ItemName.SkyTempleEasternDoorKey, ItemClassification.progression, ItemType.Consumable),
    ItemData(base_id + 124, ItemName.SkyTempleBossKey, ItemClassification.progression, ItemType.Consumable),
    ItemData(base_id + 125, ItemName.TombEntranceKey, ItemClassification.progression, ItemType.Consumable),
    ItemData(base_id + 126, ItemName.TombMidKey, ItemClassification.progression, ItemType.Consumable),
    ItemData(base_id + 127, ItemName.TombBossKey, ItemClassification.progression, ItemType.Consumable, 2),
    ItemData(base_id + 128, ItemName.HighlandsGraveyardKey, ItemClassification.progression, ItemType.Consumable),
    ItemData(base_id + 129, ItemName.GreyleafHamletKey, ItemClassification.progression, ItemType.Consumable),
    ItemData(base_id + 130, ItemName.OldMinesKey, ItemClassification.progression, ItemType.Consumable),
    ItemData(base_id + 18, ItemName.ManaLilyBulb, ItemClassification.progression, ItemType.Currency, 4),
    ItemData(base_id + 10, ItemName.ManaCharm, ItemClassification.progression, ItemType.Consumable, 5),
    ItemData(base_id + 11, ItemName.Purple_Soulbead, ItemClassification.progression_skip_balancing, ItemType.Currency, 40),
    ItemData(base_id + 12, ItemName.HealthUpgrade, ItemClassification.useful, ItemType.Upgrade, 5),
    ItemData(base_id + 13, ItemName.ManaUpgrade, ItemClassification.useful, ItemType.Upgrade, 5),
    ItemData(base_id + 22, ItemName.WoodWretchElixer, ItemClassification.useful, ItemType.Upgrade),
    ItemData(base_id + 33, ItemName.IceLizardElixer, ItemClassification.useful, ItemType.Upgrade),
    ItemData(base_id + 56, ItemName.GhostQueenElixer, ItemClassification.useful, ItemType.Upgrade),
    ItemData(base_id + 100, ItemName.MystralianElixer, ItemClassification.useful, ItemType.Upgrade),
    ItemData(base_id + 101, ItemName.AfterLifeElixer, ItemClassification.useful, ItemType.Upgrade),
    ItemData(base_id + 37, ItemName.PortalStone, ItemClassification.useful, ItemType.Upgrade),
    ItemData(base_id + 38, ItemName.ArchmagesRobe, ItemClassification.useful, ItemType.Upgrade),

    ItemData(base_id + 64, ItemName.Aura_Essence, ItemClassification.progression, ItemType.Essence),
    ItemData(base_id + 70, ItemName.Aqua_Essence, ItemClassification.progression, ItemType.Essence),
    ItemData(base_id + 72, ItemName.Gaea_Essence, ItemClassification.progression, ItemType.Essence),
    ItemData(base_id + 102, ItemName.Igni_Essence, ItemClassification.progression, ItemType.Essence),

    ItemData(base_id + 32, ItemName.SkyShard, ItemClassification.progression, ItemType.Quest),
    ItemData(base_id + 48, ItemName.BrokenPortalStone, ItemClassification.progression, ItemType.Quest),

    ItemData(base_id + 26, ItemName.IgniWand, ItemClassification.filler, ItemType.Wand),
    ItemData(base_id + 36, ItemName.AuraWand, ItemClassification.filler, ItemType.Wand),
    ItemData(base_id + 46, ItemName.GaeaWand, ItemClassification.filler, ItemType.Wand),
    ItemData(base_id + 51, ItemName.AquaWand, ItemClassification.filler, ItemType.Wand),
    ItemData(base_id + 50, ItemName.LifeStaff, ItemClassification.filler, ItemType.Wand),
    ItemData(base_id + 65, ItemName.Soul_Scepter, ItemClassification.filler, ItemType.Wand),
    ItemData(base_id + 66, ItemName.NegationScepter, ItemClassification.filler, ItemType.Wand),
    ItemData(base_id + 74, ItemName.RodOfTheBerserker, ItemClassification.filler, ItemType.Wand),
    ItemData(base_id + 39, ItemName.TrialWand, ItemClassification.useful, ItemType.Wand),
    
    ItemData(base_id + 15, ItemName.TeleportRune, ItemClassification.filler, ItemType.Rune),
    ItemData(base_id + 16, ItemName.DetonateRune, ItemClassification.progression, ItemType.Rune),
    ItemData(base_id + 17, ItemName.RandomRune, ItemClassification.filler, ItemType.Rune),
    ItemData(base_id + 20, ItemName.MoveRune, ItemClassification.progression, ItemType.Rune),
    ItemData(base_id + 25, ItemName.HomingRune, ItemClassification.useful, ItemType.Rune),
    ItemData(base_id + 28, ItemName.RightRune, ItemClassification.progression, ItemType.Rune),
    ItemData(base_id + 30, ItemName.MasteryRune, ItemClassification.filler, ItemType.Rune),
    ItemData(base_id + 34, ItemName.ImpactRune, ItemClassification.progression, ItemType.Rune),
    ItemData(base_id + 35, ItemName.OverchargeRune, ItemClassification.filler, ItemType.Rune),
    ItemData(base_id + 40, ItemName.ProximityRune, ItemClassification.filler, ItemType.Rune),
    ItemData(base_id + 42, ItemName.TimeRune, ItemClassification.progression, ItemType.Rune),
    ItemData(base_id + 52, ItemName.BounceRune, ItemClassification.progression, ItemType.Rune),
    ItemData(base_id + 54, ItemName.DuplicateRune, ItemClassification.progression, ItemType.Rune),
    ItemData(base_id + 55, ItemName.InverseRune, ItemClassification.filler, ItemType.Rune),
    ItemData(base_id + 58, ItemName.EtherRune, ItemClassification.filler, ItemType.Rune),
    ItemData(base_id + 59, ItemName.SizeRune, ItemClassification.progression, ItemType.Rune),
    ItemData(base_id + 60, ItemName.RainRune, ItemClassification.progression, ItemType.Rune),
    ItemData(base_id + 61, ItemName.SwiftRune, ItemClassification.filler, ItemType.Rune),
    ItemData(base_id + 62, ItemName.LeftRune, ItemClassification.progression, ItemType.Rune),
    ItemData(base_id + 63, ItemName.PushRune, ItemClassification.filler, ItemType.Rune),
    ItemData(base_id + 69, ItemName.AtOnceRune, ItemClassification.filler, ItemType.Rune),
    ItemData(base_id + 71, ItemName.ExpireRune, ItemClassification.filler, ItemType.Rune),
    ItemData(base_id + 76, ItemName.PeriodicRune, ItemClassification.progression, ItemType.Rune)
]

quest_items: List[ItemData] = [
    ItemData(base_id + 19, ItemName.BagOfWares, ItemClassification.progression, ItemType.Quest, 4),
    ItemData(base_id + 23, ItemName.Token, ItemClassification.progression, ItemType.Quest),
    ItemData(base_id + 43, ItemName.Pitchfork, ItemClassification.progression, ItemType.Quest),
    ItemData(base_id + 45, ItemName.BoarMeat, ItemClassification.progression, ItemType.Quest),
    ItemData(base_id + 47, ItemName.HotBread, ItemClassification.progression, ItemType.Quest),
    ItemData(base_id + 49, ItemName.Flowers, ItemClassification.progression, ItemType.Quest),
    ItemData(base_id + 53, ItemName.Badge, ItemClassification.progression, ItemType.Quest),
    ItemData(base_id + 57, ItemName.BottleForSpirits, ItemClassification.progression, ItemType.Quest),
    ItemData(base_id + 67, ItemName.BrokenPitchfork, ItemClassification.progression, ItemType.Quest),
    ItemData(base_id + 68, ItemName.LoavesOfBread, ItemClassification.progression, ItemType.Quest),
    ItemData(base_id + 73, ItemName.ChunkOfMetal, ItemClassification.progression, ItemType.Quest),
]

filler_items: List[ItemData] = [
    ItemData(base_id + 14, ItemName.FiveGreenBeads, ItemClassification.filler, ItemType.Currency),
    ItemData(base_id + 24, ItemName.FiftyGreenBeads, ItemClassification.filler, ItemType.Currency, 3),
    ItemData(base_id + 27, ItemName.ThirtyGreenBeads, ItemClassification.filler, ItemType.Currency),
    ItemData(base_id + 31, ItemName.TenGreenBeads, ItemClassification.filler, ItemType.Currency),
    ItemData(base_id + 75, ItemName.TwentyGreenBeads, ItemClassification.filler, ItemType.Currency),
    ItemData(base_id + 41, ItemName.FifteenGreenBeads, ItemClassification.filler, ItemType.Currency),
    ItemData(base_id + 44, ItemName.SeventyFiveGreenBeads, ItemClassification.filler, ItemType.Currency),
    ItemData(base_id + 29, ItemName.TwentyFiveGreenBeads, ItemClassification.filler, ItemType.Currency, 2),
]


events: List[EventItemData] = [
    EventItemData(LocationName.MystralWoodsMidBoss, ItemName.DefeatGoblinChampion),
    EventItemData(LocationName.MystralWoodsBoss, ItemName.DefeatWoodWretch),
    EventItemData(LocationName.SkyTempleBoss, ItemName.DefeatSleet),
    EventItemData(LocationName.TombOfTheMageKing_GhostQueen, ItemName.DefeatGhostQueen),
    EventItemData(LocationName.GreyleafHamletSageOfAura, ItemName.MeetSageOfAura),
    EventItemData(LocationName.SunkenQuarrySageOfAqua, ItemName.MeetSageOfAqua),
    EventItemData(LocationName.OldMinesSageOfGaea, ItemName.MeetSageOfGaea),
    EventItemData(LocationName.LavaGrottoSageOfIgni, ItemName.MeetSageOfIgni),

    EventItemData(LocationName.SkyTempleHubCelestialPuzzleTorch, ItemName.SkyTempleTorch),
    EventItemData(LocationName.SkyTempleHubCampsightTorch, ItemName.SkyTempleTorch),
    EventItemData(LocationName.SkyTempleHubNorthTorch, ItemName.SkyTempleTorch),
    EventItemData(LocationName.SkyTempleHubNorthTorchBehindDetonateRock, ItemName.SkyTempleTorch),
    EventItemData(LocationName.SkyTempleHubEastTorchBehindDetonateRock, ItemName.SkyTempleTorch),

    EventItemData(LocationName.GreyleafHamlet_RachelMarieQuest, ItemName.BagOfWaresReturned),

    EventItemData(LocationName.TheRise_GhostStatueAcrossLava, ItemName.BottledGhost),
    EventItemData(LocationName.GreyleafHamlet_GraveyardGhostStatue, ItemName.BottledGhost),
    EventItemData(LocationName.HighlandsUpper_GhostStatue, ItemName.BottledGhost),
    EventItemData(LocationName.DarkTowerAerie, ItemName.EclipseStopped)
]


all_items: List[ItemData] = tutorial_items + test_items + events + quest_items + filler_items
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

    for item in multiworld.random.choices(population=filler_items, k=sum_locations):
        ap_item = create_item(item.itemName, player)
        multiworld.itempool.append(ap_item)
