from flask import render_template, request
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.models import Inscricao, Colaborador, Treinamento, Responsavel
from .. import tabela_bp


@tabela_bp.route('/inscricoes')
@login_required
def inscricoes():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Atualizando o nome do campo para usar 'id_colaborador'
    inscricoes = db.session.query(
        Inscricao,
        Colaborador.nome.label('nome_colaborador'),
        Treinamento.treinamento.label('nome_treinamento'),
        Responsavel.nome.label('nome_responsavel')
    ).join(Colaborador, Inscricao.id_colaborador == Colaborador.id_colaborador) \
     .join(Treinamento, Inscricao.id_treinamento == Treinamento.id_treinamento) \
     .join(Responsavel, Inscricao.id_responsavel == Responsavel.id) \
     .paginate(page=page, per_page=per_page)

    return render_template('tabelas/registros/tabela_inscricoes.html', inscricoes=inscricoes)
