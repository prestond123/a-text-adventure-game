
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def red(text):    
    return "{}{}{}".format(bcolors.FAIL, text, bcolors.ENDC)
def green(text):
    return "{}{}{}".format(bcolors.OKGREEN, text, bcolors.ENDC)
def yellow(text):
    return "{}{}{}".format(bcolors.WARNING, text, bcolors.ENDC)
def blue(text):
    return "{}{}{}".format(bcolors.OKBLUE, text, bcolors.ENDC)
