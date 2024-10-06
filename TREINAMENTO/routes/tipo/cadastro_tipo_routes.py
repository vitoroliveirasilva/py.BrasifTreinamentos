from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from TREINAMENTO.forms.tipo_forms import TipoForm
from TREINAMENTO.models import Tipo
from TREINAMENTO.utils import registro_existe
from . import tipo_bp


@tipo_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro_tipo():
    form = TipoForm()

    if form.validate_on_submit():
        try:
            if not registro_existe(Tipo, nome=form.nome.data):
                tipo = Tipo.cadastro_tipo(form)
                db.session.add(tipo)
                db.session.commit()
                flash("Tipo cadastrado com sucesso!", "success")
                return redirect(url_for("tabela.tabela_tipos"))
            else:
                flash(f"O tipo '{form.nome.data}' já existe. Por favor, escolha outro nome.", "warning")
        except SQLAlchemyError:
            db.session.rollback()
            flash("Erro ao acessar o banco de dados. Tente novamente.", "danger")
        except ValueError as value_erro:
            flash(str(value_erro), "danger")
        except Exception as e:
            flash(f"Erro inesperado ao registrar o centro: {str(e)}", "danger")
    elif form.errors:
        for campo, erros in form.errors.items():
            for erro in erros:
                flash(f"ERRO - {campo.upper()}: {erro}", "warning")

    return render_template("/cadastro/cadastro_tipo.html", form=form)
