#!/usr/bin/env python3

import os
import click
from path import Path
import yaml
import logging
import logging.config
import atlas

here = Path(__file__).abspath().dirname()

logging.config.dictConfig(yaml.load((here / 'log.yaml').open()))
logger = logging.getLogger(__name__)

@click.command()
@click.option('--interface-path', required=True, help='Interface path')
def main(interface_path):
    """ Generate files """
    atlas_gen = atlas.AtlasGen(interface_path=os.path.abspath(interface_path))

    from genpack_htmldoc import HtmlDocGenPack
    atlas_gen.register_genpack(HtmlDocGenPack)

    from genpack_cpp import CppGenPack
    atlas_gen.register_genpack(CppGenPack)

    atlas_gen.generate()
    pass

if __name__ == '__main__':
    main()
