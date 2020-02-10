import socket
from src.pystone.utils import Logger
from src.binarystream.BinaryStream import BinaryStream


def connection(ip="0.0.0.0", port=19132):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip, port))
    Logger.log("Bounded on " + ip + ":" + str(port))

    while True:
        data = s.recvfrom(1024)
        stream = BinaryStream(data[0])
        packet_id = stream.get_buffer()[0]

        handle(packet_id, stream, data[1][0], data[1][1])

        Logger.log("Received " + str(hex(packet_id)) +
                   " with length of " + str(len(data[0])) +
                   " from " + str(data[1][0]) + ":" + str(data[1][1])
                   )


def handle(packet_id, stream, address, port):
    """todo: packet handling"""
