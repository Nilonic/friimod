import os
import importlib

def check_mod(mod_location):
    if(os.path.exists() == True):
        return 1
    else:
        return 0


import importlib

def load_mod(mod_location):
    """how to use:\n
    
    say i want to import a file in my current directory + 2 folders down, i'd do this:
    ```python
    load_mod("src.mod.friimod.helloworld")
    ```
    """
    modules = []
    modules_name = []

    # Import the module dynamically
    tmp = importlib.import_module(mod_location)

    # Get the list of functions from the module
    functions = [attr for attr in dir(tmp) if callable(getattr(tmp, attr))]

    # Append the functions to the 'modules' list
    for function_name in functions:
        modules.append(getattr(tmp, function_name))
        modules_name.append(function_name)

    return modules, modules_name


