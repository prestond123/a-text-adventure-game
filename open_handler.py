from command_handler import *

class OpenHandler(CommandHandler):
    def __init__(self):
        pass
    def open(self, game, item_name):        
        location = game.get_location()        
        if(item_name):            
            if(location.has_inventory_item(item_name)):
                item = location.get_inventory_item(item_name)                
                item.open()
                if(item.has_inventory()):
                    location.add_inventory_items(item.get_inventory())
            else:
                print("Open what {}?".format(item_name))
        else:
            print("Open what?")
