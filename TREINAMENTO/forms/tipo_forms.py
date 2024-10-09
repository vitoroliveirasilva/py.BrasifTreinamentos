from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class TipoForm(FlaskForm):
    # Nome do tipo
    nome = StringField("Nome do tipo", validators=[
        DataRequired(message="O nome do tipo é obrigatório."),
        Length(max=50, message="O nome do tipo deve ter no máximo 50 caracteres.")
    ])

    # Status do tipo (ativo/inativo)
    status = BooleanField("Ativo", default=True)

    submit = SubmitField('Salvar')
