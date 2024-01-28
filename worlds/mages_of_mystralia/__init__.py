import os
import settings
import typing
import threading

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Region, Entrance, \
    LocationProgressType
from .Items import MagesOfMystraliaItem, item_table, all_items, ItemType, create_events, create_items, create_item
from .Locations import MagesOfMystraliaLocation, all_locations, location_name_to_id, LocationType
from .Rules import set_access_rules, set_item_rules, set_entrance_rules
from .Regions import create_regions
from .Connections import create_connections
from .Names.ItemNames import ItemName
from .Names.LocationNames import LocationName
from .Names.RegionNames import RegionName

from worlds.AutoWorld import WebWorld, World


class MagesOfMystraliaWeb(WebWorld):
    theme = "grassFlowers"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Mages Of Mystralia for an Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["rythin"]
    )
    tutorials = [setup_en]


class MagesOfMystraliaWorld(World):
    """
    Mages Of Mystralia implementation, place holder text!
    """
    game = "Mages Of Mystralia"
    topology_present = False

    data_version = 1

    item_name_to_id = {item.itemName: item.ap_id for item in all_items if item.type != ItemType.Event}
    location_name_to_id = {location: location_name_to_id[location].id for location in location_name_to_id}


    web = MagesOfMystraliaWeb()


    def generate_early(self) -> None:
        """
        Called per player before any items or locations are created. You can set properties on your world here.
        Already has access to player options and RNG.
        """
        pass

    def create_regions(self) -> None:
        """
        Called to place player's regions into the MultiWorld's regions list. If it's hard to separate, this can be done
        during generate_early or basic as well.
        """
        create_regions(self.multiworld, self.player)
        create_connections(self.multiworld, self.player)

    def create_items(self) -> None:
        """
        Called to place player's items into the MultiWorld's itempool. After this step all regions and items have to
        be in the MultiWorld's regions and itempool, and these lists should not be modified afterwards.
        """
        create_events(self.multiworld, self.player)
        create_items(self.multiworld, self, self.player)

    def set_rules(self) -> None:
        """
        Called to set access and item rules on locations and entrances.
        """
        set_entrance_rules(self.multiworld, self.player)
        set_item_rules(self.multiworld, self.player)
        set_access_rules(self.multiworld, self.player)
        
        self.multiworld.completion_condition[self.player] = \
            lambda state: state.has(ItemName.Victory, self.player)

    def generate_basic(self) -> None:
        """
        Called after the previous steps. Some placement and player specific randomizations can be done here.
        """
        pass

    
    def get_prefill_items(self):
        """
        If items need to be placed during pre_fill, these items can be determined and created using get_prefill_items
        """
        pass


    # def pre_fill(self) -> None:
    #     """
    #     Is called to modify item placement before the regular fill process and before generate_output. If items need to be placed during pre_fill, these items can be determined and created using get_prefill_items
    #     """
    #     pass

    # def fill_hook(self) -> None:
    #     """
    #     Is called to modify item placement during the regular fill process and before generate_output.
    #     """
    #     pass

    # def post_fill(self) -> None:
    #     """
    #     Is called to modify item placement after the regular fill process and before generate_output.
    #     """
    #     pass


    def generate_output(self, output_directory: str) -> None:
        """
        Creates the output files if there is output to be generated. When this is called, self.multiworld.get_locations(self.player) 
        has all locations for the player, with attribute item pointing to the item. location.item.player can be used to see if it's a local item
        """
        pass

    # def fill_slot_data(self):
    #     """
    #     Can be used to modify the data that will be used by the server to host the MultiWorld.
    #     """
    #     return {name: getattr(self.multiworld, name)[self.player].value for name in self.option_definitions}

    # def modify_multidata(self):
    #     """
    #     Can be used to modify the data that will be used by the server to host the MultiWorld.
    #     """
    #     pass

    @classmethod
    def stage_assert_generate(cls, multiworld: MultiWorld) -> None:
        """
        Called at the start of generation to check the existence of prerequisite files, usually a ROM for games which require one.
        """
        pass

    def create_item(self, name: str) -> Item:
        return create_item(name, self.player)