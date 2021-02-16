import utils
import colour

class Damageable:
    def __init__(self):
        pass
    
    def damage(self):
        config = self.get_config() 
        if(utils.has_attribute(config, "damageable")):
            utils.add_attribute(config, "damaged")            
            if("damaged" in config):
                damaged = config.pop("damaged")
                for key in damaged:
                    config[key] = damaged[key]