import utils
from config import *
from player import *
from locations import *
from actions import *
from registry import *
from registry_builder import *
from input_handler import *
import json

class Game():
    def __init__(self, config):        
        self._config = config["game"]        
        self._completed = False
        self._quit = False
        self._registry = Registry()
        RegistryBuilder(self._registry).register_commands()
        
        self._input_handler = InputHandler(self, self._registry)
        #self._actions = config["game"]["actions"]
        
        self.player = Player(self, config["player"])
        self.locations = Locations(self, config["locations"])                                
                          
    def _handle_completed(self):        
        if(self.player.has_inventory_item(self._config["completed-inventory-item"])):
            self.completed = True        
            utils.print_messages(self._config["completed-messages"])
            
    def _handle_quitting(self):
        if(self._quit):
            utils.print_messages(self._config["quitting-messages"])
      
    def _next(self):
        self._input_handler.handle_input()
        #self._player.add_inventory_items([self._config["completed-inventory-item"]]) ## - test completed
        self._handle_completed()
        self._handle_quitting()        

        #self._set_completed() # temp

    def get_config(self):
        return self._config

    def help(self):
        self._registry.help()   

    def get_prompt(self):
        return self._config["prompt"]

    def get_location(self):
        return self.player.get_location()
        
    def quit(self):
        self._quit = True
        
    def run(self):
        while(not (self._completed or self._quit)):
            print("+ visible:", self.get_location().get_inventory_item_names())
            print("+ carrying:", self.player.get_inventory_item_names())
            self._next()
    
    def debug(self, what):
        if(what == "game"):
            print("game", self.get_config())        
        if(what == "player"):
            print("player", self.player.get_config())
            for i in self.player.get_inventory_items():
                print(" ", i)
        if(what == "location"):
            location = self.get_location()            
            print("location-config", location.get_config())
            for i in location.get_inventory_items():
                print(" ", i)
                
game = Game(config)
game.run()
