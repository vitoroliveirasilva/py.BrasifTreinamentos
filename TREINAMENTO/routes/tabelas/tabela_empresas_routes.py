from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Empresa
from . import tabela_bp


@tabela_bp.route('/empresas')
@login_required
def tabela_empresas():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    
    # Consulta para trazer as empresas
    empresas = db.session.query(Empresa)\
        .filter(Empresa.status == True)\
        .order_by(Empresa.nome_empresa)\
        .paginate(page=page, per_page=per_page)

    return render_template('/tabelas/tabela_empresas.html', empresas=empresas)
