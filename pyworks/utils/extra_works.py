from svn.exception import SvnException

from pyworks.io.file import File
from pyworks.io.directory import Directory
from pyworks.io.path import Path
from pyworks.subversion.svn import Svn
from pyworks.utils.command_line_utils import CommandLineUtils


class ExtraWorks:
    _source_link = r"https://github.com/MBijron/ExtraWorks/trunk/"
    _dest_path = r"..\..\extraworks"

    @staticmethod
    def install_if_missing(requirement, prompt_user=True) -> str:
        if not ExtraWorks.requirement_installed(requirement):
            if prompt_user:
                if not CommandLineUtils.prompt_for_yes_no(
                        "The '" + requirement + "' extra is needed to continue. Install?"):
                    raise Exception("The user canceled the installation of '" + requirement + "'")
            ExtraWorks.install_requirement(requirement)
        return ExtraWorks.get_requirement_path(requirement)

    @staticmethod
    def install_requirement(requirement) -> str:
        destination_path = ExtraWorks.__get_absolute_requirement_path(requirement) + "@"
        source_link = ExtraWorks._source_link + requirement + "@"
        try:
            Svn.export(source_link, destination_path, force=True, revision=None)
            ExtraWorks.__run_requirement_scripts(requirement)
        except FileNotFoundError as e:
            raise Exception(
                "Either cmd is not found, or svn is not installed on the system. Please make sure both are present "
                "and are added to path. tortoisesvn link: https://tortoisesvn.net/downloads.html")
        except SvnException as e:
            raise Exception("An svn exception occurred. Does the given requirement exist?")
        return ExtraWorks.get_requirement_path(requirement)

    @staticmethod
    def requirement_installed(requirement) -> bool:
        destination_path = ExtraWorks.__get_absolute_requirement_path(requirement)
        if Directory.exists(destination_path):
            return True
        return False

    @staticmethod
    def get_requirement_path(requirement) -> str:
        if ExtraWorks.requirement_installed(requirement):
            return ExtraWorks.__get_absolute_requirement_path(requirement)
        raise Exception("The requirement '" + requirement + "' is not installed")

    @staticmethod
    def uninstall(requirement) -> None:
        if ExtraWorks.requirement_installed(requirement):
            path = ExtraWorks.__get_absolute_requirement_path(requirement)
            ExtraWorks.__run_requirement_scripts(requirement, cleanup=True)
            Directory.delete(path)

    @staticmethod
    def __run_requirement_scripts(requirement, cleanup=False) -> None:
        requirement_path = ExtraWorks.__get_absolute_requirement_path(requirement)
        installer_script_path = Path.combine(requirement_path, cleanup if "takedown.py" else "setup.py")
        file_exists = File.exists(installer_script_path)
        if file_exists:
            variables = {
                "script_path": Path.get_file_path(installer_script_path)
            }
            try:
                exec(open(installer_script_path).read(), globals(), variables)
            except Exception as e:
                raise Exception("Executing the setup script from the extra resulted in an error: " + str(e))
            finally:
                File.delete(installer_script_path)

    @staticmethod
    def __get_absolute_requirement_path(requirement) -> str:
        return Path.combine(ExtraWorks.__get_dest_path(), requirement)

    @staticmethod
    def __get_dest_path() -> str:
        return Path.combine(Path.get_file_path(__file__), ExtraWorks._dest_path)
