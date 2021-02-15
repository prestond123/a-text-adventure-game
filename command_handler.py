class Action():
    def __init__(self, action):
        self.action = action        
    def set_args(self, args):
        self.args = args

class ActionParser():
    def __init__(self):
        pass    
    def parse(self, user_input):
        words = user_input.split()
        if(type(words) == str):
            word = words.strip()
            if(not word):
                return None
            return Action(word)
        if(len(words) == 0):
            return None
        action = Action(words[0])
        if(len(words) > 0):
            action.set_args(words[1:])
        return action

class CommandHandler():
    def __init__(self, game, registry):
        self._game = game
        self._set_environment_update_required()
        self._action_parser = ActionParser()
        self._command_registry = registry
            
    def _set_environment_update_required(self):
        self.environment_update_required = True
    def _is_environment_update_required(self):
        return self.environment_update_required
    
    def _set_available_actions(self):                
        self._actions = self._game.get_actions() + self._game.player.get_location().get_actions()

    def _handle_environment(self):
        if(self._is_environment_update_required()):            
            self._set_available_actions()

    def _handle_command_invoke(self, action):
        if(self._command_registry.has_command(action.action)):            
            cmd = self._command_registry.get_command(action.action)
            if(cmd.pass_args):
                cmd.command(self._game, action.args)
            else:
                cmd.command(self._game)
        else:
            print("Unknown action: ", action.action)

    def _handle_user_action(self):     
        user_input = input(self._game.prompt).lower()       
        action = self._action_parser.parse(user_input)        
        self._handle_command_invoke(action)
        
    def run(self):        
        self._handle_environment()
        self._handle_user_action()
        