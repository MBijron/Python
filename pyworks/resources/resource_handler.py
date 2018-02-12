from pyworks.io import File
from pyworks.io.path import Path


class ResourceHandler:

    @staticmethod
    def get_resource_path(resource):
        # TODO: write unit test
        if File.exists(Path.combine(Path.get_file_path(__file__), resource)):
            return Path.combine(Path.get_file_path(__file__), resource)
        else:
            raise Exception('The given resource could not be found')
