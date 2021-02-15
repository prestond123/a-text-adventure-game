from inventory import *
from actions import *

class Location(Inventory, Actions):
    def __init__(self, name, config):                
        Inventory.__init__(self, Inventory.from_config(config))
        Actions.__init__(self, Actions.from_config(config))
        self.name = name
class Locations(dict):
    def __init__(self, game, config):
        for location in config:
            self[location] = Location(location, config[location])
    def is_valid_location_name(self, location_name):
        return location_name in self
    def get_location(self, location_name):
        if(self.is_valid_location_name(location_name)):
            return self[location_name]
        return None
    # def is_valid_location_name(location_name, locations):
    #     return location_name in locations

