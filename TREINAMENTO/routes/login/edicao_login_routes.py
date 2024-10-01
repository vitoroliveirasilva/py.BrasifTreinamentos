from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import app, db
from TREINAMENTO.forms.login.edicao_login_forms import LoginForm
from TREINAMENTO.models import Login, Colaborador, Marca

@app.route("/editar/login/<int:id>", methods=["GET", "POST"])
@login_required
def editar_login(id):
    login = Login.query.get_or_404(id)
    form = LoginForm(obj=login)

    colaboradores = Colaborador.query.all()
    form.id_colaborador.choices = [(colaborador.id_colaborador, colaborador.nome) for colaborador in colaboradores]

    marcas = Marca.query.all()
    form.id_marca.choices = [(marca.id_marca, marca.nome) for marca in marcas]

    if form.validate_on_submit():
        Login.atualizar_login(login, form)
        db.session.commit()
        flash("Login atualizado com sucesso!", "success")
        return redirect(url_for("cadastro_login"))

    return render_template("/edicao/edicao_login.html", form=form, login=login)