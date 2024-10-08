from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Treinamento, Marca, Tipo
from sqlalchemy import desc
from . import tabela_bp


@tabela_bp.route('/marcas')
@login_required
def tabela_marcas():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    
    # Consulta para trazer os marcas
    marcas = db.session.query(Marca)\
        .filter(Marca.status == True)\
        .order_by(Marca.nome)\
        .paginate(page=page, per_page=per_page)


    return render_template('/tabelas/tabela_marcas.html', marcas=marcas)
