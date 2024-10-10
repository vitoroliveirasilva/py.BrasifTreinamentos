from flask import render_template, request
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.models import Colaborador, Empresa
from .. import tabela_bp

@tabela_bp.route('/colaboradores/empresa/<int:id_empresa>')
@login_required
def colaboradores_por_empresa(id_empresa):

    # Busca a empresa pelo ID, ou retorna 404 se não encontrar
    empresa = Empresa.query.get_or_404(id_empresa)

    # Parâmetros de paginação
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Consulta para trazer todos os colaboradores por empresa (ativos e inativos)
    colaboradores = Colaborador.query.filter_by(id_empresa=id_empresa).paginate(page=page, per_page=per_page, error_out=False)

    return render_template('/tabelas/associacoes/tabela_colaboradores_por_empresa.html', colaboradores=colaboradores, empresa_nome=empresa.nome_empresa)
