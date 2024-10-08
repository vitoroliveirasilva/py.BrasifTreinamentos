from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from TREINAMENTO.forms.marca_forms import MarcaForm
from TREINAMENTO.models import Marca, Tipo
from . import marca_bp


@marca_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro_marca():
    form = MarcaForm()

    try:
        tipos = Tipo.query.filter_by(status=True).all()

        if not tipos:
            flash("Nenhum tipo encontrado. Por favor, cadastre um tipo antes de cadastrar uma marca.", "warning")
            form.id_tipo.choices = []
        else:
            form.id_tipo.choices = [(tipo.id_tipo, tipo.nome) for tipo in tipos]
            
    except SQLAlchemyError as e:
        flash(f"Erro ao acessar o banco de dados ao carregar os tipos: {str(e)}", "danger")
        form.id_tipo.choices = []

    except Exception as e:
        flash(f"Erro inesperado: {str(e)}", "danger")
        form.id_tipo.choices = []

    
    if form.validate_on_submit():
        try:
            marca = Marca.cadastro_marca(form)
            db.session.add(marca)
            db.session.commit()
            flash("Marca cadastrada com sucesso!", "success")
            return redirect(url_for("marca.cadastro_marca"))
        
        except ValueError as ve:
            db.session.rollback()
            flash(str(ve), "warning")

        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f"Erro ao acessar o banco de dados: {str(e)}", "danger")

        except Exception as e:
            db.session.rollback()
            flash(f"Erro inesperado: {str(e)}", "danger")


    return render_template("/cadastro/cadastro_marca.html", form=form)
