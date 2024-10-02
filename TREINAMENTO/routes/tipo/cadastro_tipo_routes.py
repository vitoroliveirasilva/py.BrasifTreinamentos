from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.forms.tipo_forms import TipoForm
from TREINAMENTO.models import Tipo
from . import tipo_bp


@tipo_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro_tipo():
    form = TipoForm()

    if form.validate_on_submit():
        tipo = Tipo.cadastro_tipo(form)
        db.session.add(tipo)
        db.session.commit()
        flash("Tipo cadastrado com sucesso!", "success")
        return redirect(url_for("tipo.cadastro_tipo"))

    return render_template("/cadastro/cadastro_tipo.html", form=form)
