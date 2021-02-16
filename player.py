from inventory import *

class Player(Inventory):
    def __init__(self, game, config):                
        Inventory.__init__(self, game, Inventory.from_config(config))        
        self._config = config
        self._game = game
    def get_location_name(self):
        return self._config["location-name"]
    def set_location_name(self, location_name):
        self._config["location-name"] = location_name        
    def get_location(self):
        return self._game.locations.get_location(self.get_location_name())
        
