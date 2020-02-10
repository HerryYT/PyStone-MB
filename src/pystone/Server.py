from raknet import Interface
from pystone.utils import Logger


def start():
    Logger.log("Server is starting...")
    socket = Interface.connection()
