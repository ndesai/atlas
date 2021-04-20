from path import Path
from qface.generator import FileSystem, Generator
import qface.idl.domain as domain

class AtlasGen:
    """ AtlasGen """

    def __init__(self, interface_path):
        self.interface_path = interface_path

    def generate(self):
        print(f"generate interfaces from path: {self.interface_path}")
        self.qface_system = FileSystem.parse(self.interface_path)

