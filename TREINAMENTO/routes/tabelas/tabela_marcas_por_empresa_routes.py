from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import MarcaTipo
from . import tabela_bp


@tabela_bp.route('/marcas_por_tipo')
@login_required
def marcas_por_tipo():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Consulta para buscar apenas o nome da marca e o tipo, filtrando por itens ativos
    marcas_tipo = (
        db.session.query(MarcaTipo)
        .join(MarcaTipo.marca)
        .join(MarcaTipo.tipo)
        .filter(MarcaTipo.marca.has(status=True))
        .filter(MarcaTipo.tipo.has(status=True))
        .paginate(page=page, per_page=per_page)
    )

    return render_template('/tabelas/tabela_marcas_por_tipo.html', marcas_tipo=marcas_tipo)
