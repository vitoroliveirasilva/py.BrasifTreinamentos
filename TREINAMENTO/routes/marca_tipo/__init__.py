from flask import Blueprint

marca_tipo_bp = Blueprint('marca_tipo', __name__, url_prefix="/marca_tipo")

from .cadastro_marca_tipo_routes import *
from .edicao_marca_tipo_routes import *