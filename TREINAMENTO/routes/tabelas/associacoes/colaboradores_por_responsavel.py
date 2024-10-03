from flask import render_template, request
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.models import Colaborador, Responsavel
from .. import tabela_bp

@tabela_bp.route('/colaboradores/responsavel/<int:id_responsavel>')
@login_required
def colaboradores_por_responsavel(id_responsavel):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Consulta para trazer os colaboradores vinculados a um responsável específico
    colaboradores = db.session.query(Colaborador)\
        .filter(Colaborador.id_responsavel == id_responsavel)\
        .paginate(page=page, per_page=per_page)

    responsavel = Responsavel.query.get_or_404(id_responsavel)

    return render_template('tabelas/associacoes/tabela_colaboradores_por_responsavel.html', colaboradores=colaboradores, responsavel=responsavel)
