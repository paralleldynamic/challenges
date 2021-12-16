''.join(('000'+bin(int(x,16))[2:])[-4:] for x in h)

for char in input_hex:
    c = int(char, 16)
    c = bin(c)


def convert_binary(b):
    return int(b, 2)


class InputReader():
    def __init__(self, input_file_path="input.txt"):
        self.ingest_data(input_file_path)
    def ingest_data(self, input_file_path):
        with open(input_file_path, "r") as input:
            hex_message = input.readeline().strip()
        self.transmission = "".join([bin(int(char, 16))[2:].zfill(4)[:4] for char in hex_message])

class Packet():
    def __init__(self, binary, packet_begin, packet_end, version, type_id, subpackets, subpackets_begin, subpackets_end):
        self.binary = binary
        self.begin_index = packet_begin
        self.end_index = packet_end
        self.version = version
        self.type_id = type_id
        self.subpackets = subpackets
        self.subpackets_begin = subpackets_begin
        self.subpackets_end = subpackets_end

class OperatorPacket(Packet):
    def __init__(self, binary, packet_begin, packet_end, version, type_id, subpackets, subpackets_begin, subpackets_end):
        super().__init__(binary, packet_begin, packet_end, version, type_id, subpackets, subpackets_begin, subpackets_end)

class ValuePacket(Packet):
    def __init__(self, binary, packet_begin, packet_end, version, type_id, subpackets, subpackets_begin, subpackets_end):
        super().__init__(binary, packet_begin, packet_end, version, type_id, subpackets, subpackets_begin, subpackets_end)

class Transmission():
    def __init__(self, transmission):
        self.transmission = transmission
        self.packets = []

    def reader(self, packet_begin):
        if convert_binary(self.transmission[packet_begin:]) == 0:
            return False, None, None

        version_end = packet_begin + 3
        type_id_end = version_end + 3
        version = convert_binary(self.transmission[packet_begin:version_end])
        type_id = convert_binary(self.transmission[version_end:type_id_end])

        if type_id != 4:
            p = OperatorPacket
            length_type_end = type_id_end + 1
            length_type = int(self.transmission[type_id_end])
            if length_type == 0:
                subpacket_length_end = length_type_end + 15
                subpacket_length = convert_binary(self.transmission[length_type_end:subpacket_length_end])
                packet_end = subpacket_length_end + subpacket_length
                subpackets = self.transmission[subpacket_length_end:packet_end]
            if length_type == 1:
                number_of_packets_end = length_type_end + 11
                number_of_packets = convert_binary(self.transmission[length_type_end:number_of_packets_end])
                subpacket_length = 11 * number_of_packets
                packet_end = number_of_packets_end + subpacket_length
                subpackets = self.transmission[number_of_packets_end:packet_end]
        elif type_id == 4:
            p = ValuePacket
            subpackets_start = type_id_end
            current = subpackets_start
            subpackets_end = type_id_end + 5
            while self.transmission[current:subpackets_end][0] != "0":
                current = subpackets_end
                subpackets_end += 5
            packet_end = subpackets_end
            subpackets = self.transmission[subpackets_start:subpackets_end]
        packet = p(
            binary=self.transmission[packet_begin:packet_end],
            packet_begin=packet_begin,
            packet_end=packet_end,
            version=version,
            type_id=type_id,
            subpackets=subpackets,
            subpackets_start=subpackets_start,
            subpackets_end=subpackets_end
        )
        return True, packet_end, packet


