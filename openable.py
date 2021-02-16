import utils
class Openable:
    def __init__(self):
        pass
    def open(self):        
        if("attributes" in self._config and "openable" in self._config["attributes"]):
            if("inside" in self._config):
                items = self._config.pop("inside", None)
                self.add_inventory_items(items)                
                if(len(items) > 0):
                    if("attributes" in self._config and "door" in self._config["attributes"]):
                        location = self.game.get_location()
                        location.remove_inventory_item(self.name)
                        utils.print_message("You see the {} through {}".format(sorted(items), self.name))    
                    else:
                        utils.print_message("You see a {} inside the {}".format(sorted(items), self.name))                        
        else:
            utils.print_message("You cannot open this item.")