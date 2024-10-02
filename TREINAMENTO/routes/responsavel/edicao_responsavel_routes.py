from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.forms.responsavel_forms import ResponsavelForm
from TREINAMENTO.models import Responsavel


responsavel_bp = Blueprint("responsavel", __name__)

@responsavel_bp.route("/editar/responsavel/<int:id>", methods=["GET", "POST"])
@login_required
def editar_responsavel(id):
    responsavel = Responsavel.query.get_or_404(id)
    form = ResponsavelForm(obj=responsavel)

    if form.validate_on_submit():
        responsavel.atualizar_responsavel(form)
        db.session.commit()
        flash("Responsável atualizado com sucesso!", "success")
        return redirect(url_for("responsavel.cadastro_empresa"))

    return render_template("/edicao/edicao_responsavel.html", form=form, responsavel=responsavel)
