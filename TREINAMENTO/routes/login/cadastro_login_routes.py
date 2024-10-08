from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from TREINAMENTO.forms.login_forms import LoginForm
from TREINAMENTO.models import Login, Colaborador, Marca
from . import login_bp 


@login_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro_login():
    form = LoginForm()

    try:
        colaboradores = Colaborador.query.filter_by(status=True).all()
        marcas = Marca.query.filter_by(status=True).all()

        if not colaboradores:
            flash("Nenhum colaborador encontrado. Por favor, cadastre um colaborador antes de cadastrar um login.", "warning")
            form.id_colaborador.choices = []
        else:
            form.id_colaborador.choices = [(colaborador.id_colaborador, colaborador.nome) for colaborador in colaboradores]

        if not marcas:
            flash("Nenhuma marca encontrada. Por favor, cadastre uma marca antes de cadastrar um login.", "warning")
            form.id_marca.choices = []
        else:
            form.id_marca.choices = [(marca.id_marca, marca.nome) for marca in marcas]

    except SQLAlchemyError as e:
        flash(f"Erro ao acessar o banco de dados ao carregar colaboradores e marcas: {str(e)}", "danger")
        form.id_colaborador.choices = []
        form.id_marca.choices = []
        
    except Exception as e:
        flash(f"Erro inesperado ao carregar as opções: {str(e)}", "danger")
        form.id_colaborador.choices = []
        form.id_marca.choices = []


    if form.validate_on_submit():
        try:
            novo_login = Login.cadastro_login(form)
            db.session.add(novo_login)
            db.session.commit()
            flash("Login cadastrado com sucesso!", "success")
            return redirect(url_for("login.cadastro_login"))
        
        except ValueError as ve:
            db.session.rollback()
            flash(str(ve), "warning")

        except SQLAlchemyError as e:
            db.session.rollback()
            if "uq_usuario_marca" in str(e):
                flash("Já existe um login para este usuário e marca.", "danger")
            else:
                flash(f"Erro ao acessar o banco de dados: {str(e)}", "danger")

        except Exception as e:
            db.session.rollback()
            flash(f"Erro inesperado: {str(e)}", "danger")

    return render_template("/cadastro/cadastro_login.html", form=form)
