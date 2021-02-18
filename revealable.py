import utils

class Revealable:
    def __init__(self):
        pass

    def reveal(self):        
        if("reveal" in self._config):
            items = self._config.pop("reveal", None)
            visiable = utils.get_inventory_display(items)
            utils.print_message("Just seen: [{}]".format(visiable))
            items = self._config["revealed"] = items
            self.add_inventory_items(items)            
