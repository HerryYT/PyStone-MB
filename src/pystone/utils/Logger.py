from time import gmtime, strftime

HEADER = '\033[95m'
WHITE = '\033[0m'
BLUE = '\033[94m'
DARK_BLUE = '\033[1;34;1m'
GREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def log(msg):
    timestamp(WHITE + "Log > " + msg + END)


def debug(msg):
    timestamp(GREEN + "Debug > " + msg + END)


def timestamp(msg):
    print(DARK_BLUE + "[" + strftime("%H:%M:%S", gmtime()) + "] " + END + msg)
