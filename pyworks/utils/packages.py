import pip
import importlib
import site


class Packages:
    @staticmethod
    def install(package) -> None:
        # TODO: write unit test
        try:
            importlib.import_module(package)
        except ImportError:
            pip.main(['install', package])
            importlib.reload(site)
