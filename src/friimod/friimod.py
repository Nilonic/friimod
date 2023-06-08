import os
import importlib

def check_mod(mod_location):
    "make sure that you ommit the .py extenson"
    if(os.path.exists() == True):
        return True
    else:
        return False


def load_mod(mod_location):
    modules = []
    tmp = importlib.import_module(mod_location)
    x = tmp.friiboot()
    for mod in x:
        modules.append(mod)
    
    return modules

