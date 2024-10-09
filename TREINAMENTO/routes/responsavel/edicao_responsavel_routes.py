from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from TREINAMENTO.forms.responsavel_forms import ResponsavelForm
from TREINAMENTO.models import Responsavel
from . import responsavel_bp


@responsavel_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_responsavel(id):
    responsavel = Responsavel.query.get_or_404(id)
    form = ResponsavelForm(obj=responsavel)
    

    if form.validate_on_submit():
        try:
            responsavel.atualizar_responsavel(form)
            db.session.commit()
            flash("Responsável atualizado com sucesso!", "success")
            return redirect(url_for("tabela.tabela_responsaveis"))
        
        except ValueError as ve:
            db.session.rollback()
            flash(str(ve), "warning")

        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f"Erro ao acessar o banco de dados: {str(e)}", "danger")

        except Exception as e:
            db.session.rollback()
            flash(f"Erro inesperado: {str(e)}", "danger")

    return render_template("/edicao/edicao_responsavel.html", form=form, responsavel=responsavel)
