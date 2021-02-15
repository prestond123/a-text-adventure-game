import utils

class Inventory():
    def __init__(self, inventory):
        self._inventory = inventory
    def from_config(config):
        return utils.get_list("inventory", config)
    def get_inventory_items(self):
        return self._inventory        
    def add_inventory_items(self, items):        
        self._inventory += items        
    def remove_inventory_items(self, items):
        inv = []
        for item in items:
            if(items not in self._inventory):
                inv.append(item)
        self._inventory = inv
    def has_inventory_item(self, item):        
        return item in self._inventory
        

