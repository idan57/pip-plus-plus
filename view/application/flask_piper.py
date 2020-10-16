import logging

from flask import Flask, redirect, url_for

from pipper.pipper_gen import PipperGenerator
from utils.exceptions import PipRequestException, PipException


class FlaskPipper(Flask):
    def run_command(self, data, req_type=None):
        if not req_type:
            logging.error("Didn't get requst type!")
            raise PipRequestException("Didn't get requst type!")
        if type == "POST":
            upgrade_arg = "-U"
            if data["option"] != "install":
                upgrade_arg = ""

            args = {
                "function": data["option"],
                "upgrade": upgrade_arg,
                "package": "package"
            }
            proxies = {
                "http": data["http-proxy"],
                "https": data["https-proxy"]
            }

            pipper = PipperGenerator.get_pipper(args=args, proxies=proxies)

            try:
                out = pipper.run_pip()
                return redirect(url_for('success', msg=out))
            except PipException as e:
                return redirect(url_for("failure", msg=str(e)))


