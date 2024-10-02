from flask import Blueprint, render_template, redirect, url_for, flash
from TREINAMENTO import db
from flask_login import login_required
from TREINAMENTO.forms.empresa_forms import EmpresaForm
from TREINAMENTO.models import Empresa


empresa_bp = Blueprint("empresa", __name__)

@empresa_bp.route("/cadastro/empresa", methods=["GET", "POST"])
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
