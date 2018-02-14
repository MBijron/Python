import pip
import importlib
import site


def install(required_package) -> None:
    print("-    Installing and importing python library " + required_package)
    try:
        importlib.import_module(required_package)
    except ImportError:
        pip.main(['install', required_package])
        importlib.reload(site)
