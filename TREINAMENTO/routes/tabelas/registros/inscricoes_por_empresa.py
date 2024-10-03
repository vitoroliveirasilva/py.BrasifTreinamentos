from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Inscricao, Empresa, Colaborador, Responsavel
from .. import tabela_bp


@tabela_bp.route('/inscricoes/empresa')
@login_required
def inscricoes_por_empresa():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    inscricoes = db.session.query(Inscricao) \
        .join(Colaborador, Inscricao.id_colaborador == Colaborador.id_colaborador) \
        .join(Empresa, Colaborador.id_empresa == Empresa.id_empresa) \
        .join(Responsavel, Colaborador.id_responsavel == Responsavel.id) \
        .paginate(page=page, per_page=per_page)

    return render_template('/tabelas/registros/tabela_inscricoes_por_empresa.html', inscricoes=inscricoes)
