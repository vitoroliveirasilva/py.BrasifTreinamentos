from flask import render_template, redirect, url_for, flash
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required, current_user
from TREINAMENTO.forms.colaborador_forms import ColaboradorForm
from TREINAMENTO.models import Colaborador, Empresa, Filiais
from . import colaborador_bp


@colaborador_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro_colaborador():
    form = ColaboradorForm()

    # Obtem o id do responsável logado
    try:
        id_responsavel = current_user.id
        if not id_responsavel:
            flash("Não foi possível obter o ID do usuário logado no sistema.", "danger")
            return redirect(url_for("home"))
    except Exception as e:
        flash(f"Erro inesperado ao obter id do usuário logado: {str(e)}", "danger")
        return redirect(url_for("home"))

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
            colaborador = Colaborador.cadastro_colaborador(form)
            colaborador.id_responsavel = id_responsavel  # Associa o responsável ao colaborador
            db.session.add(colaborador)
            db.session.commit()
            flash("Colaborador cadastrado com sucesso!", "success")
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

    return render_template("/cadastro/cadastro_colaborador.html", form=form)

