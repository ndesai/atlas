from path import Path
import atlas

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


