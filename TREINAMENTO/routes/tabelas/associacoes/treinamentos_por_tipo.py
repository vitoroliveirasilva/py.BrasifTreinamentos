from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Treinamento, Tipo, Marca
from .. import tabela_bp


@tabela_bp.route('/treinamentos/tipo/<int:id>')
@login_required
def treinamentos_por_tipo(id):
    tipo = Tipo.query.get_or_404(id)
    
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Consulta para trazer os treinamentos de um tipo específico, incluindo a marca
    treinamentos = db.session.query(Treinamento).join(Marca)\
        .filter(Treinamento.id_tipo == id, Treinamento.status == True)\
        .paginate(page=page, per_page=per_page)
    
    return render_template('/tabelas/associacoes/tabela_treinamentos_por_tipo.html', treinamentos=treinamentos, tipo=tipo)
