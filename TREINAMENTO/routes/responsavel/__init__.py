from flask import Blueprint

responsavel_bp = Blueprint('responsavel', __name__, url_prefix="/responsavel")

from .edicao_responsavel_routes import *