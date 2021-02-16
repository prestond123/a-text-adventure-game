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
                    utils.print_message("You see a {} inside the {}".format(sorted(items), self.name))
        else:
            utils.print_message("You cannot open this item.")