from app import site
from flask import render_template, request, session, jsonify
from app.models.image import Image
from app.managers.image_manager import image_manager as im


@site.route("/image/add", methods=["POST"])
def add_image():
    data = request.get_json()
    """
    (Pdb) type(jsd)
    <class 'dict'>

    """
    # Todo: implement backend logic
    return