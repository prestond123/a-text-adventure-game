import utils
from config import *
from game import *
from player import *
from locations import *
from actions import *
from registry import *
from registry_builder import *
from input_handler import *

class Game(Actions):
    def __init__(self, config):
        super().__init__(Actions.from_config(config["game"]))        
        self._completed_inventory_item = config["game"]["completed-inventory-item"]
        self._completed_messages = config["game"]["completed-messages"]
        self._quitting_messages = config["game"]["quitting-messages"]
        self._completed = False
        self._quit = False
        self._registry = Registry()
        RegistryBuilder(self._registry).register_commands()
        
        self._input_handler = InputHandler(self, self._registry)
        #self._actions = config["game"]["actions"]
        self.prompt = config["game"]["prompt"]
        self.player = Player(self, config["player"])
        self.locations = Locations(self, config["locations"])                                

    def help(self):
        self._registry.help()    

    def _is_quitting(self):
        return self._quit

    def _update_completed(self):
        if(self.player.has_inventory_item(self._completed_inventory_item)):
            self._set_completed()                
    def _set_completed(self):
        self._completed = True                 
    def _is_completed(self):
        return self._completed

    def _handler_completed(self):
        if(self._is_completed()):
            utils.print_messages(self._completed_messages)            
    def _handler_quitting(self):
        if(self._is_quitting()):
            utils.print_messages(self._quitting_messages)
    def _handle_state(self):
        self._update_completed()
        self._handler_completed()
        self._handler_quitting()        

    def _next(self):
        self._input_handler.handle_input()
        #self._player.add_inventory_items([self._completed_inventory_item]) ## - test completed
        self._handle_state()                        
        self._set_completed() # temp

    def quit(self):
        self._quit = True

    def run(self):
        while(not (self._is_completed() or self._is_quitting())):
            self._next()
        

Game(config).run()