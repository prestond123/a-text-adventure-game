import utils
from describable import *
from openable import *
from takeable import *
class InventoryItem(Takeable, Openable, Describable):
    def __init__(self, name, config):
        self.name = name
        self._config = config
    def get_config(self):
        return self._config
    def has_inventory(self):
        return "inventory" in self._config
    def get_inventory(self):
        return self._config["inventory"]
    def add_inventory(self, items):
        if("inventory" not in self._config):
            self._config["inventory"] = {}
        self._config["inventory"] = {**self._config["inventory"], **items}
class Inventory():
    def __init__(self, inventory):
        self._inventory = inventory
    def from_config(config):
        return utils.get_dict("inventory", config)
    def get_inventory_items(self):
        return self._inventory        
    def add_inventory_items(self, items):        
        self._inventory = {**self._inventory, **items}
    def remove_inventory_items(self, items):
        inv = []
        for item in items:
            if(items not in self._inventory):
                inv.append(item)
        self._inventory = inv
    def has_inventory_item(self, name):        
        return name in self._inventory
    def get_inventory_item(self, name):
        return InventoryItem(name, self._inventory[name])
    def add_inventory_item(self, name, inventory_item):        
        self._inventory[name] = inventory_item

    