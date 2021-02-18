from registry import *
from command_handlers.examine_handler import *
from command_handlers.open_handler import *
from command_handlers.take_handler import *
from command_handlers.drop_handler import *
from command_handlers.navigation_handler import *
from command_handlers.switch_handler import *

class RegistryBuilder():    
    def __init__(self, registry):
        self._registry = registry        
    
    def quit(self, game):
        print("quiting....")
        game.quit()

    def help(self, game):        
        game.help()

    def debug(self, game, args):
        game.debug(args)
        
    def register_commands(self):
        open = OpenHandler()
        self._registry.register("-", RegistryWrapper(self.debug, True))
        self._registry.register("help", RegistryWrapper(self.help, False), "?")
        self._registry.register("quit", RegistryWrapper(self.quit, False))        
        self._registry.register("examine", RegistryWrapper(ExamineHandler().examine, True))
        self._registry.register("open", RegistryWrapper(open.open, True))
        self._registry.register("unlock", RegistryWrapper(open.unlock, True))
        self._registry.register("pick", RegistryWrapper(open.pick, True))
        self._registry.register("move", RegistryWrapper(open.move, True))  
        self._registry.register("safe", RegistryWrapper(open.safe, True), "safe")                
        self._registry.register("take", RegistryWrapper(TakeHandler().take, True))
        self._registry.register("drop", RegistryWrapper(DropHandler().drop, True))
        self._registry.register("go", RegistryWrapper(NavigationHandler().go, True))
        self._registry.register("switch", RegistryWrapper(SwitchHandler().switch, True))
        
    