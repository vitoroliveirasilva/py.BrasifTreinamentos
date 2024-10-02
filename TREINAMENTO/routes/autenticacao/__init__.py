from flask import Blueprint

autenticacao_bp = Blueprint('autenticacao', __name__)

from .autenticacao_routes import *