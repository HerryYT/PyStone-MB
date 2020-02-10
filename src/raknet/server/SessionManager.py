import time
from raknet.server.OfflineMessageHandler import OfflineMessageHandler
from binarystream.BinaryStream import BinaryStream


class SessionManager(object):
    sessions = list

    def __init__(self, server, socket):
        self.server = server
        self.socket = socket

        self.start_time = lambda: int(round(time.time() * 1000))  # ms time
        self.offline_message_handler = OfflineMessageHandler(self)
        self.start()

    def start(self):
        while True:
            msg = self.socket.recvfrom(1024)

            if len(msg) < 1:
                return

            stream = BinaryStream(msg)
            packet_id = stream.get_buffer()[0]

            self.handle(packet_id, stream, msg[1][0], msg[1][1])

    def handle(self, packet_id, stream, ip, port):
        session = self.get_session(ip, port)

    def get_session(self, address, port):
        return self.sessions

    # def session_exists(self, address, port):
    #    if isinstance(address, Session)
