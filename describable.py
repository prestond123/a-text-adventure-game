class Describable:
    def __init__(self):
        pass
    def describe(self):        
        if("description" in self._config):
            desc = self._config["description"]
            for line in desc:
                print(line)
        else:
            print("You see nothing special.")