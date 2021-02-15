from registry import *
from examine_handler import *

class RegistryBuilder():    
    def __init__(self, registry):
        self._registry = registry
        self.examine_handler = ExamineHandler()
    
    def quit(self, game):
        print("quiting")
        game.quit()

    def help(self, game):        
        game.help()

    def register_commands(self):
        self._registry.register("help", RegistryWrapper(self.help, False), "?")
        self._registry.register("quit", RegistryWrapper(self.quit, False))        
        self._registry.register("examine", RegistryWrapper(self.examine_handler.examine, True))
    