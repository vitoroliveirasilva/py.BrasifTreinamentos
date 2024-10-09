from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    # Usuário do colaborador
    usuario = StringField("usuário", validators=[
        DataRequired(message="O usuário é obrigatório."),
        Length(max=50, message="O usuário deve ter no máximo 50 caracteres.")
    ])

    # Campo para selecionar o id do colaborador
    id_colaborador = SelectField('Colaborador', coerce=int, validators=[
        DataRequired(message="Por favor, selecione um colaborador.")
    ])

    # Campo para selecionar o id marca_tipo
    id_marca_tipo = SelectField('MarcaTipo', coerce=int, validators=[
        DataRequired(message="Por favor, selecione uma relação 'marca x tipo'.")
    ])

    # Status do tipo (ativo/inativo)
    status = BooleanField('Ativo', default=True)

    submit = SubmitField('Salvar')
