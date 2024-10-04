from flask import Blueprint

inscricao_bp = Blueprint('inscricao', __name__, url_prefix="/inscricao")

from .inscricao_treinamento_routes import *
from .inscricao_colaborador_routes import *