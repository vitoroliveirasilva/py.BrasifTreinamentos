# ========== IMPORTAÇÕES ==========
from flask import Flask # Flask
from flask_sqlalchemy import SQLAlchemy # Gerenciamento do Banco de dados
from flask_login import LoginManager # Gerenciamento do Login
from flask_wtf.csrf import CSRFProtect # Proteção contra ataques CSRF
from flask_session import Session # Gerenciamento da Sessão

# Configurações de ambiente
from app_config import Config


# ========== INICIALIZAÇÃO DE EXTENSÕES ==========
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


# ========== APP ==========
def create_app():
    # Configura a pasta static para importações como CSS e JS
    app = Flask(__name__, static_folder='./static')
    
    # Configuração do app
    app.config.from_object(Config)
    
    # Inicialização das extensões
    inicializacao_extensoes(app)

# Inicializa as exntesões com o app
def inicializacao_extensoes(app):
    
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)