import svn

from PyWorks.IO import File, Directory
from PyWorks.IO.Path import Path
from PyWorks.SubVersion import Svn


class ExtraWorks:
    _source_link = r"https://github.com/MBijron/ExtraWorks/trunk/"
    _dest_path = r"..\..\ExtraWorks"

    @staticmethod
    def get_requirement(requirement):
        destination_path = Path.combine(ExtraWorks.__get_dest_path(), requirement) + "@"
        source_link = ExtraWorks._source_link + requirement + "@"
        try:
            Svn.export(source_link, destination_path, force=True, revision=None)
        except FileNotFoundError as e:
            raise Exception("Either cmd is not found, or svn is not installed on the system. Please make sure both are present and are added to path. tortoisesvn link: https://tortoisesvn.net/downloads.html")
        except svn.exception.SvnException as e:
            raise Exception("An svn exception occured. Does the given requirement exist?")

    @staticmethod
    def __get_dest_path():
        return Path.combine(Path.get_file_path(__file__), ExtraWorks._dest_path)

ExtraWorks.get_requirement("test_program@1.0.0")