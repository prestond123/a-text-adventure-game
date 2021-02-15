class Takeable:
    def __init__(self):
        pass
    def take(self, player):
        if("attributes" in self._config and "takeable" in self._config["attributes"]):       
            config = self.get_config()
            print(config)
            player.add_inventory_item(self.name, config)
            print("You take the", self.name)
        else:
            print("You cannot take this item.")