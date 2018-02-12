# noinspection PyUnresolvedReferences
import install_packages
from pyworks_.io.path import Path
import site
import importlib
import sys
import traceback
from pyworks_.windows.admin import Admin
from pyworks_.windows.environment import Environment

# the script needs admin to run
if not (Admin.is_user_admin()):
    Admin.run_as_admin()
    sys.exit(1)


def __add_dir_to_path(name, directory) -> None:
    print("-    Adding value to the environment variable '" + name + "'")
    # noinspection PyBroadException
    try:
        if Environment.environment_variable_exists(name):
            print("-        Environment variable '" + name + "' already exists")
            python_path_value = Environment.get_environment_variable(name)
            if directory not in python_path_value:
                print("-        Adding value to environment variable: '" + name + "'")
                if not (python_path_value.endswith(";")):
                    Environment.set_environment_variable(name, python_path_value + ";" + directory)
                else:
                    Environment.set_environment_variable(name, python_path_value + directory)
            else:
                print("-        Environment variable '" + name + "' already has the correct value")
        else:
            print("-        Creating to environment variable '" + name + "'")
            Environment.set_environment_variable(name, directory)
    except Exception:
        print("-        Something went wrong with the setup")
        print("-        Please send the following traceback of the error to a developer:")
        traceback.print_exc()


# print(Environment.get_environment_variable("Path"))
install_path = Path.get_script_path()
# noinspection SpellCheckingInspection
__add_dir_to_path("PYTHONPATH", install_path)
# noinspection SpellCheckingInspection
__add_dir_to_path("PATH", Path.combine(install_path, "commands"))
# noinspection SpellCheckingInspection
__add_dir_to_path("PATHEXT", ".PY")

print("-    Reloading python sys.path")
importlib.reload(site)
print(
    "-    REMEMBER! you cant use the library in the current terminal. Please restart the terminal to reload the "
    "needed environment variables")
input("setup complete")
