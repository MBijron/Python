import svn.remote

class Svn:
    @staticmethod
    def export(source_link, to_path, revision=None, force=True):
        remote = svn.remote.RemoteClient(source_link)
        remote.export(to_path, revision, force)

    @staticmethod
    def export_test():
        remote = svn.remote.RemoteClient(r"https://github.com/MBijron/ExtraWorks/trunk/test_program_no_version")
        remote.export("test_program_no_version")
