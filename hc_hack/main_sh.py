from enum import Enum, auto
from typing import Optional
from .device import DeviceDB, ChipInfo


class RunType(Enum):
    Syn: int = auto()
    Pnr: int = auto()
    All: int = auto()


All = RunType.All
Pnr = RunType.Pnr
Syn = RunType.Syn


class HCTaskEngine:
    """
    HCTaskEngine
    """

    def __init__(self):
        self.device_db = DeviceDB()
        self.chip_info: Optional[ChipInfo] = None

    def add_file(self, *files, ftype=None) -> "HCTaskEngine":
        pass

    def rm_file(self, *files) -> "HCTaskEngine":
        pass

    def set_device(self, part_number, name=None, device_version=None) -> "HCTaskEngine":
        """
        set target device

        :param part_number: Device part number. e.g. GW1N-UV4LQ144C6/I5
        :param name: Device name. There could be several devices with the same part
                    number. If so, you need to specify the name. e.g. name=GW1N-4
        :param device_version: Device Version. e.g. device_version=NA|B|C|D
        :return: :py:class:`HCTaskEngine`
        """
        if device_version == "NA":
            device_version = ""
        if name is None or device_version is not None:
            parts = self.device_db.find_by_part_number(part_number)
            for chip_info in parts:
                if chip_info.device_version == device_version:
                    self.chip_info = chip_info
                    break
            else:
                if len(parts) == 1:
                    self.chip_info = parts[0]
                else:
                    raise ValueError(f"multiple devices found with part number {part_number}, specify version or name")
        elif name is not None:
            self.chip_info = self.device_db.find(part_number, name)
        if self.chip_info is None:
            raise ValueError(f"no such a device: {part_number} with name {name}, device_version {device_version}")
        if name is not None and name != self.chip_info.name:
            raise ValueError(f"no such a device: {part_number} with name {name}, device_version {device_version}")
        if device_version is not None and device_version != self.chip_info.device_version:
            raise ValueError(f"no such a device: {part_number} with name {name}, device_version {device_version}")
        return self

    def run(self, rtype: RunType) -> "HCTaskEngine":
        pass
