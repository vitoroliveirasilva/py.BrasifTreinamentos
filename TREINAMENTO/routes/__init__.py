# Autenticação
from .autenticacao.autenticacao_routes import *

# Colaborador
from .colaborador.cadastro_colaborador_routes import cadastro_colaborador
from .colaborador.edicao_colaborador_routes import editar_colaborador

# Empresa
from .empresa.cadastro_empresa_routes import cadastro_empresa
from .empresa.edicao_empresa_routes import editar_empresa

# Login
from .login.cadastro_login_routes import cadastro_login
from .login.edicao_login_routes import editar_login

# Marca
from .marca.cadastro_marca_routes import cadastro_marca
from .marca.edicao_marca_routes import editar_marca

# Tipo
from .tipo.cadastro_tipo_routes import cadastro_tipo
from .tipo.edicao_tipo_routes import editar_tipo

# Treinamento
from .treinamento.cadastro_treinamento_routes import cadastro_treinamento
from .treinamento.edicao_treinamento_routes import editar_treinamento

# Responsável
from .responsavel.edicao_responsavel_routes import editar_responsavel