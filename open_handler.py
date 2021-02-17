import utils
import colour
from command_handler import *

class OpenHandler(CommandHandler):
    def __init__(self):
        pass

    def _get_context(self, item_name, contexts):
        for context in contexts:
            if(context.has_inventory_item(item_name)):
                return context
        return None

    def pick(self, game, action):
        self.unlock(game, action, "pick")

    def unlock(self, game, action, method="key"):
        # location = game.get_location()
        if(action):           
            items = action.split(" with ")
            if(type(items)==list and len(items) == 2):                
                location = game.get_location()  
                context = self._get_context(items[0], [location, game.player])                
                if(not context):                    
                    utils.print_message("I cannot see a '{}'".format(
                        colour.red(items[0])
                    ))
                    return
                target = context.get_inventory_item(items[0])                    
                if(not game.player.has_inventory_item(items[1])):
                    utils.print_message("You dont have a {}".format(
                        colour.red(items[1])
                    ))                
                    return
                tool = game.player.get_inventory_item(items[1])                                    
                target.unlock(location, tool, method)                
            else:
                utils.print_message("I dont understand: '{}' - Try unlock <item> with <item>.".format(
                    colour.red(action),                    
                ))
        else:
            utils.print_message("I dont understand - Try: unlock <item> with <item>")

    def open(self, game, item_name):        
        location = game.get_location()
        if(item_name):   
            context = self._get_context(item_name, [location, game.player])
            if(context):
                item = context.get_inventory_item(item_name)                                
                item.open(context)                
            else:
                utils.print_message("I cant see a '{}' - Try open <item>".format(
                    colour.red(item_name)
                ))
        else:
            utils.print_message("I dont understand - Try: open <item> ")
