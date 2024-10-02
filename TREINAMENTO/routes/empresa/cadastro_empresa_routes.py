from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.forms.empresa_forms import EmpresaForm
from TREINAMENTO.models import Empresa
from . import empresa_bp 

@empresa_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro_empresa():
    form = EmpresaForm()
    if form.validate_on_submit():
        empresa = Empresa.cadastro_empresa(form)
        db.session.add(empresa)
        db.session.commit()
        flash("Empresa cadastrada com sucesso!", "success")
        return redirect(url_for("empresa.cadastro_empresa"))
    return render_template("/cadastro/cadastro_empresa.html", form=form)
