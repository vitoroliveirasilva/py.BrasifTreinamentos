from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from TREINAMENTO.forms.treinamento_forms import TreinamentoForm
from TREINAMENTO.models import Treinamento, Marca, Tipo
from . import treinamento_bp


@treinamento_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_treinamento(id):
    treinamento = Treinamento.query.get_or_404(id)
    form = TreinamentoForm(obj=treinamento)


    try:
        tipos = Tipo.query.filter_by(status=True).all()
        marcas = Marca.query.filter_by(status=True).all()
        
        if not tipos:
            flash("Nenhum tipo encontrado. Por favor, cadastre um tipo antes de cadastrar um treinamento.", "warning")
            form.id_tipo.choices = []
        else:
            form.id_tipo.choices = [(tipo.id_tipo, tipo.nome) for tipo in tipos]

        if not marcas:
            flash("Nenhuma marca encontrado. Por favor, cadastre uma marca antes de cadastrar um treinamento.", "warning")
            form.id_marca.choices = []
        else:
            form.id_marca.choices = [(marca.id_marca, marca.nome) for marca in marcas]

    except SQLAlchemyError as e:
        flash(f"Erro ao acessar o banco de dados ao carregar os marcas: {str(e)}", "danger")
        form.id_tipo.choices = []
        form.id_marca.choices = []

    except Exception as e:
        flash(f"Erro inesperado: {str(e)}", "danger")
        form.id_tipo.choices = []
        form.id_marca.choices = []

    
    if form.validate_on_submit():
        try:
            Treinamento.atualizar_treinamento(treinamento, form)
            db.session.commit()
            flash("Treinamento atualizado com sucesso!", "success")
            return redirect(url_for("tipo.cadastro_tipo"))
        
        except ValueError as ve:
            db.session.rollback()
            flash(str(ve), "warning")

        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f"Erro ao acessar o banco de dados: {str(e)}", "danger")

        except Exception as e:
            db.session.rollback()
            flash(f"Erro inesperado: {str(e)}", "danger")
    
    
    return render_template("/edicao/edicao_treinamento.html", form=form, treinamento=treinamento)
