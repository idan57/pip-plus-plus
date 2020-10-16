import os
import sys

from view.application.web_pipper_factory import FlaskPipperFactory

if __name__ == '__main__':
    app = FlaskPipperFactory.get_pipper()
    app.run()
