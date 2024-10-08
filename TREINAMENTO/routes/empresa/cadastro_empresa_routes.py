from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from TREINAMENTO.forms.empresa_forms import EmpresaForm
from TREINAMENTO.models import Empresa, Filiais
from . import empresa_bp 


@empresa_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro_empresa():
    form = EmpresaForm()

    try:
        if not Filiais:
            flash("Nenhuma filial encontrada. Por favor, abra um chamado para a T.I. para que o problema possa ser solucionado.", "danger")
            form.filial.choices = []
        else:
            form.filial.choices = [(filial.name, filial.value) for filial in Filiais]
            
    except SQLAlchemyError as e:
        flash(f"Erro ao acessar o banco de dados ao carregar as empresas: {str(e)}", "danger")
        form.filial.choices = []
    except Exception as e:
        flash(f"Erro inesperado ao carregar as opções: {str(e)}", "danger")
        form.filial.choices = []
    

    if form.validate_on_submit():
        try:
            empresa = Empresa.cadastro_empresa(form)
            db.session.add(empresa)
            db.session.commit()
            flash("Empresa cadastrada com sucesso!", "success")
            return redirect(url_for("empresa.cadastro_empresa"))
        
        except ValueError as ve:
            db.session.rollback()
            flash(str(ve), "warning")

        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f"Erro ao acessar o banco de dados: {str(e)}", "danger")

        except Exception as e:
            db.session.rollback()
            flash(f"Erro inesperado: {str(e)}", "danger")

    
    return render_template("/cadastro/cadastro_empresa.html", form=form)
