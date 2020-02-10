import sys
from raknet.server.UDPServerSocket import UDPServerSocket


class RakNetServer(object):
    def __init__(self, port, logger):
        if port < 1 or port > 65536:
            print("Invalid port given")
            sys.exit(1)

        self.port = port
        self.logger = logger

        self.server = UDPServerSocket(port, logger)
        # self.session_manager =
