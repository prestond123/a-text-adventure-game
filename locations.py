from describable import *
from revealable import *
from inventory import *
from events import *

class Location(Events, Revealable, Describable, Inventory):
    def __init__(self, game, name, config):                                
        Inventory.__init__(self, game, Inventory.from_config(config))
        #Actions.__init__(self, Actions.from_config(config))
        self.name = name
        self.game = game
        self._config = config            

    def get_config(self):
        return self._config     

class Locations(dict):
    def __init__(self, game, config):
        self.game = game
        for location_name in config:            
            #config[location_name]["name"] = location_name
            self[location_name] = Location(game, location_name, config[location_name])

    def is_valid_location_name(self, location_name):
        return location_name in self
        
    def get_location(self, location_name):
        if(self.is_valid_location_name(location_name)):
            return self[location_name]
        return None    
