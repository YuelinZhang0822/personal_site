from app import site
from flask import render_template


@site.route("/", methods=["GET"])
def show_homepage():
    return render_template('index.html')
