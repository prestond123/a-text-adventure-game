import utils
import colour
class Unlockable:
    def __init__(self):
        pass
    
    def unlock(self, tool):
        if(utils.has_attribute(self._config, "locked")):
            if(self._config["unlock"] == tool.name):
                utils.remove_attribute(self._config, "locked")
                self.open()
            else:
                utils.print_message("You cannot unlock '{}' with a '{}'.".format(                    
                    colour.green(self.name),
                    colour.green(tool.name), 
                ))    
        else:
            utils.print_message("You cannot unlock this item.")