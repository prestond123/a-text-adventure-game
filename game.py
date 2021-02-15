import utils
from config import *
from game import *
from player import *
from locations import *
from actions import *
from registry import *
from registry_builder import *
from input_handler import *

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
        
    def _is_quitting(self):
        return self._quit

    def _update_completed(self):
        if(self.player.has_inventory_item(self._config["completed-inventory-item"])):
            self._set_completed()                
    def _set_completed(self):
        self._completed = True                 
    def _is_completed(self):
        return self._completed

    def _handler_completed(self):
        if(self._is_completed()):
            utils.print_messages(self._config["completed-messages"])
            
    def _handler_quitting(self):
        if(self._is_quitting()):
            utils.print_messages(self._config["quitting-messages"])

    def _handle_state(self):
        self._update_completed()
        self._handler_completed()
        self._handler_quitting()        

    def _next(self):
        self._input_handler.handle_input()
        #self._player.add_inventory_items([self._config["completed-inventory-item"]]) ## - test completed
        self._handle_state()                        
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
        while(not (self._is_completed() or self._is_quitting())):
            print("visible:", sorted(self.get_location().get_inventory_items()))
            print("carrying:", sorted(self.player.get_inventory_items()))
            self._next()
    
    def debug(self):
        print("game", self.get_config())
        print("player", self.player.get_inventory_items())
        print("location", self.get_location().get_config())
        print("location inv", self.get_location().get_inventory_items())

Game(config).run()
