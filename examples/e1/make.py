#!/usr/bin/env python3
from pathlib import Path
import hc_hack

HERE = Path(__file__).parent.absolute()


task_engine = hc_hack.HCTaskEngine().set_device("GW1NR-LV9QN88PC6/I5", name="GW1NR-9")
task_engine.add_file(HERE / "design.v", HERE / "tangnano9k.cst")

if __name__ == '__main__':
    print(task_engine.design_files)
