from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente
load_dotenv()

# Classe para configuração do Flask
class Config:
    
    # Configurações do BD
    DEBUG = os.getenv('DEBUG_MODE')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    # Método para verificação das variáveis críticas
    @staticmethod
    def validacao_config():
        if not Config.SQLALCHEMY_DATABASE_URI:
            raise ValueError("A variável de ambiente 'DATABASE_URL' não está configurada corretamente.")
        
        if not Config.SECRET_KEY:
            raise ValueError("A variável de ambiente 'SECRET_KEY' não está definida.")
        
Config.validacao_config()