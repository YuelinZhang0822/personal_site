from personal_site import app
from flask import render_template
from personal_site.models.wish import Wish
from personal_site.managers.wish_manager import wish_manager as wm


@app.route("/", methods=["GET"])
def show_homepage():
    return render_template('index.html')
