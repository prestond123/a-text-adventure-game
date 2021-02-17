import utils
import colour
from config import *
from player import *
from locations import *
from registry import *
from registry_builder import *
from input_handler import *
import json

class Game():
    def __init__(self, config):
        self._root_config = config
        self._config = config["game"]        
        self.max_carry = config["game"]["max-carry"]
        self._completed = False
        self._quit = False
        self._auto_examine = True
        self._registry = Registry()                
        self._input_handler = InputHandler(self, self._registry)                
        self.player = Player(self, config["player"])
        self.locations = Locations(self, config["locations"])
        RegistryBuilder(self._registry).register_commands()
                          
    def _handle_completed(self):        
        if(self.player.has_inventory_item(self._config["completed-inventory-item"])):
            self.completed = True        
            utils.print_messages(self._config["completed-messages"])
            
    def _handle_quitting(self):
        if(self._quit):
            utils.print_messages(self._config["quitting-messages"])
      
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
    
    def auto_examine(self):
        if(self._auto_examine):
            cmd = self._registry.get_command("examine")            
            cmd.command(self, None)

    def set_carrying_count(self, items):
        #print("game", self._root_config)
        count = 0
        item_names = sorted(items)
        for item_name in items:                   
            item = items[item_name]            
            config = item.get_config()
            count += 1
            for container in ["revealed"]:
                if(container in config):                    
                    inside = sorted(config[container])                    
                    for i in inside:                        
                        if(i in item_names):                            
                            count -= 1                
        self.carrying_count = count
        return count

    def get_inventory_display(self, items):
        visible = []        
        for item_name in items:
            item = items[item_name]            
            config = item.get_config()
            if(utils.has_attribute(config, "room")):
                visible.append("'{}'".format(colour.yellow(item_name)))
            elif(utils.has_attribute(config, "door") and utils.has_attribute(config, "locked")):                
                visible.append("'{}'".format(colour.red(item_name)))
            elif(utils.has_attribute(config, "openable")):
                visible.append("'{}'".format(colour.cyan(item_name)))
            else:
                visible.append("'{}'".format(colour.green(item_name)))
                #visible.append("'{}'".format(item_name))
        return ", ".join(visible)        

    def run(self):
        self.auto_examine()
        while(not (self._completed or self._quit)):
            carrying = self.player.get_inventory_items()
            carrying_display = self.get_inventory_display(carrying)
            visible = self.get_inventory_display(self.get_location().get_inventory_items())
            print("+ visible:[{}]".format(visible))
            print("+ carrying: [{}]({}/{})".format(
                carrying_display, 
                self.set_carrying_count(carrying),
                self.max_carry)
            )
            self._input_handler.handle_input()
            #self._player.add_inventory_items([self._config["completed-inventory-item"]]) ## - test completed
            self._handle_completed()
            self._handle_quitting()                    
            #self._set_completed() # temp
    
    def debug(self, what):
        if(what == "auto examine on"):
            self._auto_examine = True
        if(what == "auto examine off"):
            self._auto_examine = False
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
