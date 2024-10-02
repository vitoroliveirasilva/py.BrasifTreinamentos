from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.forms.marca_forms import MarcaForm
from TREINAMENTO.models import Marca, Tipo
from . import marca_bp


@marca_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_marca(id):
    marca = Marca.query.get_or_404(id)
    form = MarcaForm(obj=marca)

    tipos = Tipo.query.all()
    form.id_tipo.choices = [(tipo.id_tipo, tipo.nome) for tipo in tipos]

    if form.validate_on_submit():
        Marca.atualizar_marca(marca, form)
        db.session.commit()
        flash("marca atualizado com sucesso!", "success")
        return redirect(url_for("marca.cadastro_marca"))

    return render_template("/edicao/edicao_marca.html", form=form, marca=marca)
