from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.forms.colaborador_forms import ColaboradorForm
from TREINAMENTO.models import Colaborador, Empresa
from . import colaborador_bp


@colaborador_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_colaborador(id):
    colaborador = Colaborador.query.get_or_404(id)
    form = ColaboradorForm(obj=colaborador)
    
    empresas = Empresa.query.all()
    form.id_empresa.choices = [(empresa.id_empresa, empresa.nome_empresa) for empresa in empresas]

    if form.validate_on_submit():
        Colaborador.atualizar_colaborador(colaborador, form)
        db.session.commit()
        flash("Colaborador atualizado com sucesso!", "success")
        return redirect(url_for("colaborador.cadastro_colaborador"))

    return render_template("/edicao/edicao_colaborador.html", form=form, colaborador=colaborador)