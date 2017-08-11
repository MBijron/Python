from IO.Path import Path
import site
import importlib
import sys
import traceback
from setuptools import setup, find_packages
from Util.Packages import Packages
#needed for windows reasons
#print("-    Installing and importing python library pypiwin32")
#Packages.install('pypiwin32')
#from Windows.Admin import Admin
from Windows.Environment import Environment

#the script needs admin to run
#if not(Admin.isUserAdmin()):
#    Admin.runAsAdmin()
#    sys.exit(1)

setup(
    name='PythonMB',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',

    description='Yet another python library',
    long_description='Yet another python library, meant to be some sort of swiss knife solution',

    # The project's main homepage.
    url='https://github.com/MBijron/Python',

    # Author details
    author='-',
    author_email='markjex@hotmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords='python library',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['pypiwin32'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'test': ['coverage'],
    },
)

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
    except Exception as e:
        print("-        Something went wrong with the setup")
        print("-        Please send the following traceback of the error to a developer:")
        traceback.print_exc()

#print(Environment.get_environment_variable("Path"))
add_dir_to_path("PYTHONPATH", Path.scriptpath())
add_dir_to_path("PATH", Path.combine(Path.scriptpath(), "Commands"))
add_dir_to_path("PATHEXT", ".PY")

print("-    Reloading python sys.path")
importlib.reload(site)
print("-    REMEMBER! you cant use the library in the current terminal. Please restart the terminal to reload the needed environment variables")
input("setup complete")