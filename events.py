import utils
import colour
class Events:
    def __init__(self):
        pass
    
    def handle_event(self, event):                
        if("on" not in self._config):
            utils.print_message("Config Error: location '{}' has no event handlers in config.".format(
                colour.red(self.name)
            )) 

        on = self._config["on"]
        if(event[1] not in on):
            utils.print_message("Config Error: location '{}' has no event target {} in config.".format(
                colour.red(self.name),
                colour.red(event[1])
            )) 

        target = on[event[1]]

        if(event[2] not in target):
            utils.print_message("Config Error: location '{}' has no event action {} in config.".format(
                colour.red(self.name),
                colour.red(event[2])
            )) 

        details = target[event[2]]

        for key in details:
            self._config[key] = details[key]