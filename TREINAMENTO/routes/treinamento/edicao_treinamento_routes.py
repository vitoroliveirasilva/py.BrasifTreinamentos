from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from TREINAMENTO.forms.treinamento_forms import TreinamentoForm
from TREINAMENTO.models import Treinamento, Marca, Tipo, MarcaTipo
from . import treinamento_bp


@treinamento_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_treinamento(id):
    treinamento = Treinamento.query.get_or_404(id)
    form = TreinamentoForm(obj=treinamento)

    try:
        # Carrega as combinações de Marca e Tipo que estão ativas no sistema
        marca_tipos = MarcaTipo.query.join(Marca).join(Tipo).filter(Marca.status == True, Tipo.status == True).all()

        if not marca_tipos:
            flash("Nenhuma combinação de marca e tipo disponível. Por favor, cadastre primeiro as relações de 'marca x tipo'.", "warning")
            form.id_marca_tipo.choices = []
        else:
            form.id_marca_tipo.choices = [
                (mt.id_marca_tipo, f"{mt.marca.nome} - {mt.tipo.nome}") for mt in marca_tipos
            ]

    except SQLAlchemyError as e:
        flash(f"Erro ao acessar o banco de dados: {str(e)}", "danger")
        form.id_marca_tipo.choices = []

    except Exception as e:
        flash(f"Erro inesperado: {str(e)}", "danger")
        form.id_marca_tipo.choices = []

    if form.validate_on_submit():
        try:
            Treinamento.atualizar_treinamento(treinamento, form)
            db.session.commit()
            flash("Treinamento atualizado com sucesso!", "success")
            return redirect(url_for("tabela.tabela_treinamentos"))

        except ValueError as ve:
            db.session.rollback()
            flash(str(ve), "warning")

        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f"Erro ao acessar o banco de dados: {str(e)}", "danger")

        except Exception as e:
            db.session.rollback()
            flash(f"Erro inesperado: {str(e)}", "danger")

    return render_template("/cadastro/cadastro_treinamento.html", form=form)
