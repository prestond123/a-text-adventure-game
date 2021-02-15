from command_registry import *
import examine_handler

class Commands():    
    def __init__(self, registry):
        self._registry = registry
    
    def quit(self, game):
        print("quiting")
        game.quit()

    def help(self, game):        
        game.help()

    def register_commands(self):
        self._registry.register("help", Command(self.help, False), "?")
        self._registry.register("quit", Command(self.quit, False))        
        self._registry.register("examine", Command(examine_handler.examine, True))
    