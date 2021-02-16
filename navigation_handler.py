import utils
import colour
from command_handler import *

class NavigationHandler(CommandHandler):
    def __init__(self):
        pass

    def go(self, game, location_name):
        location = game.get_location()
        if(location_name): 
            if(game.locations.is_valid_location_name(location_name) and
                location.has_inventory_item(location_name)):
                game.player.set_location_name(location_name)            
            else:             
                utils.print_message("Go where '{}'?".format(
                    colour.red(location_name)
                ))
        else:
            utils.print_message("Go where?")
