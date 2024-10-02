from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.forms.inscricao_forms import InscricaoForm
from TREINAMENTO.models import Inscricao, Colaborador, Treinamento


operacoes_bp = Blueprint("operacoes", __name__)

@operacoes_bp.route("/cadastro/inscricao", methods=["GET", "POST"])
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
        return redirect(url_for("operacoes.cadastro_empresa"))

    return render_template("/operacao/cadastro_inscricao.html", form=form)
