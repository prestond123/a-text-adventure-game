class Openable:
    def __init__(self):
        pass
    def open(self):        
        if("attributes" in self._config and "openable" in self._config["attributes"]):
            if("inside" in self._config):
                items = self._config.pop("inside", None)
                self.add_inventory(items)                
                if(len(items) > 0):
                    print("You see something.")
        else:
            print("You cannot open this item.")