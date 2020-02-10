from raknet.protocol.Packet import Packet


class Datagram(Packet):
    def __init__(self, stream):
        super().__init__(stream)
        self.sequence_number = 0
        self.needBAndAs = False
        self.header_flags = 0
        self.packet_pair = False
        self.continuos_send = False
        self.packets = []

    def encodeHeader(self):
        if self.packet_pair:
            self.header_flags |= 0x10
        elif self.continuos_send:
            self.header_flags |= 0x08
        elif self.needBAndAs:
            self.header_flags |= 0x04

    def encodePayload(self):
        self.get_stream().write_l_triad(self.sequence_number)
        for packet in self.packets:
            self.get_stream().append(packet)

    def get_length(self):
        length = 4
        for packet in self.packets:
            if isinstance(packet, EncapsulatedPacket):
                length += packet.get_lenght()
            else:
                length += len(bytes(packet).hex())

