from flask import render_template, redirect, url_for, flash, session,request
from flask_login import login_required, current_user
from TREINAMENTO import db
from sqlalchemy import and_
from TREINAMENTO.forms.inscricao import InscricaoColaboradorForm
from TREINAMENTO.models import Inscricao, Treinamento, Filiais, Colaborador
from . import inscricao_bp


@inscricao_bp.route("/<int:id>/colaboradores", methods=["GET", "POST"])
@login_required
def inscricao_colaborador(id):
    treinamento = Treinamento.query.get_or_404(id)
    form = InscricaoColaboradorForm()

    form.filial.choices += [(filial.name, filial.value) for filial in Filiais]

    # Se houver um valor de filial na sessão, define como o valor padrão do formulário
    if 'inscricao_colaborador_filial' in session:
        filial_session = session['inscricao_colaborador_filial']
        form.filial.data = filial_session
        
        colaboradores = Colaborador.query.filter_by(status=True)\
            .filter(Colaborador.id_responsavel == current_user.id)\
            .filter(Colaborador.filial == filial_session).all()
    else:
        colaboradores = Colaborador.query.filter_by(status=True)\
            .filter(Colaborador.id_responsavel == current_user.id).all()

    form.id_colaborador.choices += [(colaborador.id_colaborador, colaborador.nome) for colaborador in colaboradores]

    if form.validate_on_submit():
        session['inscricao_colaborador_filial'] = form.filial.data
        nova_inscricao = Inscricao.cadastro_inscricao(form, current_user.id, treinamento.id_treinamento)
        db.session.add(nova_inscricao)
        db.session.commit()
        flash("Inscrição cadastrada com sucesso!", "success")
        return redirect(url_for("inscricao.inscricao_colaborador", id=treinamento.id_treinamento))
    elif form.errors:
        for campo, erros in form.errors.items():
            for erro in erros:
                flash(f'{campo.upper()} ERRO: {erro}', 'warning')
    
    session.pop('inscricao_colaborador_filial', None)
    return render_template("/inscricao/inscricao_colaborador.html", form=form, treinamento=treinamento)


@inscricao_bp.route("/get_colaboradores", methods=["GET"])
@login_required
def get_colaboradores():
    filial = request.args.get('filial')

    colaboradores = Colaborador.query.filter_by(status=True)\
        .filter(Colaborador.id_responsavel == current_user.id)\
        .filter(Colaborador.filial == filial).all()

    colaboradores_options = '<option value="">Selecione um colaborador</option>'
    
    colaboradores_options += ''.join(f'<option value="{colaborador.id_colaborador}">{colaborador.nome}</option>' for colaborador in colaboradores)

    return colaboradores_options
