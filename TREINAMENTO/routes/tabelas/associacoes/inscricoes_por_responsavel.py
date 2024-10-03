from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Inscricao, Treinamento, Colaborador, Marca, Responsavel
from .. import tabela_bp

@tabela_bp.route('/inscricoes/responsavel/<int:id_responsavel>')
@login_required
def inscricoes_por_responsavel(id_responsavel):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Consulta para trazer as inscrições feitas por um responsável específico, incluindo o colaborador
    inscricoes = db.session.query(Inscricao, Treinamento, Marca, Colaborador)\
        .join(Treinamento, Inscricao.id_treinamento == Treinamento.id_treinamento)\
        .join(Marca, Treinamento.id_marca == Marca.id_marca)\
        .join(Colaborador, Inscricao.id_colaborador == Colaborador.id_colaborador)\
        .filter(Inscricao.id_responsavel == id_responsavel)\
        .paginate(page=page, per_page=per_page)

    responsavel = Responsavel.query.get_or_404(id_responsavel)

    return render_template('/tabelas/associacoes/tabela_inscricoes_por_responsavel.html', inscricoes=inscricoes, responsavel=responsavel)
