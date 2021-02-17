import utils
import colour
from command_handler import *

class NavigationHandler(CommandHandler):
    def __init__(self):
        pass

    def go(self, game, location_name):
        location = game.get_location()
        if(location_name):  
            location_item = location.get_inventory_item(location_name)
            if(location.has_inventory_item(location_name)):
                utils.print_message("I dont know how to get to '{}' - Try: go <place>".format(
                    colour.red(location_name)
                ))
                return
            if(not game.locations.is_valid_location_name(location_name)):
                if("attributes" in location_item._config and "room" in location_item._config["attributes"]):
                    utils.print_message("Config Error: room '{}' not in config.".format(
                        colour.red(location_name)
                    ))
                utils.print_message("I dont know how to get to '{}' - Try: go <place>".format(
                    colour.red(location_name)
                ))
                return
            game.player.set_location_name(location_name)   
            new_location = game.get_location()
            new_location.add_inventory_item(location.name, location_item)
            game.auto_examine()
        else:
            utils.print_message("I dont understand - Try: go <place>")
