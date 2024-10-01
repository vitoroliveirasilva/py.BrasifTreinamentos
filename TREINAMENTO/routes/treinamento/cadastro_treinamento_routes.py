from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import app, db
from TREINAMENTO.forms.treinamento_forms import TreinamentoForm
from TREINAMENTO.models import Treinamento, Marca

@app.route("/cadastro/treinamento", methods=["GET", "POST"])
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
        return redirect(url_for("cadastro_treinamento"))

    return render_template("/cadastro/cadastro_treinamento.html", form=form)
