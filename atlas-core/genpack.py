from path import Path
import atlas
import logging

logger = logging.getLogger(__name__)

class GenPack(object):
    """ A Generation Pack """
    def __init__(self, atlas_system: atlas.AtlasSystem):
        self.template_paths = list()
        self.atlas_system = atlas_system
        pass

    def generate(self):
        print(f"start generation for genpack: {self}")
        self.start_generation()
        print(f"finish generation for genpack: {self}")
        self.finish_generation()
        pass

    def start_generation(self):
        print(f"ERROR: start_generation not implemented")
        sys.exit(1)
        pass

    def finish_generation(self):
        print(f"ERROR: finish_generation not implemented")
        sys.exit(1)
        pass
