from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from TREINAMENTO.forms.login_forms import LoginForm
from TREINAMENTO.models import Login, Colaborador, Marca


login_bp = Blueprint("login", __name__)

@login_bp.route("/cadastro/login", methods=["GET", "POST"])
@login_required
def cadastro_login():
    form = LoginForm()

    colaboradores = Colaborador.query.all()
    form.id_colaborador.choices = [(colaborador.id_colaborador, colaborador.nome) for colaborador in colaboradores]

    marcas = Marca.query.all()
    form.id_marca.choices = [(marca.id_marca, marca.nome) for marca in marcas]

    if form.validate_on_submit():
        novo_login = Login.cadastro_login(form)
        db.session.add(novo_login)
        db.session.commit()
        flash("Login cadastrado com sucesso!", "success")
        return redirect(url_for("login.cadastro_login"))

    return render_template("/cadastro/cadastro_login.html", form=form)
