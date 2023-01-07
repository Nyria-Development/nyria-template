from flask import Flask, render_template


class WebserverNyria(Flask):
    def __init__(self):
        super().__init__(__name__)

        @self.route("/")
        def index():
            return render_template("index.html")

        self.run()
