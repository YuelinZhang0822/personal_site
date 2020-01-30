from personal_site import app
from flask import render_template
from personal_site.models.wish import Wish
from personal_site.managers.wish_manager import wish_manager as wm


@app.route("/", methods=["GET"])
def show_wish_list():
    # Import Wish here to avoid import looping
    all_wishes = wm.get_all()
    wishes = wm.many_to_dict(all_wishes)
    return render_template('index.html', wishes=wishes)
