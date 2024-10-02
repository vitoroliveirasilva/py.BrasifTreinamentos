from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Treinamento, Marca, Tipo
from sqlalchemy import desc
from . import tabela_bp


@tabela_bp.route('/treinamentos')
@login_required
def tabela_treinamentos():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    
    # Consulta para trazer os treinamentos com os dados de tipo e marca associados
    treinamentos = db.session.query(Treinamento, Marca, Tipo)\
        .join(Marca, Treinamento.id_marca == Marca.id_marca)\
        .join(Tipo, Marca.id_tipo == Tipo.id_tipo)\
        .filter(Treinamento.status == True, Marca.status == True, Tipo.status == True)\
        .order_by(Treinamento.data_criacao.desc())\
        .paginate(page=page, per_page=per_page)

    return render_template('/tabelas/tabela_treinamentos.html', treinamentos=treinamentos)
