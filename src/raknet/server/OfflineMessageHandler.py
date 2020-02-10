class OfflineMessageHandler(object):
    def __init__(self, manager):
        self.session_manager = manager

    def handle(self, packet, address, port):
        #TODO
