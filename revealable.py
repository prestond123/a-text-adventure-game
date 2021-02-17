class Revealable:
    def __init__(self):
        pass

    def reveal(self):        
        if("reveal" in self._config):
            items = self._config.pop("reveal", None)
            items = self._config["revealed"] = items
            self.add_inventory_items(items)            
