from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from TREINAMENTO import db
from sqlalchemy.exc import SQLAlchemyError
from TREINAMENTO.forms.login_forms import LoginForm
from TREINAMENTO.models import Login, Colaborador, Marca, MarcaTipo, Tipo
from . import login_bp 


@login_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_login(id):
    login = Login.query.get_or_404(id)
    form = LoginForm(obj=login)

    try:
        colaboradores = Colaborador.query.filter_by(status=True).all()
        if not colaboradores:
            flash("Nenhum colaborador encontrado. Por favor, cadastre um colaborador antes de cadastrar um login.", "warning")
            form.id_colaborador.choices = []
        else:
            form.id_colaborador.choices = [(colaborador.id_colaborador, colaborador.nome) for colaborador in colaboradores]
        
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
        form.id_colaborador.choices = []
        form.id_marca_tipo.choices = []
        
    except Exception as e:
        flash(f"Erro inesperado ao carregar as opções: {str(e)}", "danger")
        form.id_colaborador.choices = []
        form.id_marca_tipo.choices = []


    if form.validate_on_submit():
        try:
            login.atualizar_login(form)
            db.session.commit()
            flash("Login atualizado com sucesso!", "success")
            return redirect(url_for("tabela.tabela_logins", id=id))
        
        except ValueError as ve:
            db.session.rollback()
            flash(str(ve), "warning")

        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f"Erro ao acessar o banco de dados: {str(e)}", "danger")

        except Exception as e:
            db.session.rollback()
            flash(f"Erro inesperado: {str(e)}", "danger")

    return render_template("/edicao/edicao_login.html", form=form, login=login)
