from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).parent
device_info_file = HERE / "data" / "device" / "device_info.csv"


@dataclass
class ChipInfo:
    f0: str
    part_number: str
    f2: str
    f3: str
    f4: str
    device_version: str
    packing: str
    f7: str
    f8: str
    f9: str
    args: tuple

    def __init__(self, f0, part_number, f2, f3, f4, device_version, packing, f7, f8, f9, *args):
        self.f0 = f0
        self.part_number = part_number
        self.f2 = f2
        self.f3 = f3
        self.f4 = f4
        self.device_version = device_version
        self.packing = packing
        self.f7 = f7
        self.f8 = f8
        self.f9 = f9
        self.args = args


class DeviceDB:
    """
    Device database
    """
    def __init__(self, path: str | Path = None):
        if not path:
            path = device_info_file
        self.chip_info_list = []
        self.load_data_file(path)

    def load_data_file(self, path: str | Path):
        path = Path(path)
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                self.chip_info_list.append(ChipInfo(*map(lambda x: x.strip(), line.split(","))))


if __name__ == '__main__':
    DeviceDB()
