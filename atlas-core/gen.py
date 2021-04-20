#!/usr/bin/env python3

import os
import click
import atlas

@click.command()
@click.option('--interface-path', required=True, help='Interface path')
def main(interface_path):
    """ Generate files """
    atlas_gen = atlas.AtlasGen(interface_path=os.path.abspath(interface_path))
    atlas_gen.generate()

if __name__ == '__main__':
    main()
