import svn

from PyWorks.IO import File, Directory
from PyWorks.IO.Path import Path
from PyWorks.SubVersion import Svn


class ExtraWorks:
    _source_link = r"https://github.com/MBijron/ExtraWorks/trunk/"
    _dest_path = r"..\..\ExtraWorks"

    @staticmethod
    def install_requirement(requirement):
        destination_path = ExtraWorks.__get_absolute_requirement_path(requirement) + "@"
        source_link = ExtraWorks._source_link + requirement + "@"
        try:
            Svn.export(source_link, destination_path, force=True, revision=None)
            ExtraWorks.__run_requirement_scripts(requirement)
        except FileNotFoundError as e:
            raise Exception("Either cmd is not found, or svn is not installed on the system. Please make sure both are present and are added to path. tortoisesvn link: https://tortoisesvn.net/downloads.html")
        except svn.exception.SvnException as e:
            raise Exception("An svn exception occurred. Does the given requirement exist?")

    @staticmethod
    def requirement_installed(requirement):
        destination_path = ExtraWorks.__get_absolute_requirement_path(requirement)
        if Directory.exists(destination_path):
            return True
        return False

    @staticmethod
    def get_requirement_path(requirement):
        if ExtraWorks.requirement_installed(requirement):
            return ExtraWorks.__get_absolute_requirement_path()
        raise Exception("The requirement '" + requirement + "' is not installed")

    @staticmethod
    def __run_requirement_scripts(requirement):
        requirement_path = ExtraWorks.__get_absolute_requirement_path(requirement)
        installer_script_path = Path.combine(requirement_path, "setup.py")
        if File.exists(installer_script_path):
            variables = {
                "script_path": Path.get_file_path(installer_script_path)
            }
            try:
                exec(open(installer_script_path).read(), globals(), variables)
            except Exception as e:
                raise Exception("Executing the setup script from the extra resulted in an error: " + str(e))
            File.delete(installer_script_path)

    @staticmethod
    def __get_absolute_requirement_path(requirement):
        return Path.combine(ExtraWorks.__get_dest_path(), requirement)

    @staticmethod
    def __get_dest_path():
        return Path.combine(Path.get_script_path(), ExtraWorks._dest_path)

ExtraWorks.install_requirement("with_installer@1.1.2")