from Commands.Middleware.DateMiddleware import DateMiddleware
from Commands.Middleware.FileMiddleware import FileMiddleware
from Commands.Middleware.FolderMiddleware import FolderMiddleware
from Commands.Middleware.PathMiddleware import PathMiddleware


class Middleware:
    DATE = DateMiddleware()
    FILE = FileMiddleware()
    FOLDER = FolderMiddleware()
    PATH = PathMiddleware()
