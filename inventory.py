import utils
from describable import *
from openable import *
from takeable import *
from dropable import *
from unlockable import *
from revealable import *

class Inventory():
    def __init__(self, game, inventory):
        self._inventory = inventory
        self.game = game
        
    def from_config(config):
        return utils.get_dict("inventory", config)
    
    def has_inventory(self):
        return len(self._inventory) > 0

    def has_inventory_item(self, name):        
        return name in self._inventory
    
    def get_inventory_items(self):        
        items = {}
        for name in self._inventory:
            items[name] = InventoryItem(self, name, self._inventory[name])
        return items

    def get_inventory_item(self, name):
        return InventoryItem(self, name, self._inventory[name])
        
    def get_inventory_item_names(self):
        return sorted(self._inventory)
    
    def _unwrap(self, items):
        unwrapped = {}
        for name in items:
            item = items[name]
            t = type(item)
            ### print(t)
            if(not type(item)==dict):
                c = item.get_config()
                unwrapped[name] = c
            else:
                unwrapped[name] = item      
        return unwrapped
        
    def add_inventory_items(self, items):                                      
        self._inventory = {**self._inventory, **self._unwrap(items)}
        
    def add_inventory_item(self, name, item):
        unwraped = self._unwrap({name: item})[name]
        if(not type(item)==dict):
            self._inventory[name] = item.get_config()
        else:
            self._inventory[name] = item

    def remove_inventory_items(self, items):        
        inv = []
        for item in items:
            if(items not in self._inventory):
                inv.append(item)
        self._inventory = inv
    def remove_inventory_item(self, name):        
        self._inventory.pop(name)    
    
class InventoryItem(Inventory, Revealable, Takeable, Dropable, Openable, Describable, Unlockable):
    def __init__(self, inventory, name, config):
        Inventory.__init__(self, inventory.game, Inventory.from_config(config))  
        self.name = name
        self._config = config
    def get_config(self):
        return self._config    