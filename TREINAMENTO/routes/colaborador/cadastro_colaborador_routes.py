from flask import render_template, redirect, url_for, flash, session
from TREINAMENTO import app, db
from TREINAMENTO.forms.colaborador_forms import ColaboradorForm
from TREINAMENTO.models import Colaborador, Empresa

@app.route("/cadastro/colaborador", methods=["GET", "POST"])
def cadastro_colaborador():
    form = ColaboradorForm()
    
    # ID do responsável na sessão
    id_responsavel = session.get('user_id')

    empresas = Empresa.query.all()
    form.id_empresa.choices = [(empresa.id_empresa, empresa.nome_empresa) for empresa in empresas]

    if form.validate_on_submit():
        colaborador = Colaborador.cadastro_colaborador(form)
        colaborador.id_responsavel = id_responsavel
        db.session.add(colaborador)
        db.session.commit()
        flash("Colaborador cadastrado com sucesso!", "success")
        return redirect(url_for("cadastro_colaborador"))

    return render_template("/cadastro/cadastro_colaborador.html", form=form)
