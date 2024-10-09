from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class MarcaForm(FlaskForm):
    # Nome da marca
    nome = StringField("Nome da marca", validators=[
        DataRequired(message="O nome do marca é obrigatório."),
        Length(max=50, message="O nome do marca deve ter no máximo 50 caracteres.")
    ])

    # Status da marca (ativo/inativo)
    status = BooleanField('Ativo', default=True)

    submit = SubmitField('Salvar')
