from binarystream.BinaryStream import BinaryStream


class Packet(object):
    def __init__(self, stream):
        if isinstance(stream, BinaryStream):
            self.stream = stream
        else:
            self.stream = BinaryStream()

    def get_id(self):
        return -1

    def encode(self):
        self.encodeHeader()
        self.encodePayload()

    def encodeHeader(self):
        self.get_stream().write_byte(self.get_id())

    def decodeHeader(self):
        self.get_stream().read_byte()

    def encodePayload(self):
        pass

    def decodePayload(self):
        pass

    def get_stream(self):
        return self.stream
