import time


class Session(object):
    def __init__(self, session_manager, address, port, client_id, mtu_size):
        self.session_manager = session_manager
        self.address = address
        self.port = port
        self.client_id = client_id
        self.mtu_size = mtu_size

        self.set_send_queue()

        self.last_update = lambda: int(round(time.time() * 1000))

    def set_send_queue(self):
        self.send_queue = Datagram