
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

colours=True

def red(text):    
    if(colours):
        return "{}{}{}".format(bcolors.RED, text, bcolors.ENDC)
    return text

def green(text):
    if(colours):
        return "{}{}{}".format(bcolors.GREEN, text, bcolors.ENDC)
    return text

def yellow(text):
    if(colours):
        return "{}{}{}".format(bcolors.YELLOW, text, bcolors.ENDC)
    return text

def blue(text):
    if(colours):
        return "{}{}{}".format(bcolors.BLUE, text, bcolors.ENDC)
    return text

def cyan(text):
    if(colours):
        return "{}{}{}".format(bcolors.CYAN, text, bcolors.ENDC)
    return text
