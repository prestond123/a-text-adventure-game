import utils
from command_handler import *

class DropHandler(CommandHandler):
    def __init__(self):
        pass
    def drop(self, game, item_name):
        location = game.get_location()        
        if(item_name):            
            if(game.player.has_inventory_item(item_name)):
                item = game.player.get_inventory_item(item_name)   
                item.drop(game.player, location)
            else:
                utils.print_message("Drop what {}?".format(item_name))
        else:
            utils.print_message("Drop what?")
