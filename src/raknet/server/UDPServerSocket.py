import socket
import sys


class UDPServerSocket(object):
    def __init__(self, port, logger):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            self.socket.bind(("0.0.0.0", port))
        except socket.error as msg:
            logger.log("Error, " + msg)
            sys.exit(1)

    def get_socket(self):
        return self.socket

    def send_buffer(self, buffer, address, port):
        return self.socket.sendto(buffer, (address, port))
    
    def close(self):
        self.socket.close()
