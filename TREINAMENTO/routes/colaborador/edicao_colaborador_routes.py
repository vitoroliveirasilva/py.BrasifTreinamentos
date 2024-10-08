from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from TREINAMENTO.forms.colaborador_forms import ColaboradorForm
from TREINAMENTO.models import Colaborador, Empresa, Filiais
from . import colaborador_bp


@colaborador_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_colaborador(id):
    colaborador = Colaborador.query.get_or_404(id)
    form = ColaboradorForm(obj=colaborador)


    # Carrega as filiais para o dropdown
    try:
        if not Filiais:
            flash("Nenhuma filial encontrada. Por favor, abra um chamado para a T.I. para que o problema possa ser solucionado.", "danger")
        else:
            form.filial.choices = [(filial.name, filial.value) for filial in Filiais]
            
        # Carregar empresas ativas para o dropdown
        empresas = Empresa.query.filter_by(status=True).all()
        
        if not empresas:
            flash("Nenhuma empresa encontrada. Por favor, cadastre uma empresa antes de cadastrar um colaborador.", "warning")
        else:
            form.id_empresa.choices = [(empresa.id_empresa, empresa.nome_empresa) for empresa in empresas]

    except SQLAlchemyError as e:
        flash(f"Erro ao acessar o banco de dados ao carregar as empresas: {str(e)}", "danger")
        form.id_empresa.choices = []
    except Exception as e:
        flash(f"Erro inesperado ao carregar as opções: {str(e)}", "danger")
        form.id_empresa.choices = []


    # Processo de cadastro do colaborador
    if form.validate_on_submit():
        try:
            Colaborador.atualizar_colaborador(colaborador, form)
            db.session.commit()
            flash("Colaborador atualizado com sucesso!", "success")
            return redirect(url_for("colaborador.cadastro_colaborador"))
        
        except ValueError as ve:
            db.session.rollback()
            flash(str(ve), "warning")

        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f"Erro ao acessar o banco de dados: {str(e)}", "danger")

        except Exception as e:
            db.session.rollback()
            flash(f"Erro inesperado: {str(e)}", "danger")

    return render_template("/edicao/edicao_colaborador.html", form=form, colaborador=colaborador)
