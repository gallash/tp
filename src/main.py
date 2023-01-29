import os
import sys
import yaml
import types

# Better split this file. This one stays as main.py and the other becomes 
# utils.py


ALIASES = "aliases.yaml"


def read_aliases_file() -> dict:
    """
    Reads aliases file. A function for this will help me if I decide to change
    the extention to TOML

    :returns aliases: The dictionary containing all data stored in the file
    """
    with open(ALIASES) as file:
        aliases = yaml.load(file, Loader=yaml.FullLoader)

    return aliases


def create_default_aliases_file() -> None:
    """
    Creates an empty aliases file (with some basic configurations)
    """
    with open(ALIASES, 'w') as file:
        init_config = dict()
        init_config['BaseList'] = ['default']
        init_config['Base'] = init_config['BaseList'][0]  # = default
        
        init_config['default'] = {}  # 'default' base is created empty

        yaml.dump(init_config, file)


def does_dir_path_exist():
    """ 
    True -> dir_path exists
    False -> it does not exist 
    """
    pass


def get_alias(alias: str):
    """
    Searches for the given alias in the base
    
    :params alias: String of the name of the alias for the directory
    :returns dir_path | False: String of the location, if found, or False if no
    alias was found
    """
    # Read aliases of the default base from the aliases file
    file = read_aliases_file()
    aliases = list(file[file['Base']].keys())

    if alias in aliases:
        return aliases[alias]
    return False


def check_whether_aliases_file_exists() -> dict:
    """
    Checks whether aliases file exists. If it does not, the function creates 
    one and returns it.
    
    :returns aliases: a dictionary containing all data stored in aliases.
    """
    if os.path.isfile(ALIASES) is False:
        os.system(f"touch {ALIASES}")
    
    if isinstance(read_aliases_file(), types.NoneType):
        create_default_aliases_file()
    
    assert os.path.isfile(ALIASES)
    aliases = read_aliases_file()
    return aliases 


def check_given_alias(alias: str = None) -> str:
    """
    If 'alias' is given and is in the correct format -> returns the corrected
    format if necessary
    """
    if alias is None:
        alias = input("Give the alias a name (alphanumeric):\t")

    # Checking for incorrect formatting
    loop = True
    while(loop):
        if alias == "" or not alias.isalnum():
            print("Please name it with letters and/or digits")
            continue
        
        #try:
        #    assert alias != ""
        #except:
        #    raise AliasCannotBeAnEmptyString("Please name it with letters 
        #            and/or numbers")

        #try:
        #    assert alias.isalnum()
        #except:
        #    print(AliasCannotHaveSpecialCharacters("Please name it with
        #            letters and/or digits"))

        # Removing blank spaces and separating strings with an underscore
        try:
            alias = alias.lstrip().rstrip().replace(' ', '_')  # Does nothing 
            # if it is already formatted

            # Checks whether alias is already saved in the Base
            if get_alias(alias):
                raise Exception(f"{alias} is already in use. Choose another name")
        except Exception as e:
            print(e)
            alias = input("Alias (alphanumeric):\t")
        else:
            loop = False

    # If 'alias' is not given -> ask for one
    # If 'alias' is not in the correct format -> try to correct it. 
    # If not possible to put it in the correct format ->  ask the user for 
    #  another name
    # If the given alias is already registered in the base -> ask the user if 
    #  he/she wishes to repurpose this alias (give it a new directory to point
    #  to), or if he/she wishes to choose another name
    return alias


def save_alias(dir_path: str, alias: str = None) -> None:
    """
    Save alias will perform checks to see whether this connection can be
    saved, and then it will save it, should it be allowed. Otherwise, 
    it will return to the user what went awry
    """
    # Checks existance of the target directory, and shape it into the correct 
    # format
    if dir_path == '.':
        dir_path = os.getcwd()  # Check if this function returns the 
        # directory where the user is, or if it returns the directory where tp
        # is installed
    else:
        assert does_dir_path_exist(dir_path), "The directory could not be found"
    
    # Checks if an alias was given. If none was given, prompt the user for one
    alias = check_given_alias(alias)

    # If all checks are OK, save the alias in the file
    file = read_aliases_file()
    with open(ALIASES, 'w') as f:
        try:
            file[file['Base']][alias] = dir_path
            yaml.dump(file, f)
        except Exception as e:
            print(e)
        else:
            print(f"'{alias}' which points to {dir_path} was saved successfully")


def tp(absolute_path: str) -> None:
    pass


if __name__ == '__main__':
    pass
