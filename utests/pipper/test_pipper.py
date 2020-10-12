import platform
from unittest import mock

from pipper.pipper_gen import PipperGenerator
from pipper.pipper_main import PipperWindows


@mock.patch.object(platform, "system", lambda: "Windows")
@mock.patch.object(PipperWindows, "get_pip", lambda x: "mock")
def test_windows_pipper():
    piper = PipperGenerator.get_pipper(args={"install": True})


def test_windows_search_pip():
    if platform.system() == "Windows":
        _ = PipperGenerator.get_pipper(args={"install": True})
    else:
        assert True
