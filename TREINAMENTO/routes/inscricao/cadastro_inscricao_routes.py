from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from TREINAMENTO import db
from TREINAMENTO.forms.inscricao_forms import InscricaoForm
from TREINAMENTO.models import Inscricao, Colaborador, Treinamento
from . import inscricao_bp


@inscricao_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro_inscricao():
    form = InscricaoForm()

    colaboradores = Colaborador.query.all()
    form.id_colaborador.choices = [(colaborador.id_colaborador, colaborador.nome) for colaborador in colaboradores]

    treinamentos = Treinamento.query.all()
    form.id_treinamento.choices = [(treinamento.id_treinamento, treinamento.treinamento) for treinamento in treinamentos]

    if form.validate_on_submit():
        nova_inscricao = Inscricao.cadastro_inscricao(form, current_user.id)
        db.session.add(nova_inscricao)
        db.session.commit()
        flash("Inscrição cadastrada com sucesso!", "success")
        return redirect(url_for("operacoes.cadastro_inscricao"))

    return render_template("/operacao/cadastro_inscricao.html", form=form)
