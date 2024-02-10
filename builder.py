#!/usr/bin/python3
from asset_packer import pack
import pathlib

if __name__ == "__main__":
    here = pathlib.Path(__file__).absolute().parent
    pack(here, here / "asset_packs", logger=print)