import utils
import colour
from command_handler import *

class UnlockHandler(CommandHandler):
    def __init__(self):
        pass
    
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
            else:
                utils.print_message("Dont understand {} - Unlock <what> with <what>?".format(
                    colour.red(action),                    
                ))
        else:
            utils.print_message("Unlock <what> with <what>?")
