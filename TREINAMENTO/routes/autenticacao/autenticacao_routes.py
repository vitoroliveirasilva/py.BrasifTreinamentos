from flask import render_template, redirect, url_for, request, session
from TREINAMENTO import app, login_manager, db
from TREINAMENTO.models import Responsavel
from flask_login import login_required, logout_user, login_user
from TREINAMENTO.utils import autenticacao_URL, autenticacao_token


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Gera a URL de autorização para autenticação
    auth_url = autenticacao_URL()
    # Renderiza a página de login, passando a URL de autorização como contexto
    return render_template('/autenticacao/autenticacao_login.html', auth_url=auth_url)


# Rota para receber o token de acesso após a autenticação
@app.route("/getAToken")
def get_token():
    code = request.args.get('code')
    if not code:
        return "No authorization code found", 400

    # Adquire o token de acesso usando o código de autorização
    result = autenticacao_token(code)

    if "access_token" in result:
        # Obtém as informações do usuário do token
        user_info = result.get("id_token_claims")
        user_email = user_info.get("preferred_username")  # Email do usuário
        user_name = user_info.get("name")  # Nome do usuário

        # Verifica se o usuário já existe no banco de dados
        user = Responsavel.query.filter_by(email=user_email).first()
        
        if not user:
            user = Responsavel(
                nome=user_name,
                email=user_email,
                id_azure_ad=user_info.get("oid"),
                permissao=True,
                status=True
            )
            db.session.add(user)
            db.session.commit()  # Salva o novo usuário no banco

        # Faz login do usuário
        login_user(user)
        return redirect("/cadastro/empresa")
    else:
        error = result.get("error")
        error_description = result.get("error_description")
        return f"Login failed: {error} - {error_description}", 401


# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect('/login')


# Usuário não autenticado
@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login')
