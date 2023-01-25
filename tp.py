"""
tp - teleport
Fast travel through your system

Usage:
tp project: Sends the user to the directory pointed by 'project'

Options
-s, --save: Save the alias under an identifiable name. Requires a location ('.' is a valid option as the location). Name at this moment is optional (will be asked later if not passed here)
-l, --list: Lists all saved aliases
-d, --delete: Deletes an alias and its location
-D, --Delete: Deletes all aliases and their location
"""

import sys
import subprocess
import argparse

from src import io
from src import utils
from src import exceptions


def parsing():
    parser = argparse.ArgumentParser(description=__doc__)

    # Adding arguments
    parser.add_argument(
            '-s', '--save',
            type=str,
            help="Save a location. Requires a location ('.' is a valid option)."
    )


def tp():
    pass

if __name__ == '__main__':
    if len(sys.argv) == 2:
        # This function imports io.read_aliases, checks whether the given alias is there, returns the location and we tp the user there
        try:
            utils.get_location(sys.argv[1])  # Can raise "LocationNotFound"
        except Exception as e:
            print(e)
        tp()
    else:
        args = parsing()
