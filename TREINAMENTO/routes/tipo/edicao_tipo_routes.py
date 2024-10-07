from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from TREINAMENTO.forms.tipo_forms import TipoForm
from TREINAMENTO.models import Tipo
from . import tipo_bp


@tipo_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_tipo(id):
    tipo = Tipo.query.get_or_404(id)
    form = TipoForm(obj=tipo)

    if form.validate_on_submit():
        try:
            # Usa o método atualizar_tipo que já faz a validação do nome existente
            tipo.atualizar_tipo(form)
            db.session.commit()
            flash("Tipo atualizado com sucesso!", "success")
            return redirect(url_for("tabela.tabela_tipos"))

        except ValueError as ve:
            db.session.rollback()
            flash(str(ve), "warning")

        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f"Erro ao acessar o banco de dados: {str(e)}", "danger")

        except Exception as e:
            db.session.rollback()
            flash(f"Erro inesperado ao atualizar o tipo: {str(e)}", "danger")

    # Exibe os erros de validação do formulário
    elif form.errors:
        for campo, erros in form.errors.items():
            for erro in erros:
                flash(f"ERRO - {campo.upper()}: {erro}", "warning")


    return render_template("/edicao/edicao_tipo.html", form=form, tipo=tipo)
