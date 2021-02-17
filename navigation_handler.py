import utils
import colour
from command_handler import *

class NavigationHandler(CommandHandler):
    def __init__(self):
        pass

    def _go(self, game, location_name, location):
        if(not location.has_inventory_item(location_name)):
            utils.print_message("I dont know how to get to '{}' - Try: go <place>".format(
                colour.red(location_name)
            ))
            return
        location_item = location.get_inventory_item(location_name)
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

    def go(self, game, location_name):
        location = game.get_location()
        if(location_name):                          
            self._go(game, location_name, location)
        else:
            locations = location.find_item_by_attribute("room")
            location_names = sorted(locations)
            if(len(location_names) > 1):
                utils.print_message("I dont understand where to go - Try: go <place>")
                return
            if(len(location_names) < 1):
                utils.print_message("There doesn't appear to be anywhere I can go to at the moment.")
                return     

            self._go(game, location_names[0], location)
            
