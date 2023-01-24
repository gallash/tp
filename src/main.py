import os
import sys
import yaml


ALIASES = "aliases.yaml"

def read_alias():
    args_list = sys.argv[1:]  # Not including the `main.py` itself
    if os.path.isfile(ALIASES) is False:
        os.system(f"touch {ALIASES}")
    assert os.path.isfile(ALIASES)

if __name__ == '__main__':
    pass
