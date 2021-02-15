class InputWrapper():
    def __init__(self, action):
        self.action = action        
    def set_args(self, args):
        self.args = args

class InputParser():
    def __init__(self):
        pass    
    def parse(self, user_input):
        words = user_input.split()
        if(type(words) == str):
            word = words.strip()
            if(not word):
                return None
            return InputWrapper(word)
        if(len(words) == 0):
            return None
        action = InputWrapper(words[0])
        if(len(words) > 0):
            action.set_args(" ".join(words[1:]))            
        return action

class InputHandler():
    def __init__(self, game, registry):
        self._game = game        
        self._parser = InputParser()
        self._registry = registry
            
    def _invoke(self, action):
        if(self._registry.has_command(action.action)):            
            cmd = self._registry.get_command(action.action)
            if(cmd.pass_args):
                cmd.command(self._game, action.args)
            else:
                cmd.command(self._game)
        else:
            print("I dont know how to: ", action.action)

    def handle_input(self):     
        user_input = input(self._game.get_prompt()).lower()       
        action = self._parser.parse(user_input)      
        if(action) :
            self._invoke(action)
        
        