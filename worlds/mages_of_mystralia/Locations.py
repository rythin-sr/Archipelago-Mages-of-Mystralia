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
    #these should be progressive
    LocationData(3, LocationName.Haven_ManaLilyTwo, ItemName.ManaCharm),
    LocationData(4, LocationName.Haven_ManaLilyThree, ItemName.ManaCharm),
    LocationData(5, LocationName.Haven_ManaLilyFour, ItemName.ManaCharm),
    LocationData(6, LocationName.Haven_ManaLilyFive, ItemName.ManaCharm),

    #these should be progressive
    LocationData(7, LocationName.Haven_HealthFountainOne, ItemName.HealthUpgrade),
    LocationData(8, LocationName.Haven_HealthFountainTwo, ItemName.HealthUpgrade),
    LocationData(9, LocationName.Haven_HealthFountainThree, ItemName.HealthUpgrade),
    LocationData(10, LocationName.Haven_HealthFountainFour, ItemName.HealthUpgrade),
    LocationData(11, LocationName.Haven_HealthFountainFive, ItemName.HealthUpgrade),

    #these should be progressive
    LocationData(12, LocationName.Haven_ManaFountainOne, ItemName.ManaUpgrade),
    LocationData(13, LocationName.Haven_ManaFountainTwo, ItemName.ManaUpgrade),
    LocationData(14, LocationName.Haven_ManaFountainThree, ItemName.ManaUpgrade),
    LocationData(15, LocationName.Haven_ManaFountainFour, ItemName.ManaUpgrade),
    LocationData(16, LocationName.Haven_ManaFountainFive, ItemName.ManaUpgrade),
    
    LocationData(17, LocationName.Haven_UnderBridge, ItemName.Purple_Soulbead),
    LocationData(18, LocationName.Haven_RandomRunePuzzleRoom, ItemName.RandomRune),
    LocationData(19, LocationName.WindingGlade_TeleportRunePuzzleRoom, ItemName.TeleportRune),

    LocationData(20, LocationName.MystralWoods_ManaLilyCelestialPuzzle, ItemName.Purple_Soulbead),
    LocationData(21, LocationName.MystralWoods_ManaLily, ItemName.ManaLilyBulb),

    LocationData(22, LocationName.GreyleafHamlet_ManaLily, ItemName.ManaLilyBulb)
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
    LocationData(138, LocationName.Placeholder_PurpleBead28, ItemName.Purple_Soulbead),
    LocationData(139, LocationName.Placeholder_ManaLily1, ItemName.ManaLilyBulb),
    LocationData(140, LocationName.Placeholder_ManaLily2, ItemName.ManaLilyBulb),
    LocationData(141, LocationName.Placeholder_DetonateRune, ItemName.DetonateRune)
]

events = [
    LocationData(None, LocationName.Victory, ItemName.Victory, LocationType.Event, True)
]



all_locations: List[LocationData] = test_locations + events + placeholder_locations
location_name_to_id: Dict[str, LocationData] = {location.name: location for location in all_locations if location.loc_type != LocationType.Event}