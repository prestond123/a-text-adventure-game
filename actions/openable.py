import utils
import colour
class Openable:
    def __init__(self):
        pass
    
    def open(self, context):               
        if(utils.has_attribute(self._config, "openable")):            
            if(utils.has_attribute(self._config, "locked")):
                utils.print_message("Item '{}' is locked.".format(                                
                    colour.red(self.name)
                ))
                return
            if("inside" in self._config):
                items = self._config.pop("inside", None)
                items = self._config["revealed"] = items
                item_name = sorted(items)[0] # only allow 1 item - inside stuff                
                self.add_inventory_items(items)                
                if(len(items) > 0):
                    #if(utils.has_attribute(self._config, "door")):                        
                        if("opened" in self._config):
                            utils.print_messages(self._config["opened"])
                        ## remove doors after open
                        if(utils.has_attribute(self._config, "door")):
                            context.remove_inventory_item(self.name)
                            
                        if(utils.has_attribute(self._config, "door")):  
                            utils.print_message("You see the '{}' through the '{}'".format(
                                colour.green(item_name), 
                                colour.green(self.name)
                            ))
                        else:
                            utils.print_message("You see the '{}' in the '{}'".format(
                                colour.green(item_name), 
                                colour.green(self.name)
                            ))                    
                if(self.has_inventory()):
                    context.add_inventory_items(self.get_inventory_items())
        else:                        
            if("taken" in self._config and "inside" in self._config["taken"]):
                utils.print_message("{}".format(
                    colour.red("You cannot open this item until it has been taken.")
                ))
                utils.print_message("Hint: {}".format(
                    colour.green("Taking items show more details - You may see more detail when examined, and be able to open it!")
                ))
            return
            utils.print_message("{}".format(
                colour.red("You cannot open this item.")
            ))
                        