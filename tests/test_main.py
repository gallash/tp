"""
Following the TDD principles, this is the testing script for src/main.py
"""
import os
import pytest

from src import main

 
ALIAS = "aliases.yaml"

class TestMain_SaveCurrentDirectory:
    # @pytest.mark.skip(reason="This already works, and will not suffer changes later on")
    def test_creates_alias_file_when_there_is_none(self):
        # If there is no 'alias.yaml', check if main.py creates one
        if os.path.isfile(ALIAS) is False:
            main.read_alias()
        assert os.path.isfile(ALIAS)

    def test_save_current_dir_with_dot(self):
        
        pass
