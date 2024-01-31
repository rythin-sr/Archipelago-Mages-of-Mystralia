from typing import Callable, List, Dict, NamedTuple, Optional
from enum import Enum
from BaseClasses import Location, MultiWorld
from .Names.LocationNames import LocationName
from .Names.ItemNames import ItemName

class LocationType(str, Enum):
   Item = "Item"
   Event = "Event"


def always_on(multiworld, player):
    return True

class LocationData(NamedTuple):
    id: Optional[int]
    name: str
    vanilla_item: str
    loc_type: LocationType = LocationType.Item
    event: bool = False
    included: Callable[[MultiWorld, int], bool] = always_on


class MagesOfMystraliaLocation(Location):
    game: str = "Mages Of Mystralia"

test_locations = [
    LocationData(1, LocationName.Haven_InfrontOfTower, ItemName.FiveGreenBeads),
    LocationData(2, LocationName.Haven_EnchanterManaLily, ItemName.ManaCharm),

    LocationData(3, LocationName.Haven_ManaLilyTwo, ItemName.ManaCharm), #Costs 20 Green Soul Beads
    LocationData(4, LocationName.Haven_ManaLilyThree, ItemName.ManaCharm), #Costs 20 Green Soul Beads
    LocationData(5, LocationName.Haven_ManaLilyFour, ItemName.ManaCharm), #Costs 20 Green Soul Beads
    LocationData(6, LocationName.Haven_ManaLilyFive, ItemName.ManaCharm), #Costs 20 Green Soul Beads

    LocationData(7, LocationName.Haven_UpgradeFountainOne, ItemName.HealthUpgrade),
    LocationData(8, LocationName.Haven_UpgradeFountainTwo, ItemName.ManaUpgrade),
    LocationData(9, LocationName.Haven_UpgradeFountainThree, ItemName.HealthUpgrade),
    LocationData(10, LocationName.Haven_UpgradeFountainFour, ItemName.ManaUpgrade),
    LocationData(11, LocationName.Haven_UpgradeFountainFive, ItemName.HealthUpgrade),
    LocationData(12, LocationName.Haven_UpgradeFountainSix, ItemName.ManaUpgrade),
    LocationData(13, LocationName.Haven_UpgradeFountainSeven, ItemName.HealthUpgrade),
    LocationData(14, LocationName.Haven_UpgradeFountainEight, ItemName.ManaUpgrade),
    LocationData(15, LocationName.Haven_UpgradeFountainNine, ItemName.HealthUpgrade),
    LocationData(16, LocationName.Haven_UpgradeFountainTen, ItemName.ManaUpgrade),
    
    LocationData(17, LocationName.Haven_UnderBridge, ItemName.Purple_Soulbead),
    LocationData(18, LocationName.Haven_RandomRunePuzzleRoom, ItemName.RandomRune),
    LocationData(19, LocationName.WindingGlade_TeleportRunePuzzleRoom, ItemName.TeleportRune),

    LocationData(20, LocationName.MystralWoods_ManaLilyCelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(21, LocationName.MystralWoods_ManaLily, ItemName.ManaLilyBulb),
    LocationData(23, LocationName.MystralWoods_PostCart_PurpleBeadPuzzleRoom, ItemName.Purple_Soulbead),
    LocationData(24, LocationName.MystralWoods_GoblinCamp_BagOfWares, ItemName.BagOfWares),
    LocationData(25, LocationName.MystralWoods_Lardee_MoveRune, ItemName.MoveRune),
    LocationData(26, LocationName.OldMinesLardee_BagOfWares, ItemName.BagOfWares),
    LocationData(27, LocationName.MystralWoods_DeepWoods_BagOfWaresOne, ItemName.BagOfWares),
    LocationData(28, LocationName.MystralWoods_DeepWoods_StrangeOldGoblin, ItemName.BigKey),
    LocationData(29, LocationName.MystralWoods_DeepWoods_BagOfWaresTwo, ItemName.BagOfWares),
    LocationData(30, LocationName.MystralWoods_Twiggs_LifeElixer, ItemName.WoodWretchElixer),

    LocationData(22, LocationName.GreyleafHamlet_ManaLily, ItemName.ManaLilyBulb) #Costs 99 Green Soul Beads
]

placeholder_locations = [
    LocationData(111, LocationName.Placeholder_PurpleBead1, ItemName.Purple_Soulbead),
    LocationData(112, LocationName.Placeholder_PurpleBead2, ItemName.Purple_Soulbead),
    LocationData(113, LocationName.Placeholder_PurpleBead3, ItemName.Purple_Soulbead),
    LocationData(114, LocationName.Placeholder_PurpleBead4, ItemName.Purple_Soulbead),
    LocationData(115, LocationName.Placeholder_PurpleBead5, ItemName.Purple_Soulbead),
    LocationData(116, LocationName.Placeholder_PurpleBead6, ItemName.Purple_Soulbead),
    LocationData(117, LocationName.Placeholder_PurpleBead7, ItemName.Purple_Soulbead),
    LocationData(118, LocationName.Placeholder_PurpleBead8, ItemName.Purple_Soulbead),
    LocationData(119, LocationName.Placeholder_PurpleBead9, ItemName.Purple_Soulbead),
    LocationData(120, LocationName.Placeholder_PurpleBead10, ItemName.Purple_Soulbead),
    LocationData(121, LocationName.Placeholder_PurpleBead11, ItemName.Purple_Soulbead),
    LocationData(122, LocationName.Placeholder_PurpleBead12, ItemName.Purple_Soulbead),
    LocationData(123, LocationName.Placeholder_PurpleBead13, ItemName.Purple_Soulbead),
    LocationData(124, LocationName.Placeholder_PurpleBead14, ItemName.Purple_Soulbead),
    LocationData(125, LocationName.Placeholder_PurpleBead15, ItemName.Purple_Soulbead),
    LocationData(126, LocationName.Placeholder_PurpleBead16, ItemName.Purple_Soulbead),
    LocationData(127, LocationName.Placeholder_PurpleBead17, ItemName.Purple_Soulbead),
    LocationData(128, LocationName.Placeholder_PurpleBead18, ItemName.Purple_Soulbead),
    LocationData(129, LocationName.Placeholder_PurpleBead19, ItemName.Purple_Soulbead),
    LocationData(130, LocationName.Placeholder_PurpleBead20, ItemName.Purple_Soulbead),
    LocationData(131, LocationName.Placeholder_PurpleBead21, ItemName.Purple_Soulbead),
    LocationData(132, LocationName.Placeholder_PurpleBead22, ItemName.Purple_Soulbead),
    LocationData(133, LocationName.Placeholder_PurpleBead23, ItemName.Purple_Soulbead),
    LocationData(134, LocationName.Placeholder_PurpleBead24, ItemName.Purple_Soulbead),
    LocationData(135, LocationName.Placeholder_PurpleBead25, ItemName.Purple_Soulbead),
    LocationData(136, LocationName.Placeholder_PurpleBead26, ItemName.Purple_Soulbead),
    LocationData(137, LocationName.Placeholder_PurpleBead27, ItemName.Purple_Soulbead),

    LocationData(141, LocationName.Placeholder_ManaLily1, ItemName.ManaLilyBulb),
    LocationData(142, LocationName.Placeholder_ManaLily2, ItemName.ManaLilyBulb),
    LocationData(143, LocationName.Placeholder_DetonateRune, ItemName.DetonateRune)
]

events = [
    LocationData(None, LocationName.MystalWoodsMariesCart, ItemName.FixedMariesCart, LocationType.Event, True),
    LocationData(None, LocationName.Victory, ItemName.Victory, LocationType.Event, True)
]



all_locations: List[LocationData] = test_locations + events + placeholder_locations
location_name_to_id: Dict[str, LocationData] = {location.name: location for location in all_locations if location.loc_type != LocationType.Event}