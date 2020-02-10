from raknet.protocol.Packet import Packet

class EncapsulatedPacket(Packet):
    def __init__(self, stream):
        super().__init__(stream)
        #todo
