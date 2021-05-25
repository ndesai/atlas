import atlas
from genpack import GenPack
import pathlib

class HtmlDocGenPack(GenPack):
    """ Generate HTML Documentation """
    def __init__(self, atlas_system: atlas.AtlasSystem):
        super().__init__(atlas_system)

        # Set up configuration
        script_path = pathlib.Path(__file__).parent.absolute()
        self.template_path = f"{script_path}/templates"

        self.setup()
        pass

    def __repr__(self):
        return f"HtmlDocGenPack"

    def __str__(self):
        return self.__repr__()

    def start_generation(self):
        self.gen("Index.tpl.html", "output/Index.html")
        for module in self.atlas_system.atlas_modules:
            print(f"module: {module}")
        pass

    def finish_generation(self):
        pass
