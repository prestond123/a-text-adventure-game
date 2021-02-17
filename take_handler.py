import utils
import colour
from command_handler import *

class TakeHandler(CommandHandler):
    def __init__(self):
        pass
    def take(self, game, item_name):        
        location = game.get_location()        
        if(item_name):            
            if(location.has_inventory_item(item_name)):
                item = location.get_inventory_item(item_name)   
                item.take(location, game.player)                             
            else:
                utils.print_message("I cant see a '{}' - Try: take <item>".format(
                    colour.red(item_name)
                ))
        else:
            utils.print_message("I dont understand - Try: take item")
