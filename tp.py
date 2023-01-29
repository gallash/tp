"""
tp - teleport
Fast travel through your system

Usage:
    `tp` sends the user to the directory pointed by 'project'

Options:
    The options the user has are related to creating an alias for a directory, manage the saved aliases and creating and managing the bases (namespaces for aliases).

Alias: passing the name of the alias will tp the user there. E.g., for an alias named 'project', `tp project` will send the user to the project's directory

-s, --save: Save the alias under an identifiable name. Requires a location ('.' is a valid option as the location). Name at this moment is optional (will be asked later if not passed here)


-b, --base: Just like namespaces in C++, or workspace in Linux, it separates contexts. So two same-named aliases can coexist, but in different bases. This option will change from the current base to chosen one (changes DEFAULT_BASE in the YAML file). The system starts with a default one

-B, --base-create: creates a new base. Requires a name. Can include a short description

--base-rename: renames currently selected base

--base-list: lists all bases and their descriptions (if any)

--base-delete: deletes given base (and all their aliases)

--base-delete-all: deletes all bases


-l, --list: Lists all saved aliases

-d, --delete: Deletes an alias and its location

-D, --Delete: Deletes all aliases and their location
"""

import sys
import subprocess
import argparse

from src import main
# from src import utils  # Not necessary for the time being
from src import exceptions


ROOT_DIR = ''  # Absolute path to this tp.py


def parsing():
    parser = argparse.ArgumentParser(description=__doc__)

    # Adding arguments
    parser.add_argument(
            '-s', '--save',
            type=str,
            help="Save a location. Requires a location ('.' is a valid option)."
    )
    parser.add_argument(
            '--alias',
            type=str,
            help="Alias to be given to a directory."
    )

    return parser.parse_args()


def actions_manager(args):
    """
    Manages the options' functionalities
    """
    if args.save is not None:
        main.save_alias(args.save, args.alias)

    # In the future, add --list, --delete, --base, etc


if __name__ == '__main__':
    main.check_whether_aliases_file_exists()

    if len(sys.argv) == 2:
        try:
            absolute_path = main.get_alias(sys.argv[1])  # Can raise "LocationNotFound"
        except Exception as e:
            print(e)
        else:
            main.tp(absolute_path)
    else:
        args = parsing()
        actions_manager(args)
