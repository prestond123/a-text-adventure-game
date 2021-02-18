import utils
import colour
class Switchable:
    def __init__(self):
        pass
    
    def switch(self):               
        if(utils.has_attribute(self._config, "switchable")):                        
            if("event" not in self._config):
                 utils.print_message("Config Error: switch '{}' has no event in config.".format(
                    colour.red(location_name)
                ))
            event = self._config["event"]
            if(self.game.locations.is_valid_location_name(event[0])):
                location = self.game.locations.get_location(event[0])
                location.handle_event(event)
            if("switched" in self._config):
                utils.print_messages(self._config["switched"])
            else:
                utils.print_message("Config Error: switch '{}' has bad event location in config.".format(
                    colour.red(location_name)
                ))                
        else:
            utils.print_message("You cannot switch this item.")