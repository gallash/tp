"""
Following the TDD principles, this is the testing script for src/main.py
"""
import os
import pytest

from src import main

 
ALIASES = "aliases.yaml"  # from the root dir

class TestMain_SaveCurrentDirectory:
    # @pytest.mark.skip(reason="This already works, and will not suffer changes later on")
    def test_creates_aliases_file_when_there_is_none(self):
        # If there is no 'aliases.yaml', check if main.py creates one
        if os.path.isfile(ALIASES) is False:
            main.read_alias()
        assert os.path.isfile(ALIASES)

    # @pytest.mark.skip(reason="This already works, and will not suffer changes later on")
    def test_if_aliases_file_is_empty(self):
        with open(ALIASES) as file:
            file = yaml.load(file)
            assert file.__len__() == 0

    def test_save_current_dir_with_dot(self):
        main.save_current_dir(alias="TEST_ALIAS_TP")
        with open(ALIASES) as file:
            assert file['TEST_ALIAS_TP'] == os.getcwd()

    def test_save_dir_passed_as_string(self):
        pass

    def test_returns_error_for_non_existent_dirs(self):
        pass

    def test_if_name_of_saved_directories_are_separated_by_underscore(self):
        pass

    def test_selecting_alias_does_tp_the_user_to_the_targeted_dir(self):
        """ Read these articles
        https://docs.python.org/3/library/subprocess.html
        https://stackoverflow.com/questions/13745648/running-bash-script-from-within-python
        These will help me through the configuration of calling a bash script from withing Python
        """
        # Checks whether passing '..' will make the system tp the user to one directory above
        main.tp('..')
        assert os.getcwd() == os.path.abspath('..')

    def test_removes_the_selected_alias(self):
        pass

    def test_updates_the_selected_alias(self):
        pass
