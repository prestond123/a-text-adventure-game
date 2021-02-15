from registry import *
from examine_handler import *
from open_handler import *
from take_handler import *

class RegistryBuilder():    
    def __init__(self, registry):
        self._registry = registry        
    
    def quit(self, game):
        print("quiting")
        game.quit()

    def help(self, game):        
        game.help()

    def debug(self, game):
        print(game.debug())
        
    def register_commands(self):
        self._registry.register("debug", RegistryWrapper(self.debug, False))
        self._registry.register("help", RegistryWrapper(self.help, False), "?")
        self._registry.register("quit", RegistryWrapper(self.quit, False))        
        self._registry.register("examine", RegistryWrapper(ExamineHandler().examine, True))
        self._registry.register("open", RegistryWrapper(OpenHandler().open, True))
        self._registry.register("take", RegistryWrapper(TakeHandler().take, True))
        
    