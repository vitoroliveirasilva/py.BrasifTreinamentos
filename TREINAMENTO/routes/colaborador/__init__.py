from flask import Blueprint

colaborador_bp = Blueprint('colaborador', __name__, url_prefix="/colaborador")

from .cadastro_colaborador_routes import *
from .edicao_colaborador_routes import *