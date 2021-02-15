class Command():
    def __init__(self, command, pass_args=True):        
        self.command = command
        self.pass_args = pass_args

class CommandRegistry():
    def __init__(self):
        self._registry = {}
    
    def register(self, name, command, alias=None):
        self._registry[name] = command
        if(not alias):
            alias = name[0]
        if(alias not in self._registry):
            self._registry[alias] = command

    def alias(self, name, alias):
        self._registry[alias] = self._registry[name]
    
    def has_command(self, name):
        return name in self._registry

    def get_command(self, name):
        return self._registry[name]
        
    def help(self):
        print("Available commands are:")
        for cmd in sorted(self._registry):
            print(cmd)

    def dump(self):
        print(self._registry)
