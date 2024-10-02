from flask import Blueprint

marca_bp = Blueprint('marca', __name__, url_prefix="/marca")

from .cadastro_marca_routes import *
from .edicao_marca_routes import *