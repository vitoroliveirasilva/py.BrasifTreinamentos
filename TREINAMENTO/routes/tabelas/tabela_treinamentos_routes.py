from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Treinamento, Marca, Tipo, MarcaTipo
from sqlalchemy import desc
from . import tabela_bp


@tabela_bp.route('/treinamentos')
@login_required
def tabela_treinamentos():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    
    # Consulta para trazer os treinamentos com dados de tipo e marca associados
    treinamentos = db.session.query(Treinamento).join(MarcaTipo).join(Marca).join(Tipo).filter(
        Treinamento.status == True
    ).order_by(desc(Treinamento.data_criacao)).paginate(page=page, per_page=per_page)

    return render_template('/tabelas/tabela_treinamentos.html', treinamentos=treinamentos)
