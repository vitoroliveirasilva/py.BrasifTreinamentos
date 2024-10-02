from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Login, Colaborador, Marca
from . import tabela_bp


@tabela_bp.route('/logins')
@login_required
def tabela_logins():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    
    # Consulta para trazer os logins com os dados de colaboradores e marcas associados
    logins = db.session.query(Login, Colaborador, Marca)\
        .join(Colaborador, Login.id_colaborador == Colaborador.id_colaborador)\
        .join(Marca, Login.id_marca == Marca.id_marca)\
        .filter(Login.status == True)\
        .paginate(page=page, per_page=per_page)
    
    return render_template('/tabelas/tabela_logins.html', logins=logins)
