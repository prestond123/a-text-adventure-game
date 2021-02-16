from command_handler import *

class OpenHandler(CommandHandler):
    def __init__(self):
        pass

    def _get_actor(self, item_name, actors):
        for actor in actors:
            if(actor.has_inventory_item(item_name)):
                return actor        
        return None

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
                print("Open what {}?".format(item_name))
        else:
            print("Open what?")
