from flask import Blueprint, render_template
from flask_login import login_required


menu_bp = Blueprint("menu", __name__)

@menu_bp.route("/", methods=["GET", "POST"])
@login_required
def menu():
    return render_template("/index.html")