from flask import Blueprint

inscricao_bp = Blueprint('inscricao', __name__, url_prefix="/inscricao")

from .cadastro_inscricao_routes import *