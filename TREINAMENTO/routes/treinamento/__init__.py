from flask import Blueprint

treinamento_bp = Blueprint('treinamento', __name__, url_prefix="/treinamento")

from .cadastro_treinamento_routes import *
from .edicao_treinamento_routes import *