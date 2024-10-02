from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.forms.treinamento_forms import TreinamentoForm
from TREINAMENTO.models import Treinamento, Marca
from . import treinamento_bp


@treinamento_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro_treinamento():
    form = TreinamentoForm()

    marcas = Marca.query.all()
    form.id_marca.choices = [(marca.id_marca, marca.nome) for marca in marcas]

    if form.validate_on_submit():
        treinamento = Treinamento.cadastro_treinamento(form)
        db.session.add(treinamento)
        db.session.commit()
        flash("Treinamento cadastrado com sucesso!", "success")
        return redirect(url_for("treinamento.cadastro_treinamento"))

    return render_template("/cadastro/cadastro_treinamento.html", form=form)
