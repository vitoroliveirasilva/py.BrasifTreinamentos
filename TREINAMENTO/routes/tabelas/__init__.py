from flask import Blueprint

tabela_bp = Blueprint('tabela', __name__, url_prefix="/tabela")

from .tabela_tipos_routes import *
from .tabela_marcas_routes import *
from .tabela_treinamentos_routes import *

from .tabela_responsaveis_routes import *
from .tabela_empresas_routes import *
from .tabela_colaboradores_routes import *
from .tabela_logins_routes import *

from .associacoes import *

from .registros import *