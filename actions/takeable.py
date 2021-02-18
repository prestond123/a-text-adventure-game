import utils
import colour
class Takeable:
    def __init__(self):
        pass
    
    def take(self, location, player):
        if("attributes" in self._config and "takeable" in self._config["attributes"]):       
            config = self.get_config()            
            player.add_inventory_item(self.name, config)
            location.remove_inventory_item(self.name)
            if("taken" in config):
                taken = config.pop("taken")
                for key in taken:
                    config[key] = taken[key]
            utils.print_message("You take the '{}'".format(
                colour.green(self.name)
            ))
        else:
            utils.print_message("You cannot take '{}'.".format(
                colour.red(self.name)
            ))