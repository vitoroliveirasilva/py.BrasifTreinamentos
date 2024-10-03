from flask import render_template, request
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.models import Inscricao, Colaborador, Treinamento, Marca, Responsavel
from .. import tabela_bp

@tabela_bp.route('/inscricoes/treinamento/<int:id_treinamento>')
@login_required
def inscricoes_por_treinamento(id_treinamento):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Consulta para trazer as inscrições de um treinamento específico, incluindo o responsável
    inscricoes = db.session.query(Inscricao, Colaborador, Marca, Responsavel)\
        .join(Colaborador, Inscricao.id_colaborador == Colaborador.id_colaborador)\
        .join(Treinamento, Inscricao.id_treinamento == Treinamento.id_treinamento)\
        .join(Marca, Treinamento.id_marca == Marca.id_marca)\
        .join(Responsavel, Inscricao.id_responsavel == Responsavel.id)\
        .filter(Inscricao.id_treinamento == id_treinamento)\
        .paginate(page=page, per_page=per_page)

    treinamento = Treinamento.query.get_or_404(id_treinamento)

    return render_template('/tabelas/associacoes/tabela_inscricoes_por_treinamento.html', inscricoes=inscricoes, treinamento=treinamento)
