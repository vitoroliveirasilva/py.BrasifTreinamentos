from flask import Blueprint

tipo_bp = Blueprint('tipo', __name__, url_prefix="/tipo")

from .cadastro_tipo_routes import *
from .edicao_tipo_routes import *