from flask import url_for
from msal import ConfidentialClientApplication
from app_config import Config


# Gera a URL de autorização para autenticação com a Microsoft Identity Platform.
def autenticacao_URL():
    client = ConfidentialClientApplication(
        Config.CLIENT_ID, authority=Config.AUTHORITY, client_credential=Config.CLIENT_SECRET
    )
    return client.get_authorization_request_url(Config.SCOPE, redirect_uri=url_for('autenticacao.get_token', _external=True))


# Adquire um token de acesso usando o código de autorização fornecido.
# Recebe o código de autorização e retorna o resultado da requisição para obter o token de acesso
def autenticacao_token(code):
    client = ConfidentialClientApplication(
        Config.CLIENT_ID, authority=Config.AUTHORITY, client_credential=Config.CLIENT_SECRET
    )

    return client.acquire_token_by_authorization_code(
        code, scopes=Config.SCOPE, redirect_uri=url_for('autenticacao.get_token', _external=True)
    )