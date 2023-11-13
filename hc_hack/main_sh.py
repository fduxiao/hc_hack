from enum import Enum, auto


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
        pass

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

    def run(self, rtype: RunType) -> "HCTaskEngine":
        pass
