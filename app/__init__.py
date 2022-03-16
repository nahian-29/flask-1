"""A simple flask web app"""
from flask import Flask, render_template
from app.context_processors import utility_text_processors
from app.simple_pages import simple_pages


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    @app.route("/")
    @app.route("/base.html")
    def index():
        return render_template("base.html")
    @app.route("/git.html")
    def git():
        return render_template("/git.html")
    @app.route("/git.html")
    def git():
        return render_template("/git.html")

    return app

