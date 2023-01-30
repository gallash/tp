import os
import sys
import yaml

# Better split this file. This one becomes io.py and the other becomes utils.py


ALIASES = "aliases.yaml"

def read_aliases():
    """
    Reads the aliases.yaml file and 
    """
    args_list = sys.argv[1:]  # Not including the `main.py` itself
    if os.path.isfile(ALIASES) is False:
        os.system(f"touch {ALIASES}")
    
    assert os.path.isfile(ALIASES)
    with open(ALIASES) as file:
        stored_aliases = file 
    return stored_aliases    


def save_current_dir(alias: str) -> None:
    

def tp()


if __name__ == '__main__':
    pass
