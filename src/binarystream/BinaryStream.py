from struct import *


class BinaryStream(object):
    buffer = None

    def __init__(self, buffer_val=None):
        self.buffer = bytes(0)
        self.offset = 0

        if buffer_val is not None:
            self.buffer += buffer_val
            self.offset = 0

    def get_buffer(self):
        return self.buffer

    def append(self, buf):
        if isinstance(buf, memoryview):
            self.buffer += bytes(buf)
            self.offset = len(buf)  # bytearray() ?
        elif isinstance(buf, str):
            self.buffer += bytes(bytes(buf).hex())
            self.offset += len(buf)
        elif isinstance(buf, list):
            self.buffer += bytes(buf)
            self.offset = len(buf)

    def read_byte(self):
        return self.get_buffer()[self.increaseOffset(1)]

    def write_byte(self, v):
        self.append(bytes.fromhex(v & 0xff))  # todo: test

    def write_l_triad(self, v):
        buf = bytes(3)
        buf += pack("V", v)[0:3]
        self.append(buf)

    def increaseOffset(self, v, ret=False):
        if ret:
            self.offset += v
        else:
            self.offset += v - v
        return self.offset
