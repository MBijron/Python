import os


class Directory:
    @staticmethod
    def get_files() -> [str]:
        # onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        return 2

    @staticmethod
    def exists(directory):
        return os.path.isdir(directory)
