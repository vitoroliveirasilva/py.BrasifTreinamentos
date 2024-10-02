from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Login, Colaborador, Marca
from .. import tabela_bp

@tabela_bp.route('/logins/colaborador/<int:id_colaborador>')
@login_required
def logins_por_usuario(id_colaborador):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Consulta para trazer os logins de um colaborador específico
    logins = db.session.query(Login, Marca)\
        .join(Marca, Login.id_marca == Marca.id_marca)\
        .filter(Login.id_colaborador == id_colaborador)\
        .paginate(page=page, per_page=per_page)

    colaborador = Colaborador.query.get_or_404(id_colaborador)
    
    return render_template('/tabelas/tabela_logins_por_usuario.html', logins=logins, colaborador=colaborador)
