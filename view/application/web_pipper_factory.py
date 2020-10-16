import pathlib

from flask import render_template, url_for, request

from view.application.flask_piper import FlaskPipper


class WebPipperFactory(object):
    @classmethod
    def get_pipper(cls, **kwargs):
        pass


class FlaskPipperFactory(WebPipperFactory):
    @classmethod
    def get_pipper(cls, **kwargs):
        app = FlaskPipper("Pipper")

        @app.route("/")
        def main_page():
            return render_template("home.html")

        @app.route("/about")
        def about():
            return render_template("about.html")

        @app.route("/submit", methods=['GET', 'POST'])
        def submit_request():
            data = request.data
            response = app.run_command(data, req_type=request.method)
            return response

        @app.route("/success")
        @app.route("/success/<msg>")
        def success_page(msg=""):
            return render_template("success.html", msg=msg)

        @app.route("/failure")
        @app.route("/failure/<msg>")
        def failure(msg=""):
            return render_template("failure.html", msg=msg)

        with app.test_request_context():
            cls.set_static()

        return app

    @classmethod
    def set_static(cls):
        proj_dir = pathlib.Path(__file__).parent.parent.parent
        static_path = proj_dir / "static"

        for static_file in static_path.iterdir():
            url_for("static", filename=static_file.name)
