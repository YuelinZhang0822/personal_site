from app import site
from flask import render_template
from app.models.wish import Wish
from app.managers.wish_manager import wish_manager as wm


@site.route("/wishes", methods=["GET"])
def show_wish_list():
    # Import Wish here to avoid import looping
    all_wishes = wm.get_all()
    wishes = wm.many_to_dict(all_wishes)
    return render_template('wishes.html', wishes=wishes)