from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from TREINAMENTO import db
from TREINAMENTO.forms.inscricao_forms import InscricaoForm
from TREINAMENTO.models import Inscricao, Tipo, Treinamento, Marca
from . import inscricao_bp


@inscricao_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro_inscricao():
    form = InscricaoForm()

    # Preencher o dropdown de tipos
    tipos = Tipo.query.all()
    form.id_tipo.choices += [(tipo.id_tipo, tipo.nome) for tipo in tipos]

    if form.validate_on_submit():
        nova_inscricao = Inscricao.cadastro_inscricao(form, current_user.id)
        db.session.add(nova_inscricao)
        db.session.commit()
        flash("Inscrição cadastrada com sucesso!", "success")
        return redirect(url_for("inscricao.cadastro_inscricao"))
    # Se houver erros de validação no formulário
    elif form.errors:
        for campo, erros in form.errors.items():
            for erro in erros:
                flash(f'{campo.upper()}, ERRO: {erro}', 'warning')

    return render_template("/inscricoes/cadastro_inscricao.html", form=form)


# Rota para buscar as marcas com base no tipo escolhido
@inscricao_bp.route("/get_marcas", methods=["GET"])
@login_required
def get_marcas():
    tipo_id = request.args.get('tipo_id')
    marcas = Marca.query.filter_by(id_tipo=tipo_id).all()
    marcas_options = '<option value="">Selecione uma Marca</option>'
    for marca in marcas:
        marcas_options += f'<option value="{marca.id_marca}">{marca.nome}</option>'
    return marcas_options


# Rota para buscar os treinamentos com base na marca escolhida
@inscricao_bp.route("/get_treinamentos", methods=["GET"])
@login_required
def get_treinamentos():
    marca_id = request.args.get('marca_id')
    treinamentos = Treinamento.query.filter_by(id_marca=marca_id).all()
    treinamentos_options = '<option value="">Selecione um Treinamento</option>'
    for treinamento in treinamentos:
        treinamentos_options += f'<option value="{treinamento.id_treinamento}">{treinamento.treinamento}</option>'
    return treinamentos_options
