from path import Path
import atlas
from genpack import GenPack

class HtmlDocGenPack(GenPack):
    """ Generate HTML Documentation """
    def __init__(self, atlas_system: atlas.AtlasSystem):
        super().__init__(atlas_system)
        pass

    def __repr__(self):
        return f"HtmlDocGenPack"

    def __str__(self):
        return self.__repr__()

    def start_generation(self):
        for module in self.atlas_system.atlas_modules:
            print(f"module: {module}")
        pass

    def finish_generation(self):
        pass
