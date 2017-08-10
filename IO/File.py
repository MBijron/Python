
class File:
    @staticmethod
    def readtext(path):
        with open(path, 'r', encoding='iso-8859-1') as file:
            return file.read()

    @staticmethod
    def readlines(path):
        with open(path, 'r', encoding='iso-8859-1') as file:
            return file.readlines()
