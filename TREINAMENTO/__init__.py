# ========== IMPORTAÇÕES ==========
from flask import Flask # Flask
from flask_sqlalchemy import SQLAlchemy # Gerenciamento do Banco de dados
from flask_login import LoginManager # Gerenciamento do Login
from flask_wtf.csrf import CSRFProtect # Proteção contra ataques CSRF
from flask_session import Session # Gerenciamento da Sessão
from TREINAMENTO.models import Responsavel # Tabela com os usuários do sistema

# Configurações de ambiente
from app_config import Config


# ========== INICIALIZAÇÃO DE EXTENSÕES ==========
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


# ========== APP ==========
def criacao_app():
    # Configura a pasta static para importações como CSS e JS
    app = Flask(__name__, static_folder='./static')

    # Configuração do app
    app.config.from_object(Config)

    # inicialização de extensões Flask com o app
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Inicialização do Flask-Session
    Session(app)

    # Carrega as informações do usuário através do id
    @login_manager.user_loader
    def load_user(user_id):
        return Responsavel.query.get(int(user_id))

    return app

# Criação do objeto app
app = criacao_app()

# Importação das rotas após a inicialização do aplicativo
with app.app_context():
    from TREINAMENTO import routes
