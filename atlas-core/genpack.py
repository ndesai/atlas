from path import Path
from qface.generator import Generator
import atlas
import logging

logger = logging.getLogger(__name__)

class GenPack(object):
    """ A Generation Pack """
    def __init__(self, atlas_system: atlas.AtlasSystem):
        self.template_paths = list()
        self.atlas_system = atlas_system
        self.template_path = ''
        self._generator = None
        self.context = { 'system': self.atlas_system }
        self.filters = dict()
        pass

    def setup(self):
        if self.template_path == '':
            logger.warning("template path is empty")
            return
        Generator.strict = True
        self._generator = Generator(search_path=self.template_path)
        self._generator.register_filters(self.filters)
        pass

    def generate(self):
        logger.info(f"start generation for genpack: {self}")
        self.start_generation()
        logger.info(f"finish generation for genpack: {self}")
        self.finish_generation()
        pass

    def start_generation(self):
        logger.error("start_generation not implemented")
        sys.exit(1)
        pass

    def finish_generation(self):
        logger.error("finish_generation not implemented")
        sys.exit(1)
        pass

    def generate_file(self, file_path, template, context={}, preserve=False, force=False):
        self._generator.write(file_path, template, context, preserve, force)
        pass

    def gen(self, template, file_path, context={}):
        context.update(self.context)
        self.generate_file(file_path, template, context, False, True)
        pass
