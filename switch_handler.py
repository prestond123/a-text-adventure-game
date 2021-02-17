import utils
import colour
from command_handler import *

class SwitchHandler(CommandHandler):
    def __init__(self):
        pass
    
    def flick(self, game, item_name):
        location = game.get_location()
        if(item_name):             
            if(location.has_inventory_item(item_name)):
                item = location.get_inventory_item(item_name)                                
                item.flick()
            else:
                utils.print_message("I cant see a '{}' - Try flick <switch>".format(
                    colour.red(item_name)
                ))
        else:            
            utils.print_message("I dont understand - Try: flick <switch>")
    