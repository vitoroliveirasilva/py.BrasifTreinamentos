from .menu_routes import menu_bp
from .autenticacao.autenticacao_routes import autenticacao_bp
from .colaborador.cadastro_colaborador_routes import colaborador_bp
from .empresa.cadastro_empresa_routes import empresa_bp
from .login.cadastro_login_routes import login_bp
from .marca.cadastro_marca_routes import marca_bp
from .operacoes.cadastro_inscricao_routes import operacoes_bp
from .responsavel.edicao_responsavel_routes import responsavel_bp
from .tipo.cadastro_tipo_routes import tipo_bp
from .treinamento.cadastro_treinamento_routes import treinamento_bp

def register_blueprint(app):
    app.register_blueprint(menu_bp)
    app.register_blueprint(autenticacao_bp)
    app.register_blueprint(colaborador_bp)
    app.register_blueprint(empresa_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(marca_bp)
    app.register_blueprint(operacoes_bp)
    app.register_blueprint(responsavel_bp)
    app.register_blueprint(tipo_bp)
    app.register_blueprint(treinamento_bp)
