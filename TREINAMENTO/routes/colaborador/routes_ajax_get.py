from flask import flash, request
from flask_login import login_required
from TREINAMENTO.models import Empresa
from . import colaborador_bp


# Obter as empresas através da filial selecionada no HTML (requisições AJAX javascript)
@colaborador_bp.route("/get_empresas", methods=["GET"])
@login_required
def get_empresas():
    filial = request.args.get('filial')

    if not filial:
        return flash(f"Nenhuma filial selecionada.", "danger")

    try:
        empresas = Empresa.query.filter_by(filial=filial, status=True).all()

        # Opções de empresa
        empresas_options = '<option value="">Selecione uma Empresa</option>'
        empresas_options += ''.join(f'<option value="{empresa.id_empresa}">{empresa.nome_empresa}</option>' for empresa in empresas)

        return empresas_options

    except Exception as e:
        return flash(f"Erro ao buscar empresas: {str(e)}", "danger")

