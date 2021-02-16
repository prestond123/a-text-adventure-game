import utils
import colour
from command_handler import *

class OpenHandler(CommandHandler):
    def __init__(self):
        pass

    def _get_actor(self, item_name, actors):
        for actor in actors:
            if(actor.has_inventory_item(item_name)):
                return actor        
        return None

    def unlock(self, game, action):
        # location = game.get_location()
        if(action):           
            items = action.split(" with ")
            if(type(items)==list and len(items) == 2):
                
                location = game.get_location()  

                if(not location.has_inventory_item(items[0])):                    
                    utils.print_message("Dont what target '{}' is".format(
                        colour.red(items[0])
                    ))
                    return

                target = location.get_inventory_item(items[0])
                    
                if(not game.player.has_inventory_item(items[1])):
                    utils.print_message("Dont what tool {}".format(
                        colour.red(items[1])
                    ))                
                    return

                tool = game.player.get_inventory_item(items[1])                    
                
                target.unlock(tool)

                if(target.has_inventory()):
                    location.add_inventory_items(target.get_inventory_items())      
            else:
                utils.print_message("Dont understand {} - Unlock <what> with <what>?".format(
                    colour.red(action),                    
                ))
        else:
            utils.print_message("Unlock <what> with <what>?")

    def open(self, game, item_name):        
        location = game.get_location()
        if(item_name):   
            actor = self._get_actor(item_name, [location, game.player])
            if(actor):
                item = actor.get_inventory_item(item_name)                                
                item.open()
                if(item.has_inventory()):
                    actor.add_inventory_items(item.get_inventory_items())            
            else:
                utils.print_message("Open what '{}'?".format(
                    colour.red(item_name)
                ))
        else:
            utils.print_message("Open <what>?")
