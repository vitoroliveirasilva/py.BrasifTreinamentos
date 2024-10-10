from flask import render_template, request
from flask_login import login_required
from TREINAMENTO.models import Login, Colaborador
from .. import tabela_bp


@tabela_bp.route('/logins/colaborador/<int:id_colaborador>')
@login_required
def logins_por_colaborador(id_colaborador):
    # Busca o colaborador pelo ID, ou retorna 404 se não encontrar
    colaborador = Colaborador.query.get_or_404(id_colaborador)

    # Parâmetros de paginação
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

   # Consulta para trazer todos os logins por colaborador (ativos e inativos)
    logins = Login.query.filter_by(id_colaborador=id_colaborador).paginate(page=page, per_page=per_page, error_out=False)

    return render_template('/tabelas/associacoes/tabela_logins_por_colaborador.html', logins=logins, colaborador_nome=colaborador.nome)
