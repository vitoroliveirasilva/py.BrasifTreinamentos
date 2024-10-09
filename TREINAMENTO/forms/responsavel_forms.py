from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField


class ResponsavelForm(FlaskForm):
    # Permissão do responsável
    permissao = BooleanField("Permissão", default=False)

    # Status do responsável (ativo/inativo)
    status = BooleanField("Ativo", default=True)

    submit = SubmitField("Salvar")
