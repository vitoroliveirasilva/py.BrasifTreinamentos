from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required
from TREINAMENTO.forms.inscricao import InscricaoTreinamentoForm
from TREINAMENTO.models import Tipo, Treinamento, Marca
from . import inscricao_bp


@inscricao_bp.route("/", methods=["GET", "POST"])
@login_required
def inscricao():
    form = InscricaoTreinamentoForm()

    tipos = Tipo.query.filter(Tipo.status == True).all()
    form.id_tipo.choices += [(tipo.id_tipo, tipo.nome) for tipo in tipos]

    marcas = Marca.query.filter(Marca.status == True).all()
    form.id_marca.choices += [(marca.id_marca, marca.nome) for marca in marcas]
    
    treinamentos = Treinamento.query.filter(Treinamento.status == True).all()
    form.id_treinamento.choices += [(treinamento.id_treinamento, treinamento.treinamento) for treinamento in treinamentos]

    if form.validate_on_submit():
        return redirect(url_for("inscricao.inscricao_colaborador", id=form.id_treinamento.data))
    
    return render_template("/inscricao/inscricao_treinamento.html", form=form)

@inscricao_bp.route("/get_marcas", methods=["GET"])
@login_required
def get_marcas():
    tipo_id = request.args.get('tipo_id')
    marcas = Marca.query.filter_by(id_tipo=tipo_id).all()
    marcas_options = '<option value="">Selecione uma Marca</option>'
    marcas_options += ''.join(f'<option value="{marca.id_marca}">{marca.nome}</option>' for marca in marcas)
    return marcas_options

@inscricao_bp.route("/get_treinamentos", methods=["GET"])
@login_required
def get_treinamentos():
    marca_id = request.args.get('marca_id')
    treinamentos = Treinamento.query.filter_by(id_marca=marca_id).all()
    treinamentos_options = '<option value="">Selecione um Treinamento</option>'
    treinamentos_options += ''.join(f'<option value="{treinamento.id_treinamento}">{treinamento.treinamento}</option>' for treinamento in treinamentos)
    return treinamentos_options
