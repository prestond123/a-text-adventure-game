import utils
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
                utils.print_message("Take what {}?".format(item_name))
        else:
            utils.print_message("Take what?")
