import utils
import colour
from command_handlers.command_handler import *

class ExamineHandler(CommandHandler):
    def __init__(self):
        pass
    def examine(self, game, item_name):        
        location = game.get_location()        
        if(item_name):            
            if(location.has_inventory_item(item_name)):
                item = location.get_inventory_item(item_name)
                item.describe()
                item.reveal()
                if(item.has_inventory()):
                    location.add_inventory_items(item.get_inventory_items())
            elif(game.player.has_inventory_item(item_name)):
                item = game.player.get_inventory_item(item_name)
                item.describe()
                item.reveal()
                if(item.has_inventory()):
                    game.player.add_inventory_items(item.get_inventory_items())
            else:
                utils.print_message("Examine what '{}'?".format(
                    colour.red(item_name)
                ))
        else:
            location.describe()
            location.reveal()
        