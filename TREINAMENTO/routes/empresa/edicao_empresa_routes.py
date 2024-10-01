from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import app, db
from TREINAMENTO.forms.empresa_forms import EmpresaForm
from TREINAMENTO.models import Empresa

@app.route("/editar/empresa/<int:id>", methods=["GET", "POST"])
@login_required
def editar_empresa(id):
    empresa = Empresa.query.get_or_404(id)
    form = EmpresaForm(obj=empresa)

    if form.validate_on_submit():
        Empresa.atualizar_empresa(empresa, form)
        db.session.commit()
        flash("Empresa atualizado com sucesso!", "success")
        return redirect(url_for("cadastro_empresa"))

    return render_template("/edicao/edicao_empresa.html", form=form, empresa=empresa)