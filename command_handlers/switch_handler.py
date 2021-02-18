import utils
import colour
from command_handlers.command_handler import *

class SwitchHandler(CommandHandler):
    def __init__(self):
        pass
    
    def switch(self, game, item_name):
        location = game.get_location()
        if(item_name):             
            if(location.has_inventory_item(item_name)):
                item = location.get_inventory_item(item_name)                                
                item.switch()
            else:
                utils.print_message("I cant see a '{}' - Try switch <switch>".format(
                    colour.red(item_name)
                ))
        else:            
            items = location.find_item_by_attribute("switchable")
            item_names = sorted(items)
            if(len(item_names) > 1):
                utils.print_message("I dont understand which switch - Try: switch <switch>")
                return
            if(len(item_names) < 1):
                utils.print_message("There doesn't appear to be a switch in the room.")
                return            
            item = location.get_inventory_item(item_names[0])  
            item.switch()
    