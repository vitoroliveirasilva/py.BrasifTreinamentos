from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Inscricao, Colaborador, Treinamento, Responsavel
from .. import tabela_bp


@tabela_bp.route('/inscricoes/pendentes')
@login_required
def inscricoes_pendentes():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    inscricoes = db.session.query(
        Inscricao,
        Colaborador.nome.label('nome_colaborador'),
        Treinamento.treinamento.label('nome_treinamento'),
        Responsavel.nome.label('nome_responsavel')
    ).join(Colaborador, Inscricao.id_colaborador == Colaborador.id_colaborador) \
     .join(Treinamento, Inscricao.id_treinamento == Treinamento.id_treinamento) \
     .join(Responsavel, Inscricao.id_responsavel == Responsavel.id) \
     .filter(Inscricao.status == 'Pendente') \
     .paginate(page=page, per_page=per_page)

    return render_template('tabelas/registros/tabela_inscricoes_pendentes.html', inscricoes=inscricoes)
