from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Login, Colaborador, MarcaTipo
from . import tabela_bp


@tabela_bp.route('/logins')
@login_required
def tabela_logins():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    
    # Consulta para trazer os logins com os dados de colaboradores e marcas associadas
    logins = (
        db.session.query(Login)
        .join(Colaborador)
        .join(MarcaTipo)
        .filter(Login.status == True)
        .options(db.orm.selectinload(Login.colaborador), db.orm.selectinload(Login.marca_tipo))
        .paginate(page=page, per_page=per_page)
    )
    
    return render_template('/tabelas/tabela_logins.html', logins=logins)
