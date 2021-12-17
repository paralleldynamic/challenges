from functools import reduce
from operator import add, mul

from timeit import default_timer as timer

def convert_binary(b):
    return int(b, 2)

class InputReader:
    def __init__(self, input_file_path=None):
        if input_file_path:
            self.input_file_path = input_file_path
            self.ingest_data(input_file_path)

    def ingest_data(self, input_file_path):
        with open(input_file_path, "r") as input:
            hex_message = input.readline().strip()
        self.transmission = "".join(
            [bin(int(char, 16))[2:].zfill(4)[:4] for char in hex_message]
        )

    def ingest_text(self, hex_message):
        self.transmission = "".join(
            [bin(int(char, 16))[2:].zfill(4)[:4] for char in hex_message]
        )

    def __repr__(self):
        return f"InputReader<({self.input_file_path})>"


class Packet:
    def __init__(
        self,
        binary,
        packet_begin,
        packet_end,
        version,
        type_id,
        subpackets,
    ):
        self.binary = binary
        self.begin_index = packet_begin
        self.end_index = packet_end
        self.version = version
        self.type_id = type_id
        self.subpackets = subpackets


class OperatorPacket(Packet):
    OPS = {
        0: lambda x: reduce(add, x, 0),
        1: lambda x: reduce(mul, x, 1),
        2: lambda x: min(x),
        3: lambda x: max(x),
        5: lambda x: 1 if x[0] > x[1] else 0,
        6: lambda x: 1 if x[0] < x[1] else 0,
        7: lambda x: 1 if x[0] == x[1] else 0
    }

    def __init__(
        self,
        binary,
        packet_begin,
        packet_end,
        version,
        type_id,
        subpackets,
    ):
        super().__init__(
            binary,
            packet_begin,
            packet_end,
            version,
            type_id,
            subpackets,
        )
        self.op = OperatorPacket.OPS[type_id]

    def version_sum(self):
        versions = sum(map(lambda x: x.version_sum(), self.subpackets))
        return versions + self.version

    def evaluate(self):
        vals = list(map(lambda x: x.evaluate(), self.subpackets))
        return self.op(vals)

    def __repr__(self):
        return f"OperatorPacket<(Version: {self.version}. Subpackets: {len(self.subpackets)})>"


class ValuePacket(Packet):
    def __init__(
        self,
        binary,
        packet_begin,
        packet_end,
        version,
        type_id,
        subpackets,
    ):
        super().__init__(
            binary,
            packet_begin,
            packet_end,
            version,
            type_id,
            subpackets,
        )
        v = binary[6:]
        value_binary = ""
        for n in range(0, len(v), 5):
            value_binary += v[n:n+5][-4:]
        self.value = convert_binary(value_binary)

    def version_sum(self):
        return self.version

    def evaluate(self):
        return self.value

    def __repr__(self):
        return f"ValuePacket<(Version: {self.version}. Value: {self.value})>"

class Transmission:
    def __init__(self, transmission):
        self.binary = transmission
        self.packets = []
        reading = True
        while reading:
            reading, packet, transmission = self.packet_reader(transmission)
            if packet:
                self.packets.append(packet)

    def packet_reader(self, packet, packet_begin=0):
        if not packet:
            return False, None, None

        if convert_binary(packet[packet_begin:]) == 0:
            return False, None, None

        version_end = packet_begin + 3
        type_id_end = version_end + 3
        version = convert_binary(packet[packet_begin:version_end])
        type_id = convert_binary(packet[version_end:type_id_end])
        subpackets = []

        if type_id != 4:
            p = OperatorPacket
            length_type_end = type_id_end + 1
            length_type = int(packet[type_id_end])

            if length_type == 0:
                subpacket_length_end = length_type_end + 15
                subpacket_length = convert_binary(
                    packet[length_type_end:subpacket_length_end]
                )
                subpackets_begin = subpacket_length_end
                subpackets_end = subpackets_begin + subpacket_length
                subpacket_binary = packet[subpackets_begin:subpackets_end]

                reading = True
                while reading:
                    reading, subpacket, subpacket_binary = self.packet_reader(subpacket_binary)
                    if subpacket:
                        subpackets.append(subpacket)

                packet_end = subpackets_end
                remainder = packet[packet_end:]

            if length_type == 1:
                number_of_packets_end = length_type_end + 11
                number_of_packets = convert_binary(
                    packet[length_type_end:number_of_packets_end]
                )
                subpackets_begin = number_of_packets_end
                remainder = packet[subpackets_begin:]

                for i in range(number_of_packets):
                    _, subpacket, remainder = self.packet_reader(remainder)
                    if subpacket:
                        subpackets.append(subpacket)

                packet_end = subpackets_begin

        elif type_id == 4:
            p = ValuePacket
            subpackets_begin = type_id_end
            current = subpackets_begin
            subpackets_end = current + 5

            while packet[current:subpackets_end][0] != "0":
                current = subpackets_end
                subpackets_end += 5

            packet_end = subpackets_end
            subpackets = packet[subpackets_begin:subpackets_end]
            remainder = packet[packet_end:]

        if subpackets:
            pass

        _packet = p(
            binary=packet[packet_begin:packet_end],
            packet_begin=packet_begin,
            packet_end=packet_end,
            version=version,
            type_id=type_id,
            subpackets=subpackets,
        )
        return True, _packet, remainder

if __name__ == "__main__":
    start = timer()
    ir = InputReader()
    ir.ingest_data("input.txt")
    t = Transmission(ir.transmission)
    p = t.packets[0]
    version_sum = p.version_sum()
    solution = p.evaluate()
    print(f"Part 1: {version_sum}")
    print(F"Part 2: {solution}")
    end = timer()
    print(f"Runtime was {end - start} seconds")
