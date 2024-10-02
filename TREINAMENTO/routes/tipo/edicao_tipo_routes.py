from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.forms.tipo_forms import TipoForm
from TREINAMENTO.models import Tipo


tipo_bp = Blueprint("tipo", __name__)

@tipo_bp.route("/editar/tipo/<int:id>", methods=["GET", "POST"])
@login_required
def editar_tipo(id):
    tipo = Tipo.query.get_or_404(id)
    form = TipoForm(obj=tipo)

    if form.validate_on_submit():
        Tipo.atualizar_tipo(tipo, form)
        db.session.commit()
        flash("Tipo atualizado com sucesso!", "success")
        return redirect(url_for("tipo.cadastro_tipo"))

    return render_template("/edicao/edicao_tipo.html", form=form, tipo=tipo)
