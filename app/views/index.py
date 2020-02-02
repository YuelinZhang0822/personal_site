from app import site
from flask import render_template
from app.models.wish import Wish
from app.managers.wish_manager import wish_manager as wm


@site.route("/", methods=["GET"])
def show_homepage():
    return render_template('index.html')
