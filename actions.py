import utils

class Actions():
    def __init__(self, actions):
        self._actions = actions
    def from_config(config):        
        return utils.get_list("actions", config)
    def get_actions(self):
        return self._actions            
    def has_action(self, action):
        return action in self._actions