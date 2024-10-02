from flask import Blueprint

empresa_bp = Blueprint('empresa', __name__, url_prefix="/empresa")

from .cadastro_empresa_routes import *
from .edicao_empresa_routes import *
