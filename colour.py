
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def red(text):    
    return "{}{}{}".format(bcolors.RED, text, bcolors.ENDC)

def green(text):
    return "{}{}{}".format(bcolors.GREEN, text, bcolors.ENDC)

def yellow(text):
    return "{}{}{}".format(bcolors.YELLOW, text, bcolors.ENDC)

def blue(text):
    return "{}{}{}".format(bcolors.BLUE, text, bcolors.ENDC)

def cyan(text):
    return "{}{}{}".format(bcolors.CYAN, text, bcolors.ENDC)
