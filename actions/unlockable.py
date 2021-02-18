import utils
import colour
class Unlockable:
    def __init__(self):
        pass
    
    def unlock(self, context, tool, method):
        if(utils.has_attribute(self._config, "locked")):                        
            if(self._config["unlock"] == tool.name):
                if(method=="pick"):
                    if(self._config["unlock-method"] == "key"):
                        utils.print_message("You cannot pick '{}' with a key '{}'.".format(                    
                            colour.red(self.name),
                            colour.red(tool.name), 
                        ))    
                        return
                    if(utils.has_attribute(tool.get_config(),"damaged")):
                        utils.print_message("You cannot pick '{}' with a '{}'.".format(                    
                            colour.red(self.name),
                            colour.red(tool.name), 
                        ))
                        return
                    tool.damage()
                else:
                    if(self._config["unlock-method"] == "pick"):
                        utils.print_message("You cannot unlock '{}' with a '{}'.".format(                    
                            colour.red(self.name),
                            colour.red(tool.name), 
                        ))    
                        return
                utils.remove_attribute(self._config, "locked")                    
                self.open(context)
            else:
                utils.print_message("You cannot {} '{}' with a '{}'.".format(                    
                    method,
                    colour.red(self.name),
                    colour.red(tool.name), 
                ))    
        else:
            utils.print_message("You cannot unlock this item.")