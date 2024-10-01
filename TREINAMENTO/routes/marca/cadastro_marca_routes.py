from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import app, db
from TREINAMENTO.forms.marca_forms import MarcaForm
from TREINAMENTO.models import Marca, Tipo

@app.route("/cadastro/marca", methods=["GET", "POST"])
@login_required
def cadastro_marca():
    form = MarcaForm()

    tipos = Tipo.query.all()
    form.id_tipo.choices = [(tipo.id_tipo, tipo.nome) for tipo in tipos]

    if form.validate_on_submit():
        marca = Marca.cadastro_marca(form)
        db.session.add(marca)
        db.session.commit()
        flash("Marca cadastrada com sucesso!", "success")
        return redirect(url_for("cadastro_marca"))

    return render_template("/cadastro/cadastro_marca.html", form=form)
