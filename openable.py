import utils
import colour
class Openable:
    def __init__(self):
        pass
    
    def open(self, context):               
        if(utils.has_attribute(self._config, "openable")):            
            if("inside" in self._config):
                items = self._config.pop("inside", None)
                items = self._config["revealed"] = items
                item_name = sorted(items)[0] # only allow 1 item - inside stuff                
                self.add_inventory_items(items)                
                if(len(items) > 0):
                    if(utils.has_attribute(self._config, "door")):                        
                        if(utils.has_attribute(self._config, "locked")):
                            utils.print_message("Door '{}' is locked.".format(                                
                                colour.red(self.name)
                            ))
                        else:
                            #location = self.game.get_location()
                            context.remove_inventory_item(self.name)
                            utils.print_message("You see the '{}' through the '{}'".format(
                                colour.green(item_name), 
                                colour.green(self.name)
                            ))
                    else:
                        utils.print_message("You see a '{}' inside the '{}'".format(
                            colour.green(item_name), 
                            colour.green(self.name)
                        ))
                if(self.has_inventory()):
                    context.add_inventory_items(self.get_inventory_items())
        else:
            utils.print_message("You cannot open this item.")