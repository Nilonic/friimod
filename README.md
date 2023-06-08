# friimod

friimod is a Python library that provides functions for checking and loading modules dynamically.

## Installation

You can install friimod using pip:

```shell
pip install friimod
```

## Functions

### `check_mod(mod_location)`

This function checks if a module exists at the specified `mod_location`.

- Parameters:
  - `mod_location` (str): The location of the module to check.

- Returns:
  - `1` (int): If the module exists at the specified location.
  - `0` (int): If the module does not exist.

### `load_mod(mod_location)`

This function loads a module dynamically and returns a list of its functions.

- Parameters:
  - `mod_location` (str): The location of the module to load.

- Returns:
  - List[str]: A list of functions available in the loaded module.

### `abort()`

This function terminates the program and does not return.

- Returns:
  - No return value.

## Example Usage

Here's an example demonstrating the usage of friimod:

```python
import friimod

# Check if a module exists
result = friimod.check_mod("path/to/module.py")
if result == 1:
    print("Module exists!")
else:
    print("Module does not exist!")

# Load a module and get its functions
functions = friimod.load_mod("path/to/module.py")
print("Functions in the module:", functions)

# Abort the program
friimod.abort()
#note that this KILLS the process, no returns, just exits the process with no mercy
```

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/spyspy69/friimod/blob/master/LICENCE) file for details.
