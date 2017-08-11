from IO.File import File
from IO.Path import Path

class ResourceHandler:

    @staticmethod
    def getpath(resource):
        # TODO: write unit test
        if(File.exists(Path.combine(Path.fromfile(__file__), resource))):
            return Path.combine(Path.fromfile(__file__), resource)
        else:
            raise Exception('The given resource could not be found')
