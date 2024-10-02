from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Tipo
from sqlalchemy import desc
from . import tabela_bp


@tabela_bp.route('/tipos')
@login_required
def tabela_tipos():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    
    # Consulta para trazer os Tipos
    tipos = db.session.query(Tipo)\
        .filter(Tipo.status == True)\
        .order_by(Tipo.nome)\
        .paginate(page=page, per_page=per_page)

    return render_template('/tabelas/tabela_tipos.html', tipos=tipos)
