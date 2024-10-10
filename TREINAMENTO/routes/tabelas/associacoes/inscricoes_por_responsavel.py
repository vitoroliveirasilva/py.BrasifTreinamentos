from flask import render_template, request
from flask_login import login_required
from TREINAMENTO.models import Inscricao, Responsavel
from .. import tabela_bp

@tabela_bp.route('/inscricoes/responsavel/<int:id_responsavel>')
@login_required
def inscricoes_por_responsavel(id_responsavel):
    # Busca o responsável pelo ID, ou retorna 404 se não encontrar
    responsavel = Responsavel.query.get_or_404(id_responsavel)

    # Parâmetros de paginação
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Faz a consulta de todas as inscrições vinculadas ao responsável, sem filtrar por status
    inscricoes = Inscricao.query.filter_by(id_responsavel=id_responsavel).paginate(page=page, per_page=per_page)

    return render_template('/tabelas/associacoes/tabela_inscricoes_por_responsavel.html', inscricoes=inscricoes, responsavel_name=responsavel.nome)
