import os
import sys
import yaml


ALIAS = "alias.yaml"

def read_alias():
    args_list = sys.argv[1:]  # Not including the `main.py` itself
    if os.path.isfile(ALIAS) is False:
        os.system(f"touch {ALIAS}")
    assert os.path.isfile(ALIAS)

if __name__ == '__main__':
    pass
