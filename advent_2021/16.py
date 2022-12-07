from math import prod

from utils import get_neighbors_n_dimensional, read_trimmed


class Packet:
    children: list = []
    content: str | None = None
    type_map = {
        0: sum,
        1: prod,
        2: min,
        3: max,
        5: lambda x: 1 if x[0] > x[1] else 0,
        6: lambda x: 1 if x[0] < x[1] else 0,
        7: lambda x: 1 if x[0] == x[1] else 0,
    }

    def __init__(self, version, typeID, content, is_sub_packet=False):
        self.version = version
        self.typeID = typeID
        self.content = content
        if typeID == 4:
            self.parse_literal(is_sub_packet)
        else:
            self.children = []
            self.value = None
            self.parse_operator()

    @classmethod
    def read_packet(cls, content, is_sub_packet=False):
        version = int(content[:3], 2)
        typeID = int(content[3:6], 2)
        return Packet(version, typeID, content[6:], is_sub_packet)

    def parse_literal(self, is_sub_packet=False):
        total = ""
        packet_length = 6
        while True:
            total += self.content[1:5]
            packet_length += 5
            if self.content[0] == "0":
                self.content = self.content[5:]
                break
            self.content = self.content[5:]
        bonus = 0 if is_sub_packet else 4 - (packet_length % 4)
        self.value = int(total, 2)
        self.content = self.content[bonus:]

    def parse_operator(self):
        length_type = self.content[0]
        total = 0
        if length_type == "0":
            length = int(self.content[1:16], 2)
            self.content = self.content[16:]
            original_length = len(self.content)
            while original_length - len(self.content) < length:
                child = Packet.read_packet(self.content, is_sub_packet=True)
                self.children.append(child)
                self.content = child.content
            # bonus = (16 + length + 7) % 4
            bonus = 0
            return self.content[16 + length + bonus :], total
        else:
            subpacket_count = int(self.content[1:12], 2)
            self.content = self.content[12:]
            for _ in range(subpacket_count):
                child = Packet.read_packet(self.content, is_sub_packet=True)
                self.children.append(child)
                self.content = child.content

    def __repr__(self) -> str:
        return "\n".join(
            [
                f"version: {self.version}",
                f"type: {self.typeID}",
                f"value: {self.value}",
                *[f"  {child.__repr__()}" for child in self.children],
            ]
        )

    def add_versions(self):
        if self.typeID == 4:
            return self.version
        else:
            return self.version + sum(child.add_versions() for child in self.children)

    def compute(self):
        if self.typeID == 4:
            return self.value
        child_values = [child.compute() for child in self.children]
        return Packet.type_map[self.typeID](child_values)


def q1(values):
    packet_str = "".join(values)
    packet = Packet.read_packet(packet_str)
    return packet.add_versions()


def q2(values):
    packet_str = "".join(values)
    packet = Packet.read_packet(packet_str)
    return packet.compute()


def parse_values(values):
    return ["{:04b}".format(int(c, 16)) for c in values[0]]


def main():
    filename = "./16.txt"
    values = read_trimmed(filename)
    print(q1(parse_values(values)))

    values = read_trimmed(filename)
    print(q2(parse_values(values)))


if __name__ == "__main__":
    main()
