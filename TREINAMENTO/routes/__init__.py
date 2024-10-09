from .menu_routes import menu_bp
from .autenticacao import autenticacao_bp
from .responsavel import responsavel_bp
from .colaborador import colaborador_bp
from .empresa import empresa_bp
from .login import login_bp
from .marca import marca_bp
from .tipo import tipo_bp
from .treinamento import treinamento_bp
from .tabelas import tabela_bp
from .inscricao import inscricao_bp
from .marca_tipo import marca_tipo_bp

def register_blueprint(app):
    app.register_blueprint(menu_bp)
    app.register_blueprint(autenticacao_bp)
    app.register_blueprint(responsavel_bp)
    app.register_blueprint(colaborador_bp)
    app.register_blueprint(empresa_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(marca_bp)
    app.register_blueprint(tipo_bp)
    app.register_blueprint(treinamento_bp)
    app.register_blueprint(tabela_bp)
    app.register_blueprint(inscricao_bp)
    app.register_blueprint(marca_tipo_bp)