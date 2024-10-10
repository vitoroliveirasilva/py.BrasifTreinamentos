from flask import render_template, request
from flask_login import login_required
from TREINAMENTO.models import Login, MarcaTipo
from .. import tabela_bp


@tabela_bp.route('/logins/marca_tipo/<int:id_marca_tipo>')
@login_required
def logins_por_marca_tipo(id_marca_tipo):
    # Busca a relação marca_tipo pelo ID, ou retorna 404 se não encontrar
    marca_tipo = MarcaTipo.query.get_or_404(id_marca_tipo)

    # Parâmetros de paginação
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

   # Consulta para trazer todos os logins por marca_tipo
    logins = Login.query.filter_by(id_marca_tipo=id_marca_tipo).paginate(page=page, per_page=per_page, error_out=False)

    return render_template('/tabelas/associacoes/tabela_logins_por_marca_tipo.html', logins=logins, marca_tipo=marca_tipo)
