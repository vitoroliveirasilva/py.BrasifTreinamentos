from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Login, Colaborador, Marca
from .. import tabela_bp

@tabela_bp.route('/logins/marca/<int:id_marca>')
@login_required
def logins_por_marca(id_marca):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Consulta para trazer os logins de uma marca específica
    logins = db.session.query(Login, Colaborador)\
        .join(Colaborador, Login.id_colaborador == Colaborador.id_colaborador)\
        .filter(Login.id_marca == id_marca)\
        .paginate(page=page, per_page=per_page)

    marca = Marca.query.get_or_404(id_marca)
    
    return render_template('/tabelas/tabela_logins_por_marca.html', logins=logins, marca=marca)
