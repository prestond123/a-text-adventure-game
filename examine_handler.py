from action_handler import *

class ExamineHandler(CommandHandler):
    def __init__(self):
        pass
    def examine(self, game, args):
        print("examine:", args)
        self.test()