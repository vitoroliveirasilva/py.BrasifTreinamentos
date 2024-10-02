from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.forms.treinamento_forms import TreinamentoForm
from TREINAMENTO.models import Treinamento, Marca
from . import treinamento_bp


@treinamento_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_treinamento(id):
    treinamento = Treinamento.query.get_or_404(id)
    form = TreinamentoForm(obj=treinamento)

    marcas = Marca.query.all()
    form.id_marca.choices = [(marca.id_marca, marca.nome) for marca in marcas]

    if form.validate_on_submit():
        Treinamento.atualizar_treinamento(treinamento, form)
        db.session.commit()
        flash("Treinamento atualizado com sucesso!", "success")
        return redirect(url_for("tipo.cadastro_tipo"))
    
    return render_template("/edicao/edicao_treinamento.html", form=form, treinamento=treinamento)
