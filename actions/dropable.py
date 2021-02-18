import utils
import colour
class Dropable:
    def __init__(self):
        pass
    
    def drop(self, player, location):        
        config = self.get_config()        
        location.add_inventory_item(self.name, config)
        player.remove_inventory_item(self.name)
              
        utils.print_message("You drop the '{}'".format(
            colour.green(self.name)
        ))
        