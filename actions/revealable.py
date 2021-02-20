import utils

class Revealable:
    def __init__(self):
        pass

    def reveal(self):        
        if("reveal" in self._config):
            items = self._config.pop("reveal", None)
            visible = utils.get_inventory_display(items)
            # if(len(visible) > 0):
            #     utils.print_message("Just seen: [\n  {}\n]".format(visible))
            # else:
            #     utils.print_message("Just seen: [ ]".format(visible))
            items = self._config["revealed"] = items
            self.add_inventory_items(items)            
