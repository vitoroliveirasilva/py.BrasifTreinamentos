from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Responsavel
from sqlalchemy import desc
from . import tabela_bp


@tabela_bp.route('/responsaveis')
@login_required
def tabela_responsaveis():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    
    # Consulta para trazer os responsaveis
    responsaveis = db.session.query(Responsavel)\
        .filter(Responsavel.status == True)\
        .order_by(Responsavel.data_alteracao.desc())\
        .paginate(page=page, per_page=per_page)

    return render_template('/tabelas/tabela_responsaveis.html', responsaveis=responsaveis)
