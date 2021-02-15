from inventory import *

class Player(Inventory):
    def __init__(self, game, config):                
        super().__init__(Inventory.from_config(config))
        self._location_name = config["location-name"]
        self._game = game
    def get_location_name(self):
        return self._location_name
    def set_location_name(self, location_name):
        self._location_name = location_name        
    def get_location(self):
        return self._game.locations.get_location(self.get_location_name())
        
