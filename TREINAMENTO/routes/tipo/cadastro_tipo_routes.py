from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from TREINAMENTO.forms.tipo_forms import TipoForm
from TREINAMENTO.models import Tipo
from . import tipo_bp


@tipo_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro_tipo():
    form = TipoForm()

    if form.validate_on_submit():
        try:
            tipo = Tipo.cadastro_tipo(form)
            db.session.add(tipo)
            db.session.commit()
            flash("Tipo cadastrado com sucesso!", "success")
            return redirect(url_for("tabela.marcas_por_empresa"))

        except ValueError as ve:
            db.session.rollback()
            flash(str(ve), "warning")

        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f"Erro ao acessar o banco de dados: {str(e)}", "danger")

        except Exception as e:
            db.session.rollback()
            flash(f"Erro inesperado ao registrar o tipo: {str(e)}", "danger")
        
    return render_template("/cadastro/cadastro_tipo.html", form=form)
