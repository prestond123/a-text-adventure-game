import utils
import colour
class Describable:
    def __init__(self):
        pass
    def describe(self):        
        if("description" in self._config):
            desc = self._config["description"]
            for line in desc:
                utils.print_message(colour.blue(line))
        else:
            utils.print_message("You see nothing special.")