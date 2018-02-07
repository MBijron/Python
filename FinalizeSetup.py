from IO.Path import Path
import site
import importlib
import sys
import traceback
print("-    Installing and importing python library pypiwin32")
from Util.Packages import Packages
Packages.install('pypiwin32')
Packages.install('python-docx')

from Windows.Admin import Admin
from Windows.Environment import Environment

# the script needs admin to run
if not(Admin.isUserAdmin()):
    Admin.runAsAdmin()
    sys.exit(1)

def add_dir_to_path(name, dir):
    print("-    Adding value to the environment variable '" + name + "'")
    try:
        if(Environment.environment_variable_exists(name)):
            print("-        Environment varialbe '" + name + "' allready exists")
            pythonpath_value = Environment.get_environment_variable(name)
            if(dir not in pythonpath_value):
                print("-        Adding value to environment varialbe: '" + name + "'")
                if not(pythonpath_value.endswith(";")):
                    Environment.set_environment_variable(name, pythonpath_value + ";" + dir)
                else:
                    Environment.set_environment_variable(name, pythonpath_value + dir)
            else:
                print("-        Environment varialbe '" + name + "' allready has the correct value")
        else:
            print("-        Creating to environment varialbe '" + name + "'")
            Environment.set_environment_variable(name, dir)
    except:
        print("-        Something went wrong with the setup")
        print("-        Please send the following traceback of the error to a developer:")
        traceback.print_exc()

#print(Environment.get_environment_variable("Path"))
install_path = Path.scriptpath()
add_dir_to_path("PYTHONPATH", install_path)
add_dir_to_path("PATH", Path.combine(install_path, "Commands"))
add_dir_to_path("PATHEXT", ".PY")

print("-    Reloading python sys.path")
importlib.reload(site)
print("-    REMEMBER! you cant use the library in the current terminal. Please restart the terminal to reload the needed environment variables")
input("setup complete")