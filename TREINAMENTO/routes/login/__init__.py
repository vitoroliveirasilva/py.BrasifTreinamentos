from flask import Blueprint

login_bp = Blueprint('login', __name__, url_prefix="/login")

from .cadastro_login_routes import *
from .edicao_login_routes import *