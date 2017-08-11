import pip
import importlib
import site

class Packages:
    @staticmethod
    def install(package):
        try:
            importlib.import_module(package)
        except ImportError:
            pip.main(['install', package])
            importlib.reload(site)
        #finally:
            #globals()[package] = importlib.import_module(package)