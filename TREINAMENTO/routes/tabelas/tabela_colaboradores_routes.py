from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Colaborador, Empresa
from sqlalchemy import desc
from . import tabela_bp


@tabela_bp.route('/colaboradores')
@login_required
def tabela_colaboradores():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    
    # Consulta para trazer os colaboradores com os dados de empresas associadas
    colaboradores = Colaborador.query\
        .join(Empresa)\
        .filter(Colaborador.status == True, Empresa.status == True)\
        .paginate(page=page, per_page=per_page)

    return render_template('/tabelas/tabela_colaboradores.html', colaboradores=colaboradores)
