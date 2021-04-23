#!/usr/bin/env python3

import pytest
import os
import atlas

@pytest.fixture()
def atlas_gen(request):
    interface_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "interfaces")
    atlas_gen = atlas.AtlasGen(interface_path=interface_path)
    atlas_gen.generate()
    yield atlas_gen

def test_atlas_gen(atlas_gen):
    assert atlas_gen != None

def test_valid_atlas_system(atlas_gen):
    assert atlas_gen.system != None
    assert atlas_gen.system.is_system_initialized == True

def test_invalid_atlas_system():
    interface_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "interfaces")
    atlas_gen = atlas.AtlasGen(interface_path=interface_path)
    # Generate was never called, the system will not be initialized
    assert atlas_gen.system != None
    assert atlas_gen.system.is_system_initialized == False

