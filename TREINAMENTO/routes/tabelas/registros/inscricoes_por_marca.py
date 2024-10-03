from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Inscricao, Marca
from .. import tabela_bp


@tabela_bp.route('/inscricoes/marca')
@login_required
def inscricoes_por_marca():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Consulta para trazer todas as inscrições relacionadas às marcas
    inscricoes = Inscricao.query.join(Marca).paginate(page=page, per_page=per_page)

    return render_template('/tabelas/registros/tabela_inscricoes_por_marca.html', inscricoes=inscricoes)
