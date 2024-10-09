from flask import render_template, redirect, url_for, flash
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from flask_login import login_required
from TREINAMENTO.forms.marca_tipo_forms import MarcaTipoForm
from TREINAMENTO.models import Marca, Tipo, MarcaTipo
from . import marca_tipo_bp


@marca_tipo_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro_colaborador():
    form = MarcaTipoForm()

    try:
        marcas = Marca.query.filter_by(status=True).all()
        if not marcas:
            flash("Nenhuma marca encontrada. Por favor, cadastre uma marca antes de registrar uma relação 'marca x tipo'.", "warning")
            form.id_marca.choices = []
        else:
            form.id_marca.choices = [(marca.id_marca, marca.nome) for marca in marcas]
            
        
        tipos = Tipo.query.filter_by(status=True).all()
        if not tipos:
            flash("Nenhum tipo encontrado. Por favor, cadastre um tipo antes de registrar uma relação 'marca x tipo'.", "warning")
            form.id_tipo.choices = []
        else:
            form.id_tipo.choices = [(tipo.id_tipo, tipo.nome) for tipo in tipos]

    except SQLAlchemyError as e:
        flash(f"Erro ao acessar o banco de dados ao carregar marcas e tipos: {str(e)}", "danger")
        form.id_marca.choices = []
        form.id_tipo.choices = []
    except Exception as e:
        flash(f"Erro inesperado ao carregar as opções: {str(e)}", "danger")
        form.id_marca.choices = []
        form.id_tipo.choices = []

    
    if form.validate_on_submit():
        try:
            marca_tipo = MarcaTipo.cadastro_marca_tipo(form)
            db.session.add(marca_tipo)
            db.session.commit()
            flash("Relação 'marca x tipo' registrada com sucesso!", "success")
            return redirect(url_for("tabela.marcas_por_empresa"))
        
        except ValueError as ve:
            db.session.rollback()
            flash(str(ve), "warning")

        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f"Erro ao acessar o banco de dados: {str(e)}", "danger")

        except Exception as e:
            db.session.rollback()
            flash(f"Erro inesperado: {str(e)}", "danger")

    return render_template("/cadastro/cadastro_marca_tipo.html", form=form)

