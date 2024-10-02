from flask import Blueprint

tabela_bp = Blueprint('tabela', __name__, url_prefix="/tabela")

from .tabela_marcas_routes import *
from .tabela_treinamentos_routes import *