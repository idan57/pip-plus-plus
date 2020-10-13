class PipException(Exception):
    pass


class PipNotInstalledException(PipException):
    pass


class PipInstallException(PipException):
    pass


class PipUnInstallException(PipException):
    pass
