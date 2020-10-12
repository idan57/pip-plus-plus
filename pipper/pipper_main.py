import logging
import os
from pathlib import Path

from utils.exceptions import PipException
from utils.file_searcher import PathlibFileSearcher


class Pipper(object):
    def __init__(self, **kwargs):
        if "args" not in kwargs:
            raise PipException("When using pip++ you should provide 'args'.")
        self.args = kwargs["args"]
        if "proxies" in kwargs:
            self.proxies = kwargs["proxies"]
        self.pip = self.get_pip()
        logging.info(f"Path to pip is: {self.pip}")

    def get_pip(self):
        pass

    def run_pip(self):
        args = f"{self.args['function']} {self.args['upgrade']} {self.args['package']}"
        if self.args['version']:
            args += f"=={self.args['version']}"
        logging.info(f"Runnning pip {self.args['function']} on the machine.")
        command = f"{self.pip} {args}"
        os.system(command)


class PipperLinux(Pipper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_pip(self):
        return "pip"


class PipperWindows(Pipper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_pip(self):
        head1 = Path("C:\\Program Files (x86)")
        head2 = Path("C:\\Program Files")
        result = PathlibFileSearcher.find_file(head1, "pip.exe")
        if result:
            result = PathlibFileSearcher.find_file(head2, "pip.exe")
        return str(result)
