import logging
import subprocess
import sys

from utils.exceptions import PipException, PipNotInstalledException, PipInstallException, PipUnInstallException

EXCEPTIONS = {
    "install": PipInstallException,
    "uninstall": PipUnInstallException
}


class Pipper(object):
    def __init__(self, **kwargs):
        if "args" not in kwargs:
            raise PipException("When using pip++ you should provide 'args'.")
        self.args = kwargs["args"]
        if "proxies" in kwargs:
            self.proxies = kwargs["proxies"]
        self.version = ""
        if "version" in kwargs:
            self.version = kwargs["version"]
        self.pip = self.get_pip()
        logging.info(f"Path to pip is: {self.pip}")

    def get_pip(self):
        pass

    def is_pip_install(self, pip_command=None):
        pass

    def run_pip(self):
        args = f"{self.args['function']} {self.args['upgrade']} {self.args['package']}"
        if self.args['version']:
            args += f"=={self.args['version']}"
        logging.info(f"Runnning pip {self.args['function']} on the machine.")
        command = self.get_run_command(args)
        proc = subprocess.run(command)
        if proc.returncode:
            logging.warn(f"Failed to {self.args['function']} the package!")
            raise EXCEPTIONS[self.args["functions"]]

    def get_run_command(self, args):
        pass


class PipperLinux(Pipper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_pip(self):
        if not self.is_pip_install():
            logging.info("pip is not installed, installing pip")
            self.install_pip()
        return f"pip{self.version}"

    def is_pip_install(self, pip_command=None):
        proc = subprocess.run([f"pip{self.version}"] + ["list"])
        return proc.returncode

    def install_pip(self):
        p = subprocess.run(["sudo", f"apt-get install pip{self.version}"])
        if p.returncode:
            logging.warn("Failed to install pip!")
            raise PipNotInstalledException("Failed to install pip")

    def get_run_command(self, args):
        return [self.pip, args]


class PipperWindows(Pipper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_pip(self):
        pip_command = [sys.executable, f"-m pip{self.version}"]
        if not self.is_pip_install(pip_command):
            logging.warn("pip is not installed on the machine")
            raise PipNotInstalledException("pip is not installed on the machine")
        return pip_command

    def is_pip_install(self, pip_command=None):
        executable = pip_command[0]
        pip = pip_command[1]
        proc = subprocess.run([executable] + [f"{pip} list"])
        return proc.returncode

    def get_run_command(self, args):
        executable = self.pip[0]
        pip = self.pip[1]
        return [executable, f"{pip} args"]
