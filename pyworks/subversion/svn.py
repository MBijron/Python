import svn.remote

class Svn:
    @staticmethod
    def export(source_link, to_path, revision=None, force=True):
        remote = svn.remote.RemoteClient(source_link)
        remote.export(to_path, revision, force)
