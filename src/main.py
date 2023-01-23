import os
import sys
import yaml


ALIAS = "../alias.yaml"

def read_alias():
    args_list = sys.argv[1:]  # Not including the `main.py` itself
    if os.path.isfile(ALIAS) is False:
        os.execute("cd .. && touch alias.yaml")

if __name__ == '__main__':
    pass
