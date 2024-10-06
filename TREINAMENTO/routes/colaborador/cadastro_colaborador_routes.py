from flask import render_template, redirect, url_for, flash, request
from TREINAMENTO import db
from flask_login import login_required, current_user
from TREINAMENTO.forms.colaborador_forms import ColaboradorForm
from TREINAMENTO.models import Colaborador, Empresa, Filiais
from . import colaborador_bp


@colaborador_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro_colaborador():
    form = ColaboradorForm()

    id_responsavel = current_user.id

    form.filial.choices += [(filial.name, filial.value) for filial in Filiais]

    empresas = Empresa.query.all()
    form.id_empresa.choices = [(empresa.id_empresa, empresa.nome_empresa) for empresa in empresas]

    if form.validate_on_submit():
        colaborador = Colaborador.cadastro_colaborador(form)
        colaborador.id_responsavel = id_responsavel
        db.session.add(colaborador)
        db.session.commit()
        flash("Colaborador cadastrado com sucesso!", "success")
        return redirect(url_for("colaborador.cadastro_colaborador"))
    # Se houver erros de validação no formulário
    elif form.errors:
        for campo, erros in form.errors.items():
            for erro in erros:
                flash(f'{campo.upper()} ERRO: {erro}', 'warning')

    return render_template("/cadastro/cadastro_colaborador.html", form=form)

@colaborador_bp.route("/get_empresa", methods=["GET"])
@login_required
def get_empresas():
    filial = request.args.get('filial')
    empresas = Empresa.query.filter_by(filial=filial).all()
    empresas_options = '<option value="">Selecione uma Empresa</option>'
    empresas_options += ''.join(f'<option value="{empresa.id_empresa}">{empresa.nome_empresa}</option>' for empresa in empresas)
    return empresas_options
