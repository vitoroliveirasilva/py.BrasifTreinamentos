from flask import render_template, request
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.models import Inscricao, Treinamento, Colaborador, Marca, Responsavel
from .. import tabela_bp

@tabela_bp.route('/inscricoes/colaborador/<int:id_colaborador>')
@login_required
def inscricoes_por_colaborador(id_colaborador):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # Consulta para trazer as inscrições de um colaborador específico com o responsável
    inscricoes = db.session.query(Inscricao, Treinamento, Marca, Responsavel)\
        .join(Treinamento, Inscricao.id_treinamento == Treinamento.id_treinamento)\
        .join(Marca, Treinamento.id_marca == Marca.id_marca)\
        .join(Responsavel, Inscricao.id_responsavel == Responsavel.id)\
        .filter(Inscricao.id_colaborador == id_colaborador)\
        .paginate(page=page, per_page=per_page)

    colaborador = Colaborador.query.get_or_404(id_colaborador)
    
    return render_template('/tabelas/associacoes/tabela_inscricoes_por_colaborador.html', inscricoes=inscricoes, colaborador=colaborador)
