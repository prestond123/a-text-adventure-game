import utils
import colour
from command_handlers.command_handler import *

class OpenHandler(CommandHandler):
    def __init__(self):
        pass

    def _get_context(self, item_name, contexts):
        for context in contexts:
            if(context.has_inventory_item(item_name)):
                return context
        return None
     
    def safe(self, game, combination):
        location = game.get_location()

        config = location.find_item_by_attribute("safe")
        item_names = sorted(config)
        if(len(item_names) > 1):
            utils.print_message("Config error: more than one safe in location")
            return
        if(len(item_names) < 1):
            utils.print_message("There doesn't appear to be a safe in the room.")
            return                    
        if(not combination):        
            utils.print_message("You cant open a safe without combination - Try: safe <nnnnnn>")
            return                    
        if(not config[item_names[0]]["combination"] == combination):
            utils.print_message("You entered the wrong combination")
            return
        utils.add_attribute(config[item_names[0]], "openable")
        safe = location.get_inventory_item(item_names[0])
        safe.open(location)
        
    def pick(self, game, action):
        self.unlock(game, action, "pick")

    def unlock(self, game, action, method="key"):
        # location = game.get_location()
        if(action):           
            items = action.split(" with ")
            if(not (type(items)==list and len(items) == 2)):
                items = action.split(" w ") # alias
            if(type(items)==list and len(items) == 2):                
                location = game.get_location()  
                context = self._get_context(items[0], [location, game.player])                
                if(not context):                    
                    utils.print_message("I cannot see a '{}'".format(
                        colour.red(items[0])
                    ))
                    return
                ##TODO we could index target and use alias
                target = context.get_inventory_item(items[0])                    
                if(not game.player.has_inventory_item(items[1])):
                    utils.print_message("You dont have a {}".format(
                        colour.red(items[1])
                    ))                
                    return
                ##TODO we could index tools and use alias
                tool = game.player.get_inventory_item(items[1])                                    
                target.unlock(location, tool, method)                
            else:
                method_display = method
                if(method=="key"):
                    method_display="unlock"
                utils.print_message("I dont understand: '{}' - Try {} <item> with <item>.".format(
                    colour.red(action),                    
                    colour.red(method_display),
                ))
        else:
            utils.print_message("I dont understand - Try: unlock <item> with <item>")

    def move(self, game, item_name):
        location = game.get_location()
        if(item_name):   
            context = self._get_context(item_name, [location, game.player])
            if(context):
                item = context.get_inventory_item(item_name)                                
                item.move(context)                
            else:
                utils.print_message("I cant see a '{}' - Try open <item>".format(
                    colour.red(item_name)
                ))
        else:            
            utils.print_message("I dont know what to move - Try open <item>")            

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
            items = location.find_item_by_attribute("openable")
            item_names = sorted(items)
            if(len(item_names) > 1):
                utils.print_message("I dont understand what to open - Try: open <item>")
                return
            if(len(item_names) < 1):
                utils.print_message("There doesn't appear to be anything to open in the room.")
                return            
            items[item_name].open(location)
            
