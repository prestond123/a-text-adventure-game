import utils
import colour

class Moveable:
    def __init__(self):
        pass
    
    def move(self, context):               
        if(utils.has_attribute(self._config, "moveable")):            
            if("inside" in self._config):
                items = self._config.pop("inside", None)
                self._config["revealed"] = items
                item_name = sorted(items)[0] # only allow 1 item - inside stuff                
                self.add_inventory_items(items)                
                if(len(items) > 0):                                            
                    if("moved" in self._config):
                        utils.print_messages(self._config["moved"])                        
                    utils.print_message("You see a '{}' after moving the '{}'".format(
                        colour.green(item_name), 
                        colour.green(self.name)
                    ))                    
                if(self.has_inventory()):
                    context.add_inventory_items(self.get_inventory_items())
            else:
                utils.print_message("You moved the '{}'".format(                    
                    colour.green(self.name)
                ))      
        else:                                    
            utils.print_message("{}".format(
                colour.red("You cannot move this item.")
            ))
                        