from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class FileType(Enum):
    Auto = 1
    Verilog = 2
    VHDL = 3
    NetList = 4
    CST = 5
    SDC = 6
    FDC = 7
    GC = 8
    GPA = 9
    GSC = 10
    Binary = 11
    Other = 12


suffix_map = {
    ".v": FileType.Verilog,
    ".vm": FileType.NetList,
    ".vo": FileType.NetList,
    ".vg": FileType.NetList,
    ".cst": FileType.CST,
    ".sdc": FileType.SDC,
    ".fdc": FileType.FDC,
    ".gao": FileType.GC,
    ".rao": FileType.GC,
    ".gpa": FileType.GPA,
    ".gsc": FileType.GSC,
    ".bin": FileType.Binary,
}


@dataclass
class DesignFile:
    path: Path
    file_type: FileType
    is_disable: bool

    def set_type(self):
        if self.file_type == FileType.Auto:
            suffix = self.path.suffix
            self.file_type = suffix_map.get(suffix, None)
            if self.file_type is None:
                raise TypeError(f"unknown ext name: {suffix}")
        return self
