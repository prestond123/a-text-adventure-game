import utils
import colour

class Damageable:
    def __init__(self):
        pass
    
    def damage(self, tool):
        if(tool.has_attribute["damageable"]):
            tool.add_attribute("damaged")
            config = self.get_config()      
            if("damaged" in config):
                damaged = config.pop("damaged")
                for key in damaged:
                    config[key] = damaged[key]