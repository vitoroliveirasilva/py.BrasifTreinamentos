from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from TREINAMENTO.forms.empresa_forms import EmpresaForm
from TREINAMENTO.models import Empresa
from . import empresa_bp 


@empresa_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_empresa(id):
    empresa = Empresa.query.get_or_404(id)
    form = EmpresaForm(obj=empresa)


    if form.validate_on_submit():
        try:
            Empresa.atualizar_empresa(empresa, form)
            db.session.commit()
            flash("Empresa atualizado com sucesso!", "success")
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


    return render_template("/edicao/edicao_empresa.html", form=form, empresa=empresa)
