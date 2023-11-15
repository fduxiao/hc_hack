from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).parent
device_info_file = HERE / "data" / "device" / "device_info.csv"


@dataclass
class ChipInfo:
    maybe_id: str  # 0x0 0x18  not sure what it is, behaviors like an id
    part_number: str  # 0x8 0x20
    series: str  # 0x10 0x28
    name: str  # 0x18 0x30
    device: str  # 0x20 0x38
    device_version: str  # 0x28 0x40
    package: str  # 0x30 0x48
    voltage: str  # 0x38 0x50
    speed: str  # 0x40 0x58
    f9: str  # 0x48 0x60
    args: tuple  # 0x50 0x68

    def __init__(self, maybe_id, part_number, series, name, device, device_version, package, voltage, speed, f9, *args):
        self.maybe_id = maybe_id
        self.part_number = part_number
        self.series = series
        self.name = name
        self.device = device
        self.device_version = device_version
        self.package = package
        self.voltage = voltage
        self.speed = speed
        self.f9 = f9
        self.args = args


class DeviceDB:
    """
    Device database
    """
    def __init__(self, path: str | Path = None):
        if not path:
            path = device_info_file
        self.chip_info_list: list[ChipInfo] = []
        self.load_data_file(path)

    def load_data_file(self, path: str | Path):
        path = Path(path)
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                self.chip_info_list.append(ChipInfo(*map(lambda x: x.strip(), line.split(","))))

    def find(self, part_number, name):
        for chip_info in self.chip_info_list:
            if chip_info.part_number == part_number and chip_info.name == name:
                return chip_info
        return None

    def find_by_part_number(self, part_number):
        result = []
        for chip_info in self.chip_info_list:
            if chip_info.part_number == part_number:
                result.append(chip_info)
        return result


if __name__ == '__main__':
    for ci in DeviceDB().chip_info_list:
        print(ci)
