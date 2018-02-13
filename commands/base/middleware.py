from commands.middleware import AnyMiddleware
from commands.middleware.date_middleware import DateMiddleware
from commands.middleware.file_middleware import FileMiddleware
from commands.middleware.folder_middleware import FolderMiddleware
from commands.middleware.path_middleware import PathMiddleware


class Middleware:
    DATE = DateMiddleware()
    FILE = FileMiddleware()
    FOLDER = FolderMiddleware()
    PATH = PathMiddleware()
    ANY = AnyMiddleware()
