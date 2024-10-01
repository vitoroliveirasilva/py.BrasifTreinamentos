from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import app, db
from TREINAMENTO.forms.inscricao_forms import InscricaoForm
from TREINAMENTO.models import Inscricao, Colaborador, Treinamento

@app.route("/cadastro/inscricao", methods=["GET", "POST"])
@login_required
def cadastro_inscricao():
    form = InscricaoForm()

    colaboradores = Colaborador.query.all()
    form.id_colaborador.choices = [(colaborador.id_colaborador, colaborador.nome) for colaborador in colaboradores]

    treinamentos = Treinamento.query.all()
    form.id_treinamento.choices = [(treinamento.id_treinamento, treinamento.treinamento) for treinamento in treinamentos]

    if form.validate_on_submit():
        nova_inscricao = Inscricao.cadastro_inscricao(form)
        db.session.add(nova_inscricao)
        db.session.commit()
        flash("Inscrição cadastrada com sucesso!", "success")
        return redirect(url_for("cadastro_empresa"))

    return render_template("/operacao/cadastro_inscricao.html", form=form)
