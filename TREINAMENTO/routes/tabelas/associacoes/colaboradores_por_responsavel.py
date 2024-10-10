from flask import render_template, request
from flask_login import login_required, current_user
from TREINAMENTO.models import Colaborador
from .. import tabela_bp

@tabela_bp.route('/colaboradores/responsavel/<int:id_responsavel>')
@login_required
def colaboradores_por_responsavel(id_responsavel):
    # Parâmetros de paginação
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    
    # Consulta para trazer todos os colaboradores por responsável (ativos e inativos)
    colaboradores = Colaborador.query.filter_by(id_responsavel=id_responsavel).paginate(page=page, per_page=per_page, error_out=False)

    # Nome do responsável
    responsavel_name = current_user.nome

    return render_template('tabelas/associacoes/tabela_colaboradores_por_responsavel.html', colaboradores=colaboradores, responsavel_name=responsavel_name)
