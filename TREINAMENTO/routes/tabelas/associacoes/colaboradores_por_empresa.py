from flask import render_template, request
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.models import Colaborador, Empresa
from .. import tabela_bp

@tabela_bp.route('/colaboradores/empresa/<int:id_empresa>')
@login_required
def colaboradores_por_empresa(id_empresa):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Consulta para trazer os colaboradores vinculados a uma empresa específica
    colaboradores = db.session.query(Colaborador)\
        .filter(Colaborador.id_empresa == id_empresa)\
        .paginate(page=page, per_page=per_page)

    empresa = Empresa.query.get_or_404(id_empresa)

    return render_template('/tabelas/associacoes/tabela_colaboradores_por_empresa.html', colaboradores=colaboradores, empresa=empresa)
